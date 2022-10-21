

# La fonction pour faire un dépot
# Le montant doit etre positif
def deposit():
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



if __name__ == '__main__':
    deposit()
