import time
import os
import paraules

tipus, paraula = paraules.retorna_paraula()

lletres_entrades = []

errors = 0
paraules_encertades = 0

print("Benvingut al joc del Penjat")
nom = input("Escriu el teu nom: ")

encertada = False
while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("###### JOC DEL PENJAT ######")
    print(f"Jugador: {nom}             Paraules encertades: {str(paraules_encertades)}")
    # Dibuixa pista
    print(f"{tipus} de {len(paraula)} lletres\n")

    # Ha encertat.
    # Demanem nova paraula i comprovem si s'han acabat
    if encertada:
        nova_paraula =  paraules.retorna_paraula()
        if not nova_paraula:
            print("\nENHORABONA. HAS GUANYAT!!!!")
            break;
        else:
            tipus = nova_paraula[0]
            paraula = nova_paraula[1]
            lletres_entrades.clear()
            encertada = False

    # Dibuixa paraula i comprova si s'ha encertat
    encertada = True
    for lletra in paraula:
        if lletra in lletres_entrades:
            print(f"{lletra:3}", end=" ")
        else:
            print(f"{'__':3}", end=" ")
            encertada = False

    # Mostra errors / Dibuixa penjat i controla el Game Over sortint del bucle
    #print(f"\nErrors: {errors}")
    if (errors >= 1):
        print("\n\n---------|")
    if (errors >= 2):
        print("         o")
    if (errors >= 3):
        print("        /|\\")
    if (errors >=4):
        print("        / \\")
        print("\nHAS PERDUT!!!")
        time.sleep(2)
        break;
 
    if encertada:
       paraules_encertades += 1
       continue

    # Demana nova lletra
    lletra = input("\nIntrodueix una lletra: ").capitalize()
    if lletra not in lletres_entrades:
        lletres_entrades.append(lletra)
        if lletra not in paraula:
            errors += 1

