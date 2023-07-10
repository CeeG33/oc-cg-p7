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

wallet = 500
actions_data = {}

with open("bruteforce/actionsv2.csv", "r", encoding="utf-8") as data_file:
    reader = csv.DictReader(data_file)
    for row in reader:
        share_name = row["Actions #"]
        cost_per_share = int(row["Coût par action (en euros)"])
        profit = int(row["Bénéfice (après 2 ans)"])
        actions_data[share_name] = [cost_per_share, profit]
    
for share_name, data in actions_data.items():
    print(share_name, data)

print(actions_data["Action-1"])


"""
print("Data brute : " + str(data_source))
print("Premier de la liste : " + data_source[0])

actions_combinations = itertools.combinations(data_source, 2)

combinations_list = []

for (share, benefit) in actions_combinations:
    combinations_list.append(share + benefit)

print("Test combinaisons : " + str(combinations_list))
"""