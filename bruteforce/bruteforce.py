import itertools
import csv
from dataclasses import dataclass
from memory_profiler import profile
from time import perf_counter

@dataclass(slots=True, frozen=True)
class Action:
    """Objet représentant une action."""
    name: str
    cost: float
    profit: float

    @property
    def calculated_profit(self):
        """Calcule et affiche le profit de l'action."""
        profit_calculation = float(self.cost) * (float(self.profit) / 100)
        rounded = round(profit_calculation, 2)
        return rounded
    
    def __repr__(self):
        return self.name
    

WALLET_AMOUNT = 500

bruteforce_data_path = "bruteforce/actionsv2.csv"
bruteforce_actions_data = []
combinations_list = []
combinations_cost = []

# @profile
def extract_csv_data(path: str, target_list: list):
    """Extrait les données d'un fichier CSV, crée chaque objet Action en découlant et les ajoute à la liste ciblée."""
    with open(path, encoding="utf-8") as data_file:
        reader = csv.reader(data_file)
        next(reader)
        for row in reader:
            target_list.append(Action(row[0], row[1], row[2]))

# @profile
def populate_share_combinations(data_source: list, target_list: list):
    """Crée toutes les combinaisons d'action possibles selon une liste existante et les ajoute à une autre liste ciblée."""
    for iteration in range(1, len(data_source) + 1):
        actions_combinations = itertools.combinations(data_source, iteration)
        for combination in actions_combinations:
            target_list.append(combination)

# @profile
def calculate_combinations_cost_and_profit(data_source: list, target_list: list):
    """Calcule le coût et le bénéfice généré par chaque combinaison issue de la liste existante et l'ajoute à la liste ciblée."""
    for combination in data_source:
        action_sum = 0
        total_profit = 0
    
        for action in combination:
            action_sum += float(action.cost)
            total_profit += float(action.calculated_profit)
            
        if action_sum <= WALLET_AMOUNT:
            target_list.append(("Action combination : ", combination, " || Combination cost : ",  action_sum, " || Profit : ", round(total_profit, 2)))

# @profile
def get_best_result(data_source: list):
    """Affiche la meilleure combinaison d'actions de la liste en paramètre."""
    ranked_combinations = sorted(data_source, key=lambda x: x[5], reverse=True)
    best_result = ranked_combinations[0]

    best_result_formatted = "{}{}{}{}{}{}".format(
        best_result[0],
        best_result[1],
        best_result[2],
        best_result[3],
        best_result[4],
        best_result[5],
    )

    print("Best combination : ", best_result_formatted)


extract_csv_data(bruteforce_data_path, bruteforce_actions_data)
populate_share_combinations(bruteforce_actions_data, combinations_list)
calculate_combinations_cost_and_profit(combinations_list, combinations_cost)
get_best_result(combinations_cost)




# Mesure du temps d'exécution des fonctions

# cProfile.run("extract_csv_data(bruteforce_data_path, bruteforce_actions_data)")
# cProfile.run("populate_share_combinations(bruteforce_actions_data, combinations_list)")
# cProfile.run("calculate_combinations_cost_and_profit(combinations_list, combinations_cost)")
# cProfile.run("get_best_result(combinations_cost)")


"""

def performance(func):
    Monitor process time for a function
    def wrapper(*args, **kwargs):
        t1 = perf_counter()
        result = func(*args, **kwargs)
        t2 = perf_counter()
        print(f"\nThe function {func.__name__} took {round(t2 - t1, 5)} s")
        return result

    return wrapper


# action_list = [("Action-1", 20, 0.05), 
#                ("Action-2", 30, 0.10),
#                ("Action-3", 50, 0.15),
#                ("Action-4", 70, 0.20),
#                ("Action-5", 60, 0.17),
#                ("Action-6", 80, 0.25),
#                ("Action-7", 22, 0.07),
#                ("Action-8", 26, 0.11),
#                ("Action-9", 48, 0.13),
#                ("Action-10", 34, 0.27),
#                ("Action-11", 42, 0.17),
#                ("Action-12", 110, 0.09),
#                ("Action-13", 38, 0.23),
#                ("Action-14", 14, 0.01),
#                ("Action-15", 18, 0.03),
#                ("Action-16", 8, 0.08),
#                ("Action-17", 4, 0.12),
#                ("Action-18", 10, 0.14),
#                ("Action-19", 24, 0.21),
#                ("Action-20", 114, 0.18)]





"""