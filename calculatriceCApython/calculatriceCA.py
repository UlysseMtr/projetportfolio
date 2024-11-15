def calculatrice_chiffre_affaire():
    print("Calculatrice de Chiffre d'Affaires")
    print("La formule du chiffre d'affaires est :")
    print("Chiffre d'Affaires = Prix de Vente Unitaire × Quantité Vendue\n")

    try:
        prix_unitaire = float(input("Entrez le prix de vente unitaire (€) : "))
        quantite = int(input("Entrez la quantité vendue : "))
        
        chiffre_affaire = prix_unitaire * quantite
        print(f"\nChiffre d'affaires calculé : {chiffre_affaire:.2f} €")
    except ValueError:
        print("Erreur : Veuillez entrer des valeurs numériques valides.")

calculatrice_chiffre_affaire()