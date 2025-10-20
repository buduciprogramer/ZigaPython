import tkinter as tk
from tkinter import messagebox, simpledialog
import datetime
import os

# Gosti lista i fajl
guests = []

def save_to_file():
    with open("guests.txt", "w", encoding="utf-8") as f:
        for g in guests:
            line = f"{g['first_name']},{g['last_name']},{g['room']},{g['checkin']},{g['checkout']},{g['total']},{g['restaurant_total']}\n"
            f.write(line)

def load_from_file():
    guests.clear()
    try:
        with open("guests.txt", "r", encoding="utf-8") as f:
            for line in f:
                first_name, last_name, room, checkin, checkout, total, restaurant_total = line.strip().split(",")
                guests.append({
                    "first_name": first_name,
                    "last_name": last_name,
                    "room": room,
                    "checkin": checkin,
                    "checkout": checkout,
                    "total": float(total),
                    "restaurant_total": float(restaurant_total)
                })
    except FileNotFoundError:
        pass

# Funkcije

def gui_add_guest():
    add_window = tk.Toplevel()
    add_window.title("Dodaj gosta")
    add_window.geometry("300x400")

    labels = ["Ime", "Prezime", "Broj sobe", "Check-in (YYYY-MM-DD)", "Check-out (YYYY-MM-DD)", "Cijena po danu"]
    entries = []

    for label in labels:
        tk.Label(add_window, text=label).pack()
        entry = tk.Entry(add_window)
        entry.pack()
        entries.append(entry)

    def submit_guest():
        try:
            first_name = entries[0].get().strip()
            last_name = entries[1].get().strip()
            room_number = entries[2].get().strip()
            checkin_date = entries[3].get().strip()
            checkout_date = entries[4].get().strip()
            price_per_day = float(entries[5].get().replace(",", ".").strip())

            if not first_name or not last_name or not room_number:
                raise ValueError("Ime, prezime i broj sobe ne smeju biti prazni.")

            d1 = datetime.datetime.strptime(checkin_date, "%Y-%m-%d")
            d2 = datetime.datetime.strptime(checkout_date, "%Y-%m-%d")
            number_of_days = (d2 - d1).days
            if number_of_days <= 0:
                raise ValueError("Datum odjave mora biti posle datuma prijave.")

            total_price = number_of_days * price_per_day

            guests.append({
                "first_name": first_name,
                "last_name": last_name,
                "room": room_number,
                "checkin": checkin_date,
                "checkout": checkout_date,
                "total": total_price,
                "restaurant_total": 0.0
            })

            save_to_file()
            messagebox.showinfo("Uspeh", f"Gost {first_name} {last_name} dodat. Ukupno: {total_price:.2f} KM")
            add_window.destroy()
        except Exception as e:
            messagebox.showerror("Greška", str(e))

    tk.Button(add_window, text="Dodaj gosta", command=submit_guest).pack(pady=20)

def gui_show_all():
    show_window = tk.Toplevel()
    show_window.title("Lista gostiju")
    show_window.geometry("800x400")

    text = tk.Text(show_window)
    text.pack(expand=True, fill="both")

    if not guests:
        text.insert("end", "Nema unesenih gostiju.")
        return

    total_all = 0
    for g in guests:
        total_bill = g['total'] + g['restaurant_total']
        total_all += total_bill
        text.insert("end", f"{g['first_name']} {g['last_name']} - Soba: {g['room']} - {g['checkin']} → {g['checkout']} - "
                           f"Boravak: {g['total']:.2f} KM - Restoran: {g['restaurant_total']:.2f} KM - UKUPNO: {total_bill:.2f} KM\n")

    text.insert("end", f"\nUkupan iznos za sve goste: {total_all:.2f} KM")

def delete_guest():
    last_name = simpledialog.askstring("Brisanje gosta", "Unesite prezime gosta:")
    if not last_name:
        return
    global guests
    before = len(guests)
    guests = [g for g in guests if g["last_name"].lower() != last_name.lower()]
    save_to_file()
    after = len(guests)
    if before == after:
        messagebox.showinfo("Brisanje", "Gost nije pronađen.")
    else:
        messagebox.showinfo("Brisanje", "Gost obrisan.")

def search_guest():
    room = simpledialog.askstring("Pretraga", "Unesite broj sobe:")
    if not room:
        return
    for g in guests:
        if g["room"] == room:
            messagebox.showinfo("Gost pronađen", f"{g['first_name']} {g['last_name']} - {g['checkin']} → {g['checkout']}")
            return
    messagebox.showinfo("Pretraga", "Gost nije pronađen.")

