#!/usr/bin/env python3

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.lines import Line2D

#load data
data = pd.read_csv('../data/power_simulation_data.csv', index_col=0)
data['significance'] = np.where(data['p'] < 0.05, 1, 0)
data['pct_div'] = data['movements'] / data['tree.size']

sns.set_style('whitegrid')
fig, [[ax1,ax2,ax3,ax4], [ax5,ax6,ax7,ax8]] = plt.subplots(2, 4, figsize=(10,5), sharey=True, sharex=True)

line_styles = ['-', '--', '-.', ':']
tree_sizes = data.loc[data['metric'] == 'RF']['tree.size'].unique()
line_style_map = {size: line_styles[i % len(line_styles)] for i, size in enumerate(tree_sizes)}

# Robinson-foulds
for tree_size in tree_sizes:
    # subset data
    subset = data[(data['metric'] == 'RF') & (data['tree.size'] == tree_size)]
    # calculate proportions significant
    proportions = subset.groupby('pct_div')['significance'].mean().reset_index()
    proportions.columns = ['pct_div', 'proportion_significant']
    # plot
    sns.lineplot(data = proportions, x = 'pct_div', y = 'proportion_significant',
                label=f"{tree_size}",
                linewidth=2,
                color=sns.color_palette('viridis', len(tree_sizes))[list(tree_sizes).index(tree_size)],
                linestyle=line_style_map[tree_size],
                ax=ax1,
                legend=False)

ax1.set_title('RF')
ax1.set_ylabel('Proportion Significant', fontsize=12)
ax1.tick_params(axis='y', labelsize=12)
ax1.set_xticks([0, 0.1, 0.2, 0.3, 0.4, 0.5])

# Information-corrected Robinson-foulds
for tree_size in tree_sizes:
    # subset data
    subset = data[(data['metric'] == 'ICRF') & (data['tree.size'] == tree_size)]
    # calculate proportions significant
    proportions = subset.groupby('pct_div')['significance'].mean().reset_index()
    proportions.columns = ['pct_div', 'proportion_significant']
    # plot
    sns.lineplot(data = proportions, x = 'pct_div', y = 'proportion_significant',
                label=f"{tree_size}",
                linewidth=2,
                color=sns.color_palette('viridis', len(tree_sizes))[list(tree_sizes).index(tree_size)],
                linestyle=line_style_map[tree_size],
                ax=ax2,
                legend=False)

ax2.set_title('ICRF')

# Jaccard Robinson-foulds
for tree_size in tree_sizes:
    # subset data
    subset = data[(data['metric'] == 'JRF') & (data['tree.size'] == tree_size)]
    # calculate proportions significant
    proportions = subset.groupby('pct_div')['significance'].mean().reset_index()
    proportions.columns = ['pct_div', 'proportion_significant']
    # plot
    sns.lineplot(data = proportions, x = 'pct_div', y = 'proportion_significant',
                label=f"{tree_size}",
                linewidth=2,
                color=sns.color_palette('viridis', len(tree_sizes))[list(tree_sizes).index(tree_size)],
                linestyle=line_style_map[tree_size],
                ax=ax3,
                legend=False)

ax3.set_title('JRF')

# Nye similarity
for tree_size in tree_sizes:
    # subset data
    subset = data[(data['metric'] == 'NS') & (data['tree.size'] == tree_size)]
    # calculate proportions significant
    proportions = subset.groupby('pct_div')['significance'].mean().reset_index()
    proportions.columns = ['pct_div', 'proportion_significant']
    # plot
    sns.lineplot(data = proportions, x = 'pct_div', y = 'proportion_significant',
                label=f"{tree_size}",
                linewidth=2,
                color=sns.color_palette('viridis', len(tree_sizes))[list(tree_sizes).index(tree_size)],
                linestyle=line_style_map[tree_size],
                ax=ax4)
# Add legend
ax4.legend(
    bbox_to_anchor=(1.05, 1.05),
    loc='upper left',
    title=r'$n_\text{leaves}$',
    fontsize=12, title_fontsize=12
)

ax4.set_title('NS')

# Mutual Clustering Information
for tree_size in tree_sizes:
    # subset data
    subset = data[(data['metric'] == 'MCI') & (data['tree.size'] == tree_size)]
    # calculate proportions significant
    proportions = subset.groupby('pct_div')['significance'].mean().reset_index()
    proportions.columns = ['pct_div', 'proportion_significant']
    # plot
    sns.lineplot(data = proportions, x = 'pct_div', y = 'proportion_significant',
                label=f"{tree_size}",
                linewidth=2,
                color=sns.color_palette('viridis', len(tree_sizes))[list(tree_sizes).index(tree_size)],
                linestyle=line_style_map[tree_size],
                ax=ax5,
                legend = False)

