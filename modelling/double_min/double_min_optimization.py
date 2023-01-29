import random

import hyperopt
from hyperopt import hp, fmin, tpe, Trials
from hyperopt.pyll import scope
import pandas as pd
from analysis import data_prep, double_min_simulation
from matplotlib import pyplot as plt

"""
Some default values
last_min_window_atleast = 30
last_min_window_atmost = 90
after_double_min_atmost = 45

double_min_tolerance = 0.005
down_after_double_min_tolerance = 0.01
double_min_dim_atleast = 0.05
trailing_loss_perc = 0.02
"""

A = scope.int(hp.uniform('last_min_window_atleast', 3, 10))
B = scope.int(hp.uniform('last_min_window_atmost', 3, 50)) #A
C = scope.int(hp.uniform('after_double_min_atmost', 1, 20))
D = hp.uniform('double_min_tolerance', 0.0001, 0.05)
E = hp.uniform('down_after_double_min_tolerance', 0.001, 0.05) #D
F = hp.uniform('double_min_dim_atleast', 0.005, 0.1)
G = hp.uniform('trailing_loss_perc', 0.001, 0.05)


space = {"last_min_window_atleast": A, "last_min_window_atmost": B, "after_double_min_atmost": C,
         "double_min_tolerance": D, "down_after_double_min_tolerance": E, "double_min_dim_atleast": F,
         "trailing_loss_perc": G}

# df = data_prep(pd.read_csv("data/AAPL.csv"))
# partial_double_min_simulation = partial(double_min_simulation, input=df)
seed = random.randint(0, 9999)
random.seed(seed)
print(f"Using seed {seed}.")
trials = Trials()
best = fmin(double_min_simulation, space, algo=tpe.suggest, max_evals=10000, trials=trials)

print(f"Best config: {hyperopt.space_eval(space, best)}")
results = [-trial["loss"] for trial in trials.results]
pd.DataFrame(trials).to_csv("trials3.csv")

best_idx = 0
best = results[best_idx]
for i, res in enumerate(results[1:]):
    if res > best:
        plt.plot([best_idx, i+1], [best, res], c='r')
        best = res
        best_idx = i+1
plt.title(f"Best capital reached: {max(results)}")
plt.plot(results)
plt.show()
