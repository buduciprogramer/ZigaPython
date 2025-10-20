import numpy as np

tickers=np.array(["AAPL","MSFT","JNJ"])
kupovna_cijena=np.array([150,250,160])
trenutna_cijena=np.array([195,330,150])
komada=np.array([10,5,7])


investirano=kupovna_cijena*komada
vrijednost_danas=trenutna_cijena*komada
profit=vrijednost_danas-investirano
prinos_postotak=(profit/investirano)*100

for i in range(len(tickers)):
    print(f"{tickers[i]} | Investirano: {investirano[i]:.2f} | Vrijednost: {vrijednost_danas[i]:.2f} | Profit: {profit[i]:.2f} | Prinos: {prinos_postotak[i]:.2f}%")

naj_index = np.argmax(profit)
print(f"\nNajprofitabilnija dionica: {tickers[naj_index]} sa profitom od {profit[naj_index]:.2f} ({prinos_postotak[naj_index]:.2f}%)")


promjena_cijene = trenutna_cijena - kupovna_cijena

# Dionica s najvećim porastom cijene
max_index = np.argmax(promjena_cijene)
print(f"Dionica s najvećim porastom cijene: {tickers[max_index]} ({promjena_cijene[max_index]})")

# Dionica s najvećim padom cijene
min_index = np.argmin(promjena_cijene)
print(f"Dionica s najvećim padom cijene: {tickers[min_index]} ({promjena_cijene[min_index]})")

# Portfelj s porastom cijene
porast_mask = promjena_cijene > 0
portfolio_porast = np.extract(porast_mask, tickers)
print(f"\nPortfolio s porastom cijena: {portfolio_porast}")

# Portfelj s padom cijene
pad_mask = promjena_cijene < 0
portfolio_pad = np.extract(pad_mask, tickers)
print(f"Portfolio s padom cijena: {portfolio_pad}")