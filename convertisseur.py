#Tuple () : immutable -> non modifiable
#Liste [] : mutable -> rajouter/supprimer ou modifier des éléments
from forex_python.converter import CurrencyRates

# Fonction pour obtenir les taux de change
def get_exchange_rate(base_currency, target_currency):
    c = CurrencyRates()
    try:
        rate = c.get_rate(base_currency, target_currency)
        return rate
    except Exception as e:
        raise ValueError(f"Erreur lors de la récupération du taux de change : {e}")

# Fonction pour afficher les devises disponibles
def display_available_currencies():
    c = CurrencyRates()
    currencies = c.get_rates("USD")
    print("Devises disponibles : ", ", ".join(currencies.keys()))

# Fonction pour effectuer la conversion
def convert_currency():
    while True:
        try:
            somme = float(input("Veuillez entrer la somme à convertir : "))
            monnaie_depart = input("Quelle est votre monnaie d'origine ? ").upper()
            monnaie_final = input("En quoi voulez-vous convertir votre monnaie ? ").upper()

            # Validation des devises
            if monnaie_depart.upper() != "USD" and monnaie_depart.upper() not in c.get_rates("USD"):
                raise ValueError("La devise d'origine n'est pas valide.")
            if monnaie_final.upper() != "USD" and monnaie_final.upper() not in c.get_rates("USD"):
                raise ValueError("La devise de conversion n'est pas valide.")

            # Appelle la fonction qui utilise la bibliothèque forex-python pour obtenir le taux de change
            taux_echange = get_exchange_rate(monnaie_depart, monnaie_final)

            # Effectue la conversion en utilisant le taux de change récupéré
            montant_converti = somme * taux_echange

            # Donne le résultat de la conversion
            print(somme, monnaie_depart, "équivaut à", montant_converti, monnaie_final)

            # Ajoute la conversion à l'historique
            historique.append((somme, monnaie_depart, montant_converti, monnaie_final))

            # Demande à l'utilisateur s'il souhaite effectuer une autre conversion
            continuer = input("Voulez-vous effectuer une autre conversion ? (Oui/Non) ")

            # Si la réponse n'est pas 'oui', la boucle est interrompue, sinon, l'utilisateur peut effectuer une autre conversion
            if continuer not in ("oui", "o", "Oui", "O"):
                break  # Utilisation de break pour sortir de la boucle

        except ValueError as e:
            print(f"Erreur : {e}")
            continue

# Fonction pour afficher l'historique des conversions
def display_conversion_history():
    print("\nHistorique des conversions :")
    for i, conversion in enumerate(historique, 1):
        somme, monnaie_depart, montant_converti, monnaie_final = conversion
        print(f"{i}. {somme} {monnaie_depart} équivaut à {montant_converti} {monnaie_final}")

# Utilisation d'une boucle infinie pour permettre à l'utilisateur de faire plusieurs conversions
historique = []
c = CurrencyRates()
display_available_currencies()
convert_currency()

# À la fin du programme, affiche l'historique des conversions
display_conversion_history()