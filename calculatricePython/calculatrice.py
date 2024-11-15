def calculatrice():
    print("Choisissez une opération :")
    print("1. Addition")
    print("2. Soustraction")
    print("3. Division")
    print("4. Multiplication")
    print("5. Puissance")
    print("6. Modulo")
    print("7. Valeur absolue")

    choix = input("Entrez le numéro de l'opération : ")
    if choix in ['1', '2', '3', '4', '5', '6']:
        num1 = float(input("Entrez le premier nombre : "))
        num2 = float(input("Entrez le deuxième nombre : "))
        if choix == '1':
            print(f"Résultat : {num1 + num2}")
        elif choix == '2':
            print(f"Résultat : {num1 - num2}")
        elif choix == '3':
            if num2 != 0:
                print(f"Résultat : {num1 / num2}")
            else:
                print("Erreur : Division par zéro.")
        elif choix == '4':
            print(f"Résultat : {num1 * num2}")
        elif choix == '5':
            print(f"Résultat : {num1 ** num2}")
        elif choix == '6':
            print(f"Résultat : {num1 % num2}")
    elif choix == '7':
        num = float(input("Entrez un nombre : "))
        print(f"Valeur absolue : {abs(num)}")
    else:
        print("Choix invalide.")

calculatrice()
