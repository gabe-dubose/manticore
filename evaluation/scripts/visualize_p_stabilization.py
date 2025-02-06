#!/usr/bin/env python3

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.lines import Line2D

# load data
data = pd.read_csv('../data/p_var_data.csv', index_col=0)
data = data.sort_values(by='tree.size', ascending=True)

var_data = (
    data.groupby(['tree.size', 'replicate.pair', 'metric', 'iterations'])
    .agg(stdev_p=('p', 'std'))
    .reset_index()
)
var_data = var_data.sort_values(by="tree.size", ascending=True)

# plot var data

sns.set_style('whitegrid')
fig, [[ax1,ax2,ax3,ax4], [ax5,ax6,ax7,ax8]] = plt.subplots(2, 4, figsize=(10,5), sharey=True, sharex=True)

order = [5, 10, 20, 40, 60, 80, 100]
var_data['tree.size'] = pd.Categorical(var_data['tree.size'], categories=order, ordered=True)

# Robinson-foulds
sns.lineplot(var_data.loc[var_data['metric'] == 'RF'], 
             x='iterations', y='stdev_p', hue='tree.size', ax=ax1, legend=False,
             palette='viridis', style='tree.size', linewidth=3)

ax1.set_xscale('log')
ax1.set_title('RF')
ax1.set_ylabel(r's.d. of $P(Null \geq Observed)$', fontsize=12)
ax1.set_xlabel('')
ax1.tick_params(axis='y', labelsize=12)

# Information-corrected Robinson-foulds
sns.lineplot(var_data.loc[var_data['metric'] == 'ICRF'], 
             x='iterations', y='stdev_p', hue='tree.size', ax=ax2, legend=False,
             palette='viridis', style='tree.size', linewidth=3)

ax2.set_xscale('log')
ax2.set_title('ICRF')
ax2.set_ylabel('')
ax2.set_xlabel('')

# Jaccard Robinson-foulds
sns.lineplot(var_data.loc[var_data['metric'] == 'JRF'], 
             x='iterations', y='stdev_p', hue='tree.size', ax=ax3, legend=False,
             palette='viridis', style='tree.size', linewidth=3)

ax3.set_xscale('log')
ax3.set_title('JRF')
ax3.set_ylabel('')
ax3.set_xlabel('')

# Nye Similarity
sns.lineplot(var_data.loc[var_data['metric'] == 'NS'], 
             x='iterations', y='stdev_p', hue='tree.size', ax=ax4,
             palette='viridis', style='tree.size', hue_order=order, style_order=order,
             linewidth=3)

# make legend
handles, labels = ax4.get_legend_handles_labels()
unique_labels = list(dict.fromkeys(labels))
unique_handles = [handles[labels.index(lbl)] for lbl in unique_labels]
unique_handles = [Line2D([], [], color=h.get_color(), linestyle=h.get_linestyle(), linewidth=3) for h in unique_handles]

# Set the new legend
ax4.legend(
    unique_handles, unique_labels, 
    bbox_to_anchor=(1.05, 1.05), loc='upper left', title='n Leaves',
    fontsize=12, title_fontsize=12
)

ax4.set_xscale('log')
ax4.set_title('NS')
ax4.set_ylabel('')
ax4.set_xlabel('')

# Mutual clustering information
sns.lineplot(var_data.loc[var_data['metric'] == 'MCI'], 
             x='iterations', y='stdev_p', hue='tree.size', ax=ax5, legend=False,
             palette='viridis', style='tree.size', linewidth=3)

ax5.set_xscale('log')
ax5.set_title('MCI')
ax5.set_ylabel(r's.d. of $P(Null \geq Observed)$', fontsize=12)
ax5.set_xlabel('Iterations', fontsize=12)
ax5.set_xticks([10**1, 10**2, 10**3, 10**4])
ax5.set_xticklabels([r'$10^1$', r'$10^2$', r'$10^3$', r'$10^4$'], fontsize=12)
ax5.tick_params(axis='y', labelsize=12)

# Shared phylogenetic information (Note that I had a typo in the abbreviation for this)
sns.lineplot(var_data.loc[var_data['metric'] == 'SPI'], 
             x='iterations', y='stdev_p', hue='tree.size', ax=ax6, legend=False,
             palette='viridis', style='tree.size', linewidth=3)

ax6.set_xscale('log')
ax6.set_title('SPI')
ax6.set_ylabel('')
ax6.set_xlabel('Iterations', fontsize=12)
ax6.set_xticks([10**1, 10**2, 10**3, 10**4])
ax6.set_xticklabels([r'$10^1$', r'$10^2$', r'$10^3$', r'$10^4$'], fontsize=12)

# Matching split distance
sns.lineplot(var_data.loc[var_data['metric'] == 'MSD'], 
             x='iterations', y='stdev_p', hue='tree.size', ax=ax7, legend=False,
             palette='viridis', style='tree.size', linewidth=3)

ax7.set_xscale('log')
ax7.set_title('MSD')
ax7.set_ylabel('')
ax7.set_xlabel('Iterations', fontsize=12)
ax7.set_xticks([10**1, 10**2, 10**3, 10**4])
ax7.set_xticklabels([r'$10^1$', r'$10^2$', r'$10^3$', r'$10^4$'], fontsize=12)
ax7.tick_params(axis='y', labelsize=12)

# Matching split information distance
sns.lineplot(var_data.loc[var_data['metric'] == 'MSID'], 
             x='iterations', y='stdev_p', hue='tree.size', ax=ax8, legend=False,
             palette='viridis', style='tree.size', linewidth=3)

ax8.set_xscale('log')
ax8.set_title('MSID')
ax8.set_ylabel('')
ax8.set_xlabel('Iterations', fontsize=12)
ax8.set_xticks([10**1, 10**2, 10**3, 10**4])
ax8.set_xticklabels([r'$10^1$', r'$10^2$', r'$10^3$', r'$10^4$'], fontsize=12)

# add subplto labels
ax1.text(8.5**4,0.165, 'A', fontsize=15)
ax2.text(8.5**4,0.165, 'B', fontsize=15)
ax3.text(8.5**4,0.165, 'C', fontsize=15)
ax4.text(8.5**4,0.165, 'D', fontsize=15)
ax5.text(8.5**4,0.165, 'E', fontsize=15)
ax6.text(8.5**4,0.165, 'F', fontsize=15)
ax7.text(8.5**4,0.165, 'G', fontsize=15)
ax8.text(8.5**4,0.165, 'H', fontsize=15)

plt.tight_layout()
plt.savefig('../figures/p_stabilization.png', dpi=600)
plt.savefig('../figures/p_stabilization.pdf')
