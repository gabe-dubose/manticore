#!/usr/bin/env python3

import pandas as pd
import numpy as np
import statsmodels.api as sm

# load data
data = pd.read_csv('../data/random_pairs_data.csv', index_col=0)
data = data.sort_values(by='tree.size', ascending=True)
data['significance'] = np.where(data['p'] < 0.05, 1, 0)

# min-max normalize congruence values for easier comparison
data['normalized_congruence'] = data.groupby(['tree.size', 'metric'])['congruence'].transform(lambda x: (x - x.min()) / (x.max() - x.min()))

for (metric, tree_size), group in data.groupby(['metric', 'tree.size']):
    X = group[['normalized_congruence']]
    y = group['significance']

    # Check if all y values are the same (all 0s or all 1s)
    if y.nunique() == 1:
        print(f"Skipping metric {metric}, tree.size {tree_size}: all values in 'significance' are {y.iloc[0]}")
        continue  # Skip fitting the model

    # Add an intercept
    X = sm.add_constant(X)

    # Fit logistic regression
    try:
        model = sm.Logit(y, X).fit(disp=0)  # disp=0 suppresses output
        print(f"\nLogistic regression results for metric {metric}, tree.size {tree_size}:\n")
        print(model.summary())
    except np.linalg.LinAlgError:
        print(f"Skipping metric {metric}, tree.size {tree_size}: singular matrix issue")