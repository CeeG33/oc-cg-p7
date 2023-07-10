import itertools
import csv

action_list = [("Action-1", 20, 0.05), 
               ("Action-2", 30, 0.10),
               ("Action-3", 50, 0.15),
               ("Action-4", 70, 0.20),
               ("Action-5", 60, 0.17),
               ("Action-6", 80, 0.25),
               ("Action-7", 22, 0.07),
               ("Action-8", 26, 0.11),
               ("Action-9", 48, 0.13),
               ("Action-10", 34, 0.27),
               ("Action-11", 42, 0.17),
               ("Action-12", 110, 0.09),
               ("Action-13", 38, 0.23),
               ("Action-14", 14, 0.01),
               ("Action-15", 18, 0.03),
               ("Action-16", 8, 0.08),
               ("Action-17", 4, 0.12),
               ("Action-18", 10, 0.14),
               ("Action-19", 24, 0.21),
               ("Action-20", 114, 0.18)]

wallet_amount = 500
actions_data = {}

with open("bruteforce/actionsv2.csv", "r", encoding="utf-8") as data_file:
    reader = csv.DictReader(data_file)
    for row in reader:
        share_name = row["Actions #"]
        cost_per_share = int(row["Coût par action (en euros)"])
        profit = int(row["Bénéfice (après 2 ans)"])
        actions_data[share_name] = [cost_per_share, profit]
    
"""for share_name, data in actions_data.items():
    print(share_name, data)
"""

print(actions_data["Action-1"][0])

actions_combinations = itertools.combinations(actions_data, 10)

combinations_list = []

for combination in actions_combinations:
    combinations_list.append(combination)

combinations_cost = []


for combination in combinations_list:
    action_sum = 0
    total_profit = 0
    for action in combination:
        share = actions_data[action][0]
        action_sum += share

        action_profit = actions_data[action][1] / 100
        calculated_profit = share * action_profit
        total_profit += calculated_profit
        
    if action_sum <= wallet_amount:
        combinations_cost.append(("Action combination : ", combination, "Combination cost : ", action_sum, "Profit : ", round(total_profit, 2)))

combinations_ranked = sorted(combinations_cost, key=lambda x: x[5], reverse=True)
print("Meilleure combinaison : " + str(combinations_ranked[0]))
print("Pire combinaison : " + str(combinations_ranked[-1]))

"""
"""