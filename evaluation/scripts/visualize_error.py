#!/usr/bin/env python3

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.lines import Line2D

# load data
data = pd.read_csv('../data/random_pairs_data.csv')
data['significance'] = np.where(data['p'] < 0.05, 1, 0)

# initialize dataframe
proportion_data = pd.DataFrame(columns = ['metric', 'tree_size', 'alpha', 'proportion'])
# assemble proportion data
alpha_levels = [0.05]
tree_sizes = data.loc[data['metric'] == 'RF']['tree.size'].unique()
metrics = list(data['metric'].unique())

row_index = 0
for metric in metrics:
    for tree_size in tree_sizes:
        # get subset
        subset = data[(data['metric'] == metric) & (data['tree.size'] == tree_size)]
        # calcualte portion leq alpha
        for alpha in alpha_levels:
            alpha_subset = subset[subset['p'] <= alpha]
            proportion = len(alpha_subset) / len(subset)
            #print(f"{metric}\t{tree_size}\t{alpha}\t{proportion}")
            proportion_data.loc[row_index] = [metric, tree_size, alpha, proportion]
            row_index += 1

sns.set_style('whitegrid')
fig, [[ax1,ax2,ax3,ax4], [ax5,ax6,ax7,ax8]] = plt.subplots(2, 4, figsize=(12,5), sharey=True, sharex=True)

# define line styles
line_styles = ['-', '--', '-.', ':']
tree_sizes = data.loc[data['metric'] == 'RF']['tree.size'].unique()
line_style_map = {size: line_styles[i % len(line_styles)] for i, size in enumerate(tree_sizes)}

# Robinson-Foulds
subset = proportion_data[proportion_data['metric'] == 'RF']
sns.lineplot(data=subset, x='tree_size', y='proportion', ax=ax1, color=sns.color_palette('viridis', 7)[0], 
                legend=False, linewidth=2)

ax1.set_ylim(-0.01, 0.07)
ax1.set_xlim(-0.01, 100)
ax1.axhline(y=0.05, color='tab:gray', linestyle='--', linewidth=2)
ax1.text(x=70, y=0.0525, s=r'$\alpha = 0.05$', fontsize=12, color='tab:gray')
ax1.set_ylabel(r'Proportion $\leq \alpha$', fontsize=12)
ax1.tick_params(axis='x', labelsize=12)
ax1.tick_params(axis='y', labelsize=12)
ax1.set_title('RF')
ax1.set_xticks([5, 10, 20, 40, 60, 80, 100])

# Information-corrected Robinson-foulds
subset = proportion_data[proportion_data['metric'] == 'ICRF']
sns.lineplot(data=subset, x='tree_size', y='proportion', ax=ax2, color=sns.color_palette('viridis', 7)[0], 
                legend=False, linewidth=2)

ax2.axhline(y=0.05, color='tab:gray', linestyle='--', linewidth=2)
ax2.text(x=70, y=0.0525, s=r'$\alpha = 0.05$', fontsize=12, color='tab:gray')
ax2.tick_params(axis='x', labelsize=12)
ax2.tick_params(axis='y', labelsize=12)
ax2.set_title('ICRF')

# Jaccard Robinson-foulds
subset = proportion_data[proportion_data['metric'] == 'JRF']
sns.lineplot(data=subset, x='tree_size', y='proportion', ax=ax3, color=sns.color_palette('viridis', 7)[0], 
                legend=False, linewidth=2)

ax3.axhline(y=0.05, color='tab:gray', linestyle='--', linewidth=2)
ax3.text(x=70, y=0.0525, s=r'$\alpha = 0.05$', fontsize=12, color='tab:gray')
ax3.tick_params(axis='x', labelsize=12)
ax3.tick_params(axis='y', labelsize=12)
ax3.set_title('JRF')

# Nye similarity
subset = proportion_data[proportion_data['metric'] == 'NS']
sns.lineplot(data=subset, x='tree_size', y='proportion', ax=ax4, color=sns.color_palette('viridis', 7)[0], 
                legend=False, linewidth=2)

ax4.axhline(y=0.05, color='tab:gray', linestyle='--', linewidth=2)
ax4.text(x=70, y=0.0525, s=r'$\alpha = 0.05$', fontsize=12, color='tab:gray')
ax4.tick_params(axis='x', labelsize=12)
ax4.tick_params(axis='y', labelsize=12)
ax4.set_title('NS')

# MCI
subset = proportion_data[proportion_data['metric'] == 'MCI']
sns.lineplot(data=subset, x='tree_size', y='proportion', ax=ax5, color=sns.color_palette('viridis', 7)[0], 
                legend=False, linewidth=2)

ax5.axhline(y=0.05, color='tab:gray', linestyle='--', linewidth=2)
ax5.text(x=70, y=0.0525, s=r'$\alpha = 0.05$', fontsize=12, color='tab:gray')
ax5.tick_params(axis='x', labelsize=12)
ax5.tick_params(axis='y', labelsize=12)
ax5.set_title('MCI')
ax5.set_ylabel(r'Proportion $\leq \alpha$', fontsize=12)
ax5.set_xlabel(r'$n_\text{leaves}$', fontsize=12)

# SPI
subset = proportion_data[proportion_data['metric'] == 'SPI']
sns.lineplot(data=subset, x='tree_size', y='proportion', ax=ax6, color=sns.color_palette('viridis', 7)[0], 
                legend=False, linewidth=2)

ax6.axhline(y=0.05, color='tab:gray', linestyle='--', linewidth=2)
ax6.text(x=70, y=0.0425, s=r'$\alpha = 0.05$', fontsize=12, color='tab:gray')
ax6.tick_params(axis='x', labelsize=12)
ax6.tick_params(axis='y', labelsize=12)
ax6.set_title('SPI')
ax6.set_xlabel(r'$n_\text{leaves}$', fontsize=12)

# MSD
subset = proportion_data[proportion_data['metric'] == 'MSD']
sns.lineplot(data=subset, x='tree_size', y='proportion', ax=ax7, color=sns.color_palette('viridis', 7)[0], 
                legend=False, linewidth=2)

ax7.axhline(y=0.05, color='tab:gray', linestyle='--', linewidth=2)
ax7.text(x=0, y=0.0525, s=r'$\alpha = 0.05$', fontsize=12, color='tab:gray')
ax7.tick_params(axis='x', labelsize=12)
ax7.tick_params(axis='y', labelsize=12)
ax7.set_title('MSD')
ax7.set_xlabel(r'$n_\text{leaves}$', fontsize=12)

# MSID
subset = proportion_data[proportion_data['metric'] == 'MSID']
sns.lineplot(data=subset, x='tree_size', y='proportion', ax=ax8, color=sns.color_palette('viridis', 7)[0], 
                legend=False, linewidth=2)

ax8.axhline(y=0.05, color='tab:gray', linestyle='--', linewidth=2)
ax8.text(x=70, y=0.0525, s=r'$\alpha = 0.05$', fontsize=12, color='tab:gray')
ax8.tick_params(axis='x', labelsize=12)
ax8.tick_params(axis='y', labelsize=12)
ax8.set_title('MSID')
ax8.set_xlabel(r'$n_\text{leaves}$', fontsize=12)

plt.tight_layout()

plt.savefig('../figures/error.png', dpi=600)
plt.savefig('../figures/error.pdf')