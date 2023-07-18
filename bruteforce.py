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
    
    def __lt__(self, other):
        return self.profit < other.profit
    
# Définition du montant du porte-feuille client.
wallet_amount = 500

# Fichier de données source.
bruteforce_data_path = "actions.csv"


def extract_csv_data(path: str):
    """Extrait les données d'un fichier CSV, crée chaque objet Action en découlant."""
    bruteforce_actions_data = []
    
    with open(path, encoding="utf-8") as data_file:
        reader = csv.reader(data_file)
        next(reader)
        for row in reader:
            if float(row[1]) > 0:
                bruteforce_actions_data.append(Action(row[0], float(row[1]), float(row[2])))
    
    return bruteforce_actions_data


def populate_share_combinations(data_source: list):
    """Crée toutes les combinaisons d'action possibles selon une liste existante."""
    combinations_list = []

    for iteration in range(1, len(data_source) + 1):
        actions_combinations = itertools.combinations(data_source, iteration)
        for combination in actions_combinations:
            combinations_list.append(combination)

    return combinations_list


def calculate_combinations_cost_and_profit(data_source: list):
    """Calcule le coût et le bénéfice généré par chaque combinaison issue de la liste existante."""
    combinations_cost = []

    for combination in data_source:
        action_sum = 0
        total_profit = 0
    
        for action in combination:
            action_sum += float(action.cost)
            total_profit += float(action.calculated_profit)
            
        if action_sum <= wallet_amount:
            combinations_cost.append(("Action combination : ", combination, " || Combination cost : ",  action_sum, " || Profit : ", round(total_profit, 2)))

    return combinations_cost


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


def performance(func):
    """Décorateur qui calcule le temps d'exécution d'une fonction."""
    def wrapper(*args, **kwargs):
        t1 = perf_counter()
        result = func(*args, **kwargs)
        t2 = perf_counter()
        print(f"La fonction '{func.__name__}' s'est exécutée en {round(t2 - t1, 5)} s")
        return result

    return wrapper


# Fonction principale

# Décommenter la ligne ci-dessous pour mesurer le temps d'exécution.
# @performance

# Décommenter la ligne ci-dessous pour mesurer l'allocation mémoire.
# @profile
def main():
    csv_data = extract_csv_data(bruteforce_data_path)
    combinations = populate_share_combinations(csv_data)
    combinations_cost = calculate_combinations_cost_and_profit(combinations)
    get_best_result(combinations_cost)

if __name__ == "__main__":
    main()
