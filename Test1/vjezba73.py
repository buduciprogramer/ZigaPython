recenica=input("Unesi recenicu")

zabranjene_rijeci=[]
print("Unesi 5 zabranjenih rijeci")
for i in range(5):
    rijec=input(f"{i+1}")
    zabranjene_rijeci.append(rijec)
    
    rijeci_u_recenici=recenica.split()
    
    nova_recenica=[]
    
    for rijec in rijeci_u_recenici:
        rijec_cista=rijec.strip('.,!?').lower()
        if rijec_cista in zabranjene_rijeci:
            nova_recenica.append("mačka")
    else:
        nova_recenica.append(rijec)
        izmijenjena_recenica = ' '.join(nova_recenica)