#!/usr/bin/env python3

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.lines import Line2D
from sklearn.metrics import roc_curve, auc

#load HA data
hA_data = pd.read_csv('../data/power_simulation_data.csv', index_col=0)
hA_data['significance'] = np.where(hA_data['p'] < 0.05, 1, 0)
hA_data['pct_div'] = hA_data['movements'] / hA_data['tree.size']

# load HO data
h0_data = pd.read_csv('../data/random_pairs_data.csv', index_col=0)
h0_data['significance'] = np.where(h0_data['p'] < 0.05, 1, 0)

# initialize list to store aucs
auc_records = []

# define lines for tree sizes
line_styles = ['-', '--', '-.', ':']
tree_sizes = h0_data.loc[h0_data['metric'] == 'RF']['tree.size'].unique()
line_style_map = {size: line_styles[i % len(line_styles)] for i, size in enumerate(tree_sizes)}

sns.set_style('whitegrid')
fig, [[ax1,ax2,ax3,ax4], [ax5,ax6,ax7,ax8]] = plt.subplots(2, 4, figsize=(10,5), sharey=True, sharex=True)

# Robinson-Foulds
for tree_size in tree_sizes:
    h0_subset = h0_data[(h0_data['metric'] == 'RF') & (h0_data['tree.size'] == tree_size)]
    hA_subset = hA_data[(hA_data['metric'] == 'RF') & (hA_data['tree.size'] == tree_size)]
    p_values_null = list(h0_subset['p'])
    p_values_alt = list(hA_subset['p'])
    y_true = [0]*len(p_values_null) + [1]*len(p_values_alt)
    scores = p_values_null + p_values_alt
    fpr, tpr, thresholds = roc_curve(y_true, [-p for p in scores])
    roc_auc = auc(fpr, tpr)
    auc_records.append({'metric': 'RF', 'tree_size': tree_size, 'auc': roc_auc})
    
    sns.lineplot(x=fpr, y=tpr, ax=ax1,
                color=sns.color_palette('viridis', len(tree_sizes))[list(tree_sizes).index(tree_size)],
                linestyle=line_style_map[tree_size], label=f"{tree_size}", legend=False, linewidth=2)

# add random lines
ax1.plot([0, 1], [0, 1], linestyle='--', color='tab:gray', linewidth=2)
ax1.set_title('RF')
ax1.set_ylabel('True Positive Rate', fontsize=12)
ax1.text(x=0.5, y=0.7, s="Non-discriminative line", rotation=45, color='gray', fontsize=10, ha='center', va='top', alpha=1)
ax1.tick_params(axis='x', labelsize=12)
ax1.tick_params(axis='y', labelsize=12)

# Information-corrected Robinson-foulds
for tree_size in tree_sizes:
    h0_subset = h0_data[(h0_data['metric'] == 'ICRF') & (h0_data['tree.size'] == tree_size)]
    hA_subset = hA_data[(hA_data['metric'] == 'ICRF') & (hA_data['tree.size'] == tree_size)]
    p_values_null = list(h0_subset['p'])
    p_values_alt = list(hA_subset['p'])
    y_true = [0]*len(p_values_null) + [1]*len(p_values_alt)
    scores = p_values_null + p_values_alt
    fpr, tpr, thresholds = roc_curve(y_true, [-p for p in scores])
    roc_auc = auc(fpr, tpr)
    auc_records.append({'metric': 'ICRF', 'tree_size': tree_size, 'auc': roc_auc})
    
    sns.lineplot(x=fpr, y=tpr, ax=ax2,
                color=sns.color_palette('viridis', len(tree_sizes))[list(tree_sizes).index(tree_size)],
                linestyle=line_style_map[tree_size], label=f"{tree_size}", legend=False, linewidth=2)

# add random lines
ax2.plot([0, 1], [0, 1], linestyle='--', color='tab:gray', linewidth=2)
ax2.set_title('ICRF')
ax2.set_ylabel('True Positive Rate', fontsize=12)
ax2.text(x=0.5, y=0.7, s="Non-discriminative line", rotation=45, color='gray', fontsize=10, ha='center', va='top', alpha=1)
ax2.tick_params(axis='x', labelsize=12)
ax2.tick_params(axis='y', labelsize=12)

