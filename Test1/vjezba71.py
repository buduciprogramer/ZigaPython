koraci=[]

for i in range(7):
    unos=int(input(f"Unesite broj koraka za dan{i + 1}:"))
    koraci.append(unos)
    
    aktivni_dani=0
    for broj_koraka in koraci:
        if broj_koraka>10000:
            aktivni_dani+=1
            
            print(f"Sandine je imala {aktivni_dani} aktivnih dana ove sedmice.")