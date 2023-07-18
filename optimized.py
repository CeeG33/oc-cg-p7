import bruteforce

# Fichier de données source.
data_path = "dataset2_Python+P7.csv"

def calculate_action_cost_and_profit(data: list):
    """Calcule le coût et le bénéfice généré par la combinaison cible."""
    action_sum = 0
    total_profit = 0
    action_list = []
    
    for action in data:
        action_sum += float(action.cost)
        total_profit += float(action.calculated_profit)
        action_list.append(action)

    return print(f"Combination : {action_list} || Combination cost : {round(action_sum, 2)} || Profit : {round(total_profit, 2)}")


# Fonction principale

# Décommenter la ligne ci-dessous pour mesurer le temps d'exécution.
# @bruteforce.performance

# Décommenter la ligne ci-dessous pour mesurer l'allocation mémoire.
# @bruteforce.profile
def main():
    # Définition du montant du porte-feuille client.
    wallet_amount = 500
    csv_data = bruteforce.extract_csv_data(data_path)
    actions_data_sorted = sorted(csv_data, reverse=True)

    resultat = []

    for action in actions_data_sorted:
        if (wallet_amount - float(action.cost)) >= 0:
            resultat.append(action)
            wallet_amount = wallet_amount - float(action.cost)

    calculate_action_cost_and_profit(resultat)

main()
