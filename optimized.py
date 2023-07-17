import bruteforce

bruteforce_data_path = "actions.csv"
bruteforce_actions_data = []

def calculate_action_cost_and_profit(data: list):
    action_sum = 0
    total_profit = 0
    action_list = []
    for action in data:
        action_sum += float(action.cost)
        total_profit += float(action.calculated_profit)
        action_list.append(action)

    return print(f"Combination : {action_list} || Combination cost : {action_sum} || Profit : {round(total_profit, 2)}")


# Fonction principale

# @bruteforce.performance
# @bruteforce.profile
def main():
    WALLET_AMOUNT = 500
    bruteforce.extract_csv_data(bruteforce_data_path, bruteforce_actions_data)
    actions_data_sorted = sorted(bruteforce_actions_data, reverse=True)

    print(actions_data_sorted)

    resultat = []

    for action in actions_data_sorted:
        if (WALLET_AMOUNT - float(action.cost)) >= 0 and float(action.cost) > 0:
            resultat.append(action)
            WALLET_AMOUNT = WALLET_AMOUNT - float(action.cost)

    calculate_action_cost_and_profit(resultat)

main()