def order_food():
    room = simpledialog.askstring("Narudžba", "Unesite broj sobe:")
    if not room:
        return
    guest_found = next((g for g in guests if g["room"] == room), None)
    if not guest_found:
        messagebox.showerror("Greška", "Soba nije pronađena.")
        return

    menu = {
        "1": ("Masala Dosa", 130),
        "2": ("Butter Naan", 20),
        "3": ("Paneer Dosa", 130),
        "4": ("Tea", 10),
        "5": ("Coffee", 15),
    }

    total = 0
    while True:
        menu_str = "\n".join([f"{code}. {item} - {price} KM" for code, (item, price) in menu.items()])
        choice = simpledialog.askstring("Meni", f"{menu_str}\nOdaberi broj artikla (ili 0 za kraj):")
        if choice is None or choice == "0":
            break
        elif choice in menu:
            item, price = menu[choice]
            total += price
            messagebox.showinfo("Dodano", f"Dodano: {item} - {price} KM")
        else:
            messagebox.showwarning("Neispravno", "Pogrešan unos.")

    if total > 0:
        guest_found["restaurant_total"] += total
        save_to_file()
        messagebox.showinfo("Račun", f"Ukupan račun za hranu: {total} KM")

# Login i lozinka

def create_owner_credentials_file():
    if not os.path.exists("owner_credentials.txt"):
        with open("owner_credentials.txt", "w", encoding="utf-8") as f:
            f.write("admin,admin\n")

def login_screen(root):
    root.title("Prijava vlasnika")
    root.geometry("300x230")

    for widget in root.winfo_children():
        widget.destroy()

    tk.Label(root, text="Korisničko ime:").pack(pady=5)
    username_entry = tk.Entry(root)
    username_entry.pack()

    tk.Label(root, text="Lozinka:").pack(pady=5)
    password_entry = tk.Entry(root, show="*")
    password_entry.pack()

    def check_login():
        username = username_entry.get().strip()
        password = password_entry.get().strip()

        try:
            with open("owner_credentials.txt", "r", encoding="utf-8") as f:
                for line in f:
                    user, pwd = line.strip().split(",")
                    if username == user and password == pwd:
                        main_gui(root)
                        return
        except FileNotFoundError:
            messagebox.showerror("Greška", "Fajl sa podacima o vlasniku nije pronađen.")
            return

        messagebox.showerror("Greška", "Pogrešno korisničko ime ili lozinka.")

    def open_change_password():
        def submit_new_password():
            old_pwd = old_entry.get()
            new_pwd = new_entry.get()
            confirm_pwd = confirm_entry.get()

            try:
                with open("owner_credentials.txt", "r", encoding="utf-8") as f:
                    user, pwd = f.readline().strip().split(",")
            except FileNotFoundError:
                messagebox.showerror("Greška", "Fajl sa podacima o vlasniku nije pronađen.")
                change_pw_window.destroy()
                return

            if old_pwd != pwd:
                messagebox.showerror("Greška", "Stara lozinka nije tačna.")
                return

            if new_pwd != confirm_pwd:
                messagebox.showerror("Greška", "Lozinke se ne poklapaju.")
                return

            if not new_pwd:
                messagebox.showerror("Greška", "Nova lozinka ne može biti prazna.")
                return

            with open("owner_credentials.txt", "w", encoding="utf-8") as f:
                f.write(f"{user},{new_pwd}\n")

            messagebox.showinfo("Uspeh", "Lozinka je uspešno promenjena.")
            change_pw_window.destroy()

        change_pw_window = tk.Toplevel(root)
        change_pw_window.title("Promena lozinke")
        change_pw_window.geometry("300x200")

        tk.Label(change_pw_window, text="Stara lozinka:").pack()
        old_entry = tk.Entry(change_pw_window, show="*")
        old_entry.pack()

        tk.Label(change_pw_window, text="Nova lozinka:").pack()
        new_entry = tk.Entry(change_pw_window, show="*")
        new_entry.pack()

        tk.Label(change_pw_window, text="Potvrdi novu lozinku:").pack()
        confirm_entry = tk.Entry(change_pw_window, show="*")
        confirm_entry.pack()

        tk.Button(change_pw_window, text="Promeni lozinku", command=submit_new_password).pack(pady=10)

    tk.Button(root, text="Prijavi se", command=check_login).pack(pady=10)
    tk.Button(root, text="Promeni lozinku", command=open_change_password).pack()

# Glavni meni

def main_gui(root):
    for widget in root.winfo_children():
        widget.destroy()

    root.title("Hotel Management System")
    root.geometry("400x400")

    tk.Label(root, text="Hotel Management Menu", font=("Arial", 16)).pack(pady=10)

    tk.Button(root, text="1. Dodaj gosta", width=30, command=gui_add_guest).pack(pady=5)
    tk.Button(root, text="2. Prikaži sve goste", width=30, command=gui_show_all).pack(pady=5)
    tk.Button(root, text="3. Obriši gosta", width=30, command=delete_guest).pack(pady=5)
    tk.Button(root, text="4. Pretraga po sobi", width=30, command=search_guest).pack(pady=5)
    tk.Button(root, text="5. Naruči hranu", width=30, command=order_food).pack(pady=5)
    tk.Button(root, text="6. Izlaz", width=30, command=root.quit).pack(pady=20)

# Start

if __name__ == "__main__":
    load_from_file()
    create_owner_credentials_file()
    root = tk.Tk()
    login_screen(root)
    root.mainloop()