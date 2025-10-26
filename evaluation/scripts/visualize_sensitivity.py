#!/usr/bin/env python3

import json
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from matplotlib.lines import Line2D

data = '../data/rtc_sensitivity_results.json'
with open(data, 'r') as infile:
    data = json.load(infile)

metrics = list(data.keys())
tree_sizes = list(data[metrics[0]].keys())
order = ['RF', 'ICRF', 'JRF', 'NS', 'MCI', 'SPI', 'MSD', 'MSID']

# initialize plot
sns.set_style('whitegrid')
fig, [[ax1,ax2,ax3,ax4], [ax5,ax6,ax7,ax8]] = plt.subplots(2, 4, figsize=(10,5), sharey=True, sharex=True)
axes = [ax1, ax2, ax3, ax4, ax5, ax6, ax7, ax8]
colors = [sns.color_palette('viridis', 7)[i] for i in [2, 4, 6]]
linestyles = ['-', '--', '-.']

for i, metric in enumerate(order):
    for j, tree_size in enumerate(tree_sizes):
        results = data[metric][tree_size]
        #initialize list to store averages
        integrated_ps = []
        for result in results:
            integrated_p = result['integrated.p']
            integrated_ps.append(integrated_p)
            prop_div = result['prop.div']
            # plot
            sns.lineplot(x=prop_div, y=integrated_p, ax=axes[i], color = colors[j], linestyle=linestyles[j], alpha=0.3)
        # calculate mean and plot
        mean_int_p = np.mean(integrated_ps, axis=0)
        sns.lineplot(x=prop_div, y=mean_int_p, ax=axes[i], color = colors[j], linestyle=linestyles[j], alpha=1, linewidth=3)
        axes[i].text(x=0, y=0.06, s=r'$\alpha = 0.05$', color='tab:gray')
        # label
        axes[i].set_title(f'{metric}', fontsize=12)
    # plot alpha line
    axes[i].axhline(y=0.05, linewidth = 2, color='tab:gray', linestyle='--')

ax1.set_ylabel(r'Integrated $P(Null \geq Obs.)$', fontsize=12)
ax1.set_xticks([0, 0.1, 0.2, 0.3, 0.4, 0.5])
ax1.tick_params(axis='y', labelsize=12)
ax5.set_ylabel(r'Integrated $P(Null \geq Obs.)$', fontsize=12)
ax5.tick_params(axis='y', labelsize=12)
ax5.tick_params(axis='x', labelsize=12)
ax6.tick_params(axis='x', labelsize=12)
ax7.tick_params(axis='x', labelsize=12)
ax8.tick_params(axis='x', labelsize=12)
ax5.set_xlabel(r'$\frac{\text{SPRs}}{n_\text{leaves}}$', fontsize=12)
ax6.set_xlabel(r'$\frac{\text{SPRs}}{n_\text{leaves}}$', fontsize=12)
ax7.set_xlabel(r'$\frac{\text{SPRs}}{n_\text{leaves}}$', fontsize=12)
ax8.set_xlabel(r'$\frac{\text{SPRs}}{n_\text{leaves}}$', fontsize=12)

# add legend
legend_handles = [
    Line2D([0], [0],
           color=colors[j],
           linestyle=linestyles[j],
           linewidth=3,
           label=f"{tree_sizes[j]}")
    for j in range(len(tree_sizes))
]

axes[3].legend(
    handles=legend_handles,
    bbox_to_anchor=(1.05, 1.05),
    loc='upper left',
    title=r'$n_\text{leaves}$',
    fontsize=12,
    title_fontsize=12
)

plt.tight_layout()
plt.savefig('../figures/sensitivity.png', dpi=600)