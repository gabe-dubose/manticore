#!/usr/bin/env python3

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.lines import Line2D

# load data
#load HA data
hA_data = pd.read_csv('../data/power_simulation_data.csv', index_col=0)
hA_data['significance'] = np.where(hA_data['p'] < 0.05, 1, 0)

# load HO data
h0_data = pd.read_csv('../data/random_pairs_data.csv', index_col=0)
h0_data['significance'] = np.where(h0_data['p'] < 0.05, 1, 0)

# initialize dataframes
metrics = list(hA_data['metric'].unique())
tree_sizes = list(hA_data['tree.size'].unique())
hA_agreement_data = pd.DataFrame(0, columns=metrics, index=metrics)
hA_comps_data = pd.DataFrame(0, columns=metrics, index=metrics)
h0_agreement_data = pd.DataFrame(0, columns=metrics, index=metrics)
h0_comps_data = pd.DataFrame(0, columns=metrics, index=metrics)

# define replicate chunks
chunks = [list(range(i, i + 8)) for i in range(1, len(hA_data), 8)]
for chunk in chunks:
    subset = hA_data.loc[chunk]
    # iterate through metric comparisons
    for m1 in metrics:
        for m2 in metrics:
            if m1 != m2:
                comp = subset.loc[(subset['metric'] == m1) | (subset['metric'] == m2)]
                # add 1 to dataframe if agreement is met
                if comp['significance'].sum() == 0 or comp['significance'].sum() == 2:
                    hA_agreement_data.loc[m1, m2] = hA_agreement_data.loc[m1, m2] + 1
                # add 1 to comparison
                hA_comps_data.loc[m1, m2] = hA_comps_data.loc[m1, m2] + 1
            if m1 == m2:
                # add 1 to diagonal
                hA_agreement_data.loc[m1, m2] = hA_agreement_data.loc[m1, m2] + 1
                # add 1 to comparison
                hA_comps_data.loc[m1, m2] = hA_comps_data.loc[m1, m2] + 1

# define replicate chunks
chunks = [list(range(i, i + 8)) for i in range(1, len(h0_data), 8)]
for chunk in chunks:
    subset = h0_data.loc[chunk]
    # iterate through metric comparisons
    for m1 in metrics:
        for m2 in metrics:
            if m1 != m2:
                comp = subset.loc[(subset['metric'] == m1) | (subset['metric'] == m2)]
                # add 1 to dataframe if agreement is met
                if comp['significance'].sum() == 0 or comp['significance'].sum() == 2:
                    h0_agreement_data.loc[m1, m2] = h0_agreement_data.loc[m1, m2] + 1
                # add 1 to comparison
                h0_comps_data.loc[m1, m2] = h0_comps_data.loc[m1, m2] + 1
            if m1 == m2:
                # add 1 to diagonal
                h0_agreement_data.loc[m1, m2] = h0_agreement_data.loc[m1, m2] + 1
                # add 1 to comparison
                h0_comps_data.loc[m1, m2] = h0_comps_data.loc[m1, m2] + 1

import warnings
warnings.filterwarnings("ignore")

# define percent agreements
hA_agreement = hA_agreement_data / hA_comps_data
hA_agreement = (hA_agreement + hA_agreement.T) / 2
hA_mask = np.triu(np.ones_like(hA_agreement, dtype=bool), k=0)

h0_agreement = h0_agreement_data / h0_comps_data
h0_agreement = (h0_agreement + h0_agreement.T) / 2
h0_mask = np.triu(np.ones_like(h0_agreement, dtype=bool), k=0)

sns.set_style('whitegrid')
fig, [ax1, ax2] = plt.subplots(1, 2, figsize=(10, 5))

# define color bar
vmin = min(hA_agreement.min().min(), h0_agreement.min().min())
vmax = max(hA_agreement.max().max(), h0_agreement.max().max())

sns.heatmap(data=hA_agreement, annot=True, mask=hA_mask, 
            cmap='viridis_r', ax=ax1, cbar=False,
           vmin=vmin, vmax=vmax)
sns.heatmap(data=h0_agreement, annot=True, mask=h0_mask, 
            cmap='viridis_r', ax=ax2, cbar=False, 
           vmin=vmin, vmax=vmax)

ax1.tick_params(axis='x', labelsize=12)
ax1.tick_params(axis='y', labelsize=12)

ax2.tick_params(axis='x', labelsize=12)
ax2.tick_params(axis='y', labelsize=12)

# add color bar
cbar_ax = fig.add_axes([1, 0.07, 0.02, 0.9])  # [left, bottom, width, height]
norm = plt.Normalize(vmin=vmin, vmax=vmax)
sm = plt.cm.ScalarMappable(cmap="viridis_r", norm=norm)
sm.set_array([])
cbar = fig.colorbar(sm, cax=cbar_ax, ticks=np.arange(0.75, 1.01, 0.05))
cbar.set_label("% Agreement", fontsize=12)
cbar.ax.tick_params(labelsize=12)

fig.text(0.01, 1, 'A', fontsize=17)
fig.text(0.504, 1, 'B', fontsize=17)

plt.tight_layout()

plt.savefig('../figures/pct_agreement.png', dpi=600, bbox_inches='tight')
plt.savefig('../figures/pct_agreement.pdf', bbox_inches='tight')                   