ax5.set_title('MCI')
ax5.set_ylabel('Proportion Significant', fontsize=12)
ax5.tick_params(axis='y', labelsize=12)
ax5.set_xlabel(r'$\frac{\text{SPRs}}{n_\text{leaves}}$', fontsize=16)
ax5.tick_params(axis='x', labelsize=12)

# Shared Phylogenetic Information
for tree_size in tree_sizes:
    # subset data
    subset = data[(data['metric'] == 'SPI') & (data['tree.size'] == tree_size)]
    # calculate proportions significant
    proportions = subset.groupby('pct_div')['significance'].mean().reset_index()
    proportions.columns = ['pct_div', 'proportion_significant']
    # plot
    sns.lineplot(data = proportions, x = 'pct_div', y = 'proportion_significant',
                label=f"{tree_size}",
                linewidth=2,
                color=sns.color_palette('viridis', len(tree_sizes))[list(tree_sizes).index(tree_size)],
                linestyle=line_style_map[tree_size],
                ax=ax6,
                legend = False)

ax6.set_title('SPI')
ax6.set_xlabel(r'$\frac{\text{SPRs}}{n_\text{leaves}}$', fontsize=16)
ax6.tick_params(axis='x', labelsize=12)

# Matching Split Distance
for tree_size in tree_sizes:
    # subset data
    subset = data[(data['metric'] == 'MSD') & (data['tree.size'] == tree_size)]
    # calculate proportions significant
    proportions = subset.groupby('pct_div')['significance'].mean().reset_index()
    proportions.columns = ['pct_div', 'proportion_significant']
    # plot
    sns.lineplot(data = proportions, x = 'pct_div', y = 'proportion_significant',
                label=f"{tree_size}",
                linewidth=2,
                color=sns.color_palette('viridis', len(tree_sizes))[list(tree_sizes).index(tree_size)],
                linestyle=line_style_map[tree_size],
                ax=ax7,
                legend = False)

ax7.set_title('MSD')
ax7.set_xlabel(r'$\frac{\text{SPRs}}{n_\text{leaves}}$', fontsize=16)
ax7.tick_params(axis='x', labelsize=12)

# Matching Split Information Distance
for tree_size in tree_sizes:
    # subset data
    subset = data[(data['metric'] == 'MSID') & (data['tree.size'] == tree_size)]
    # calculate proportions significant
    proportions = subset.groupby('pct_div')['significance'].mean().reset_index()
    proportions.columns = ['pct_div', 'proportion_significant']
    # plot
    sns.lineplot(data = proportions, x = 'pct_div', y = 'proportion_significant',
                label=f"{tree_size}",
                linewidth=2,
                color=sns.color_palette('viridis', len(tree_sizes))[list(tree_sizes).index(tree_size)],
                linestyle=line_style_map[tree_size],
                ax=ax8,
                legend = False)

ax8.set_title('MSID')
ax8.set_xlabel(r'$\frac{\text{SPRs}}{n_\text{leaves}}$', fontsize=16)
ax8.tick_params(axis='x', labelsize=12)

# add reference lines
ax1.axhline(y=0.8, color='tab:gray', linestyle='-', linewidth=1.5)
ax2.axhline(y=0.8, color='tab:gray', linestyle='-', linewidth=1.5)
ax3.axhline(y=0.8, color='tab:gray', linestyle='-', linewidth=1.5)
ax4.axhline(y=0.8, color='tab:gray', linestyle='-', linewidth=1.5)
ax5.axhline(y=0.8, color='tab:gray', linestyle='-', linewidth=1.5)
ax6.axhline(y=0.8, color='tab:gray', linestyle='-', linewidth=1.5)
ax7.axhline(y=0.8, color='tab:gray', linestyle='-', linewidth=1.5)
ax8.axhline(y=0.8, color='tab:gray', linestyle='-', linewidth=1.5)

ax1.text(x=0, y=0.825, s='80% Power', fontsize=8, color='tab:gray')
ax2.text(x=0, y=0.825, s='80% Power', fontsize=8, color='tab:gray')
ax3.text(x=0, y=0.825, s='80% Power', fontsize=8, color='tab:gray')
ax4.text(x=0, y=0.825, s='80% Power', fontsize=8, color='tab:gray')
ax5.text(x=0, y=0.825, s='80% Power', fontsize=8, color='tab:gray')
ax6.text(x=0, y=0.825, s='80% Power', fontsize=8, color='tab:gray')
ax7.text(x=0, y=0.825, s='80% Power', fontsize=8, color='tab:gray')
ax8.text(x=0, y=0.825, s='80% Power', fontsize=8, color='tab:gray')

plt.tight_layout()

plt.savefig('../figures/power_curves.pdf')
plt.savefig('../figures/power_curves.png', dpi=600)