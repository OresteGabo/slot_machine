
NOMBRE_LIGNES_MAX = 3
# La fonction pour faire un dépot
# Le montant doit etre positif
def depot():
    """

    :rtype: Return int
    """
    while True:
        amount =input("Combien souhaitez-vous déposer $")
        if amount.isdigit():
            amount=int(amount)
            if amount >= 0:
                break
            else:
                print("Le montant doit etre superieur à 0")
        else:
            print("Le montant doit etre numerique")
    return amount

# L'utilisateur doit saisir lenombre de ligne
# Le nombre doit etre d'abord numerique, et superieur à zero
def get_nombre_lignes():
    """

    :rtype: Return int
    """
    while True:
        lignes =input("Combien de ligne souhaitez-vous parier (1-"+ str(NOMBRE_LIGNES_MAX)+ ") $")
        if lignes.isdigit():
            lignes=int(lignes)
            if lignes >= 0:
                break
            else:
                print("Le montant doit etre superieur à 0")
        else:
            print("Le montant doit etre numerique")
    return lignes



def main():
    balance=depot()
    lignes=get_nombre_lignes()
    print(balance,lignes)


main()