# Jaccard Robinson-foulds
for tree_size in tree_sizes:
    h0_subset = h0_data[(h0_data['metric'] == 'JRF') & (h0_data['tree.size'] == tree_size)]
    hA_subset = hA_data[(hA_data['metric'] == 'JRF') & (hA_data['tree.size'] == tree_size)]
    p_values_null = list(h0_subset['p'])
    p_values_alt = list(hA_subset['p'])
    y_true = [0]*len(p_values_null) + [1]*len(p_values_alt)
    scores = p_values_null + p_values_alt
    fpr, tpr, thresholds = roc_curve(y_true, [-p for p in scores])
    roc_auc = auc(fpr, tpr)
    auc_records.append({'metric': 'JRF', 'tree_size': tree_size, 'auc': roc_auc})
    
    sns.lineplot(x=fpr, y=tpr, ax=ax3,
                color=sns.color_palette('viridis', len(tree_sizes))[list(tree_sizes).index(tree_size)],
                linestyle=line_style_map[tree_size], label=f"{tree_size}", legend=False, linewidth=2)

# add random lines
ax3.plot([0, 1], [0, 1], linestyle='--', color='tab:gray', linewidth=2)
ax3.set_title('JRF')
ax3.set_ylabel('True Positive Rate', fontsize=12)
ax3.text(x=0.5, y=0.7, s="Non-discriminative line", rotation=45, color='gray', fontsize=10, ha='center', va='top', alpha=1)
ax3.tick_params(axis='x', labelsize=12)
ax3.tick_params(axis='y', labelsize=12)

# Nye similarity
for tree_size in tree_sizes:
    h0_subset = h0_data[(h0_data['metric'] == 'NS') & (h0_data['tree.size'] == tree_size)]
    hA_subset = hA_data[(hA_data['metric'] == 'NS') & (hA_data['tree.size'] == tree_size)]
    p_values_null = list(h0_subset['p'])
    p_values_alt = list(hA_subset['p'])
    y_true = [0]*len(p_values_null) + [1]*len(p_values_alt)
    scores = p_values_null + p_values_alt
    fpr, tpr, thresholds = roc_curve(y_true, [-p for p in scores])
    roc_auc = auc(fpr, tpr)
    auc_records.append({'metric': 'NS', 'tree_size': tree_size, 'auc': roc_auc})
    
    sns.lineplot(x=fpr, y=tpr, ax=ax4,
                color=sns.color_palette('viridis', len(tree_sizes))[list(tree_sizes).index(tree_size)],
                linestyle=line_style_map[tree_size], label=f"{tree_size}", legend=False, linewidth=2)

# add random lines
ax4.plot([0, 1], [0, 1], linestyle='--', color='tab:gray', linewidth=2)
ax4.set_title('NS')
ax4.set_ylabel('True Positive Rate', fontsize=12)
ax4.text(x=0.5, y=0.7, s="Non-discriminative line", rotation=45, color='gray', fontsize=10, ha='center', va='top', alpha=1)
ax4.tick_params(axis='x', labelsize=12)
ax4.tick_params(axis='y', labelsize=12)

# Add legend
ax4.legend(
    bbox_to_anchor=(1.05, 1.05),
    loc='upper left',
    title=r'$n_\text{leaves}$',
    fontsize=12, title_fontsize=12
)

# Mutual Clustering Information
for tree_size in tree_sizes:
    h0_subset = h0_data[(h0_data['metric'] == 'MCI') & (h0_data['tree.size'] == tree_size)]
    hA_subset = hA_data[(hA_data['metric'] == 'MCI') & (hA_data['tree.size'] == tree_size)]
    p_values_null = list(h0_subset['p'])
    p_values_alt = list(hA_subset['p'])
    y_true = [0]*len(p_values_null) + [1]*len(p_values_alt)
    scores = p_values_null + p_values_alt
    fpr, tpr, thresholds = roc_curve(y_true, [-p for p in scores])
    roc_auc = auc(fpr, tpr)
    auc_records.append({'metric': 'MCI', 'tree_size': tree_size, 'auc': roc_auc})
    
    sns.lineplot(x=fpr, y=tpr, ax=ax5,
                color=sns.color_palette('viridis', len(tree_sizes))[list(tree_sizes).index(tree_size)],
                linestyle=line_style_map[tree_size], label=f"{tree_size}", legend=False, linewidth=2)

# add random lines
ax5.plot([0, 1], [0, 1], linestyle='--', color='tab:gray', linewidth=2)
ax5.set_title('MCI')
ax5.set_ylabel('True Positive Rate', fontsize=12)
ax5.text(x=0.5, y=0.7, s="Non-discriminative line", rotation=45, color='gray', fontsize=10, ha='center', va='top', alpha=1)
ax5.set_xlabel('False Positive Rate', fontsize=12)
ax5.tick_params(axis='x', labelsize=12)
ax5.tick_params(axis='y', labelsize=12)

# Shared Phylogenetic Information
for tree_size in tree_sizes:
    h0_subset = h0_data[(h0_data['metric'] == 'SPI') & (h0_data['tree.size'] == tree_size)]
    hA_subset = hA_data[(hA_data['metric'] == 'SPI') & (hA_data['tree.size'] == tree_size)]
    p_values_null = list(h0_subset['p'])
    p_values_alt = list(hA_subset['p'])
    y_true = [0]*len(p_values_null) + [1]*len(p_values_alt)
    scores = p_values_null + p_values_alt
    fpr, tpr, thresholds = roc_curve(y_true, [-p for p in scores])
    roc_auc = auc(fpr, tpr)
    auc_records.append({'metric': 'SPI', 'tree_size': tree_size, 'auc': roc_auc})
    
    sns.lineplot(x=fpr, y=tpr, ax=ax6,
                color=sns.color_palette('viridis', len(tree_sizes))[list(tree_sizes).index(tree_size)],
                linestyle=line_style_map[tree_size], label=f"{tree_size}", legend=False, linewidth=2)

# add random lines
ax6.plot([0, 1], [0, 1], linestyle='--', color='tab:gray', linewidth=2)
ax6.set_title('SPI')
ax6.set_ylabel('True Positive Rate', fontsize=12)
ax6.text(x=0.5, y=0.7, s="Non-discriminative line", rotation=45, color='gray', fontsize=10, ha='center', va='top', alpha=1)
ax6.set_xlabel('False Positive Rate', fontsize=12)
ax6.tick_params(axis='x', labelsize=12)
ax6.tick_params(axis='y', labelsize=12)

# Matching Split Distance
for tree_size in tree_sizes:
    h0_subset = h0_data[(h0_data['metric'] == 'MSD') & (h0_data['tree.size'] == tree_size)]
    hA_subset = hA_data[(hA_data['metric'] == 'MSD') & (hA_data['tree.size'] == tree_size)]
    p_values_null = list(h0_subset['p'])
    p_values_alt = list(hA_subset['p'])
    y_true = [0]*len(p_values_null) + [1]*len(p_values_alt)
    scores = p_values_null + p_values_alt
    fpr, tpr, thresholds = roc_curve(y_true, [-p for p in scores])
    roc_auc = auc(fpr, tpr)
    auc_records.append({'metric': 'MSD', 'tree_size': tree_size, 'auc': roc_auc})
    
    sns.lineplot(x=fpr, y=tpr, ax=ax7,
                color=sns.color_palette('viridis', len(tree_sizes))[list(tree_sizes).index(tree_size)],
                linestyle=line_style_map[tree_size], label=f"{tree_size}", legend=False, linewidth=2)

# add random lines
ax7.plot([0, 1], [0, 1], linestyle='--', color='tab:gray', linewidth=2)
ax7.set_title('MSD')
ax7.set_ylabel('True Positive Rate', fontsize=12)
ax7.text(x=0.5, y=0.7, s="Non-discriminative line", rotation=45, color='gray', fontsize=10, ha='center', va='top', alpha=1)
ax7.set_xlabel('False Positive Rate', fontsize=12)
ax7.tick_params(axis='x', labelsize=12)
ax7.tick_params(axis='y', labelsize=12)

# Matching Split Information Distance
for tree_size in tree_sizes:
    h0_subset = h0_data[(h0_data['metric'] == 'MSID') & (h0_data['tree.size'] == tree_size)]
    hA_subset = hA_data[(hA_data['metric'] == 'MSID') & (hA_data['tree.size'] == tree_size)]
    p_values_null = list(h0_subset['p'])
    p_values_alt = list(hA_subset['p'])
    y_true = [0]*len(p_values_null) + [1]*len(p_values_alt)
    scores = p_values_null + p_values_alt
    fpr, tpr, thresholds = roc_curve(y_true, [-p for p in scores])
    roc_auc = auc(fpr, tpr)
    auc_records.append({'metric': 'MSID', 'tree_size': tree_size, 'auc': roc_auc})
    
    sns.lineplot(x=fpr, y=tpr, ax=ax8,
                color=sns.color_palette('viridis', len(tree_sizes))[list(tree_sizes).index(tree_size)],
                linestyle=line_style_map[tree_size], label=f"{tree_size}", legend=False, linewidth=2)

# add random lines
ax8.plot([0, 1], [0, 1], linestyle='--', color='tab:gray', linewidth=2)
ax8.set_title('MSID')
ax8.set_ylabel('True Positive Rate', fontsize=12)
ax8.text(x=0.5, y=0.7, s="Non-discriminative line", rotation=45, color='gray', fontsize=10, ha='center', va='top', alpha=1)
ax8.set_xlabel('False Positive Rate', fontsize=12)
ax8.tick_params(axis='x', labelsize=12)
ax8.tick_params(axis='y', labelsize=12)

plt.tight_layout()

plt.savefig('../figures/roc_curves.pdf')
plt.savefig('../figures/roc_curves.png', dpi=600)

# plot aucs
auc_dataframe = pd.DataFrame(auc_records)

sns.set_style('whitegrid')
fig, [[ax1,ax2,ax3,ax4], [ax5,ax6,ax7,ax8]] = plt.subplots(2, 4, figsize=(12,5), sharey=True, sharex=True)

# RF
auc_data = auc_dataframe.loc[auc_dataframe['metric'] == 'RF']
sns.lineplot(data=auc_data, x='tree_size', y='auc', ax=ax1, color=sns.color_palette('viridis', 7)[0], linewidth=2)
ax1.set_title('RF')
ax1.set_ylabel('Area Under ROC Curve', fontsize=12)
ax1.tick_params(axis='x', labelsize=12)
ax1.tick_params(axis='y', labelsize=12)
ax1.set_xticks([5, 10, 20, 40, 60, 80, 100])
ax1.set_ylim(0,1.05)

# ICRF
auc_data = auc_dataframe.loc[auc_dataframe['metric'] == 'ICRF']
sns.lineplot(data=auc_data, x='tree_size', y='auc', ax=ax2, color=sns.color_palette('viridis', 7)[0], linewidth=2)
ax2.set_title('ICRF')
ax2.set_ylabel('Area Under ROC Curve', fontsize=12)
ax2.tick_params(axis='x', labelsize=12)
ax2.tick_params(axis='y', labelsize=12)

# JRF
auc_data = auc_dataframe.loc[auc_dataframe['metric'] == 'JRF']
sns.lineplot(data=auc_data, x='tree_size', y='auc', ax=ax3, color=sns.color_palette('viridis', 7)[0], linewidth=2)
ax3.set_title('JRF')
ax3.set_ylabel('Area Under ROC Curve', fontsize=12)
ax3.tick_params(axis='x', labelsize=12)
ax3.tick_params(axis='y', labelsize=12)

# NS
auc_data = auc_dataframe.loc[auc_dataframe['metric'] == 'NS']
sns.lineplot(data=auc_data, x='tree_size', y='auc', ax=ax4, color='black', linewidth=2)
ax4.set_title('NS')
ax4.set_ylabel('Area Under ROC Curve', fontsize=12)
ax4.tick_params(axis='x', labelsize=12)
ax4.tick_params(axis='y', labelsize=12)

# MCI
auc_data = auc_dataframe.loc[auc_dataframe['metric'] == 'MCI']
sns.lineplot(data=auc_data, x='tree_size', y='auc', ax=ax5, color=sns.color_palette('viridis', 7)[0], linewidth=2)
ax5.set_title('MCI')
ax5.set_ylabel('Area Under ROC Curve', fontsize=12)
ax5.tick_params(axis='x', labelsize=12)
ax5.tick_params(axis='y', labelsize=12)
ax5.set_xlabel(r'$n_\text{leaves}$', fontsize=12)

# SPI
auc_data = auc_dataframe.loc[auc_dataframe['metric'] == 'SPI']
sns.lineplot(data=auc_data, x='tree_size', y='auc', ax=ax6, color=sns.color_palette('viridis', 7)[0], linewidth=2)
ax6.set_title('SPI')
ax6.set_ylabel('Area Under ROC Curve', fontsize=12)
ax6.tick_params(axis='x', labelsize=12)
ax6.tick_params(axis='y', labelsize=12)
ax6.set_xlabel(r'$n_\text{leaves}$', fontsize=12)

# MSD
auc_data = auc_dataframe.loc[auc_dataframe['metric'] == 'MSD']
sns.lineplot(data=auc_data, x='tree_size', y='auc', ax=ax7, color=sns.color_palette('viridis', 7)[0], linewidth=2)
ax7.set_title('MSD')
ax7.set_ylabel('Area Under ROC Curve', fontsize=12)
ax7.tick_params(axis='x', labelsize=12)
ax7.tick_params(axis='y', labelsize=12)
ax7.set_xlabel(r'$n_\text{leaves}$', fontsize=12)

# MSID
auc_data = auc_dataframe.loc[auc_dataframe['metric'] == 'MSID']
sns.lineplot(data=auc_data, x='tree_size', y='auc', ax=ax8, color=sns.color_palette('viridis', 7)[0], linewidth=2)
ax8.set_title('MSID')
ax8.set_ylabel('Area Under ROC Curve', fontsize=12)
ax8.set_xlabel(r'$n_\text{leaves}$', fontsize=12)
ax8.tick_params(axis='x', labelsize=12)
ax8.tick_params(axis='y', labelsize=12)

# add reference lines
ax1.axhline(y=0.5, xmin = 0.05, xmax = 0.95, color='tab:gray', linestyle='--', linewidth=2)
ax1.text(x=27.5, y=0.525, s='Non-discriminative line', fontsize=12, color='tab:gray')
ax2.axhline(y=0.5, xmin = 0.05, xmax = 0.95, color='tab:gray', linestyle='--', linewidth=2)
ax2.text(x=27.5, y=0.525, s='Non-discriminative line', fontsize=12, color='tab:gray')
ax3.axhline(y=0.5, xmin = 0.05, xmax = 0.95, color='tab:gray', linestyle='--', linewidth=2)
ax3.text(x=27.5, y=0.525, s='Non-discriminative line', fontsize=12, color='tab:gray')
ax4.axhline(y=0.5, xmin = 0.05, xmax = 0.95, color='tab:gray', linestyle='--', linewidth=2)
ax4.text(x=27.5, y=0.525, s='Non-discriminative line', fontsize=12, color='tab:gray')
ax5.axhline(y=0.5, xmin = 0.05, xmax = 0.95, color='tab:gray', linestyle='--', linewidth=2)
ax5.text(x=27.5, y=0.525, s='Non-discriminative line', fontsize=12, color='tab:gray')
ax6.axhline(y=0.5, xmin = 0.05, xmax = 0.95, color='tab:gray', linestyle='--', linewidth=2)
ax6.text(x=27.5, y=0.525, s='Non-discriminative line', fontsize=12, color='tab:gray')
ax7.axhline(y=0.5, xmin = 0.05, xmax = 0.95, color='tab:gray', linestyle='--', linewidth=2)
ax7.text(x=27.5, y=0.525, s='Non-discriminative line', fontsize=12, color='tab:gray')
ax8.axhline(y=0.5, xmin = 0.05, xmax = 0.95, color='tab:gray', linestyle='--', linewidth=2)
ax8.text(x=27.5, y=0.525, s='Non-discriminative line', fontsize=12, color='tab:gray')

plt.tight_layout()

plt.savefig('../figures/auc_roc_curves.pdf')
plt.savefig('../figures/auc_roc_curves.png', dpi=600)