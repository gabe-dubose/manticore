#!/usr/bin/env python3

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# load data
data = pd.read_csv('../data/random_pairs_data.csv', index_col=0)
data = data.sort_values(by='tree.size', ascending=True)

sns.set_style('whitegrid')
fig, [[ax1,ax2,ax3,ax4], [ax5,ax6,ax7,ax8]] = plt.subplots(2, 4, figsize=(10,5), sharey=True, sharex=True)

# Robinson-foulds
line_styles = ['-', '--', '-.', ':']
tree_sizes = data.loc[data['metric'] == 'RF']['tree.size'].unique()
line_style_map = {size: line_styles[i % len(line_styles)] for i, size in enumerate(tree_sizes)}

# Plot with different line styles
for tree_size in tree_sizes:
    subset = data[(data['metric'] == 'RF') & (data['tree.size'] == tree_size)]
    sns.ecdfplot(
        data=subset,
        x='p',
        ax=ax1,
        label=f"{tree_size}",
        linewidth=3,
        alpha=0.8,
        color=sns.color_palette('viridis', len(tree_sizes))[list(tree_sizes).index(tree_size)],
        linestyle=line_style_map[tree_size]
    )

# add theoretical expectation
ax1.plot([0, 1], [0, 1], linestyle='--', color='black', linewidth=3)
ax1.set_title('RF')
ax1.set_xlabel('')
ax1.set_ylabel('Cumulative Proportion', fontsize=12)
ax1.tick_params(axis='y', labelsize=12)

# Information-corrected Robinson-foulds
line_styles = ['-', '--', '-.', ':']
tree_sizes = data.loc[data['metric'] == 'ICRF']['tree.size'].unique()
line_style_map = {size: line_styles[i % len(line_styles)] for i, size in enumerate(tree_sizes)}

# Plot with different line styles
for tree_size in tree_sizes:
    subset = data[(data['metric'] == 'ICRF') & (data['tree.size'] == tree_size)]
    sns.ecdfplot(
        data=subset,
        x='p',
        ax=ax2,
        linewidth=3,
        alpha=0.8,
        label=f"{tree_size}",
        color=sns.color_palette('viridis', len(tree_sizes))[list(tree_sizes).index(tree_size)],
        linestyle=line_style_map[tree_size]
    )

# ad theoretical expectation
ax2.plot([0, 1], [0, 1], linestyle='--', color='black', linewidth=3)
ax2.set_title('ICRF')
ax2.set_xlabel('')

# Jaccard Robinson-foulds
line_styles = ['-', '--', '-.', ':']
tree_sizes = data.loc[data['metric'] == 'JRF']['tree.size'].unique()
line_style_map = {size: line_styles[i % len(line_styles)] for i, size in enumerate(tree_sizes)}

# Plot with different line styles
for tree_size in tree_sizes:
    subset = data[(data['metric'] == 'JRF') & (data['tree.size'] == tree_size)]
    sns.ecdfplot(
        data=subset,
        x='p',
        ax=ax3,
        linewidth=3,
        alpha=0.8,
        label=f"{tree_size}",
        color=sns.color_palette('viridis', len(tree_sizes))[list(tree_sizes).index(tree_size)],
        linestyle=line_style_map[tree_size]
    )

# ad theoretical expectation
ax3.plot([0, 1], [0, 1], linestyle='--', color='black', linewidth=3)
ax3.set_title('JRF')
ax3.set_xlabel('')

# Nye similarity
line_styles = ['-', '--', '-.', ':']
tree_sizes = data.loc[data['metric'] == 'NS']['tree.size'].unique()
line_style_map = {size: line_styles[i % len(line_styles)] for i, size in enumerate(tree_sizes)}

# Plot with different line styles
for tree_size in tree_sizes:
    subset = data[(data['metric'] == 'NS') & (data['tree.size'] == tree_size)]
    sns.ecdfplot(
        data=subset,
        x='p',
        ax=ax4,
        linewidth=3,
        alpha=0.8,
        label=f"{tree_size}",
        color=sns.color_palette('viridis', len(tree_sizes))[list(tree_sizes).index(tree_size)],
        linestyle=line_style_map[tree_size]
    )

# add theoretical expectation
ax4.plot([0, 1], [0, 1], linestyle='--', color='black', linewidth=3, label="\nExpected:\n$F(P) = P$")
ax4.set_title('NS')
ax4.set_xlabel('')

# Add legend
ax4.legend(
    bbox_to_anchor=(1.05, 1.05),
    loc='upper left',
    title='n Leaves',
    fontsize=12, title_fontsize=12
)


# Mutual Clustering Information
line_styles = ['-', '--', '-.', ':']
tree_sizes = data.loc[data['metric'] == 'MCI']['tree.size'].unique()
line_style_map = {size: line_styles[i % len(line_styles)] for i, size in enumerate(tree_sizes)}

# Plot with different line styles
for tree_size in tree_sizes:
    subset = data[(data['metric'] == 'MCI') & (data['tree.size'] == tree_size)]
    sns.ecdfplot(
        data=subset,
        x='p',
        ax=ax5,
        linewidth=3,
        alpha=0.8,
        label=f"{tree_size}",
        color=sns.color_palette('viridis', len(tree_sizes))[list(tree_sizes).index(tree_size)],
        linestyle=line_style_map[tree_size]
    )

# ad theoretical expectation
ax5.plot([0, 1], [0, 1], linestyle='--', color='black', linewidth=3)
ax5.set_title('MCI')
ax5.set_xlabel(r'$P(Null \geq Observed)$', fontsize=12)
ax5.set_xticks([0.0, 0.2, 0.4, 0.6, 0.8, 1.0])
ax5.set_ylabel('Cumulative Proportion', fontsize=12)
ax5.tick_params(axis='y', labelsize=12)
ax5.tick_params(axis='x', labelsize=12)

# Shared Phylogenetic Information
line_styles = ['-', '--', '-.', ':']
tree_sizes = data.loc[data['metric'] == 'SPI']['tree.size'].unique()
line_style_map = {size: line_styles[i % len(line_styles)] for i, size in enumerate(tree_sizes)}

# Plot with different line styles
for tree_size in tree_sizes:
    subset = data[(data['metric'] == 'SPI') & (data['tree.size'] == tree_size)]
    sns.ecdfplot(
        data=subset,
        x='p',
        ax=ax6,
        linewidth=3,
        alpha=0.8,
        label=f"{tree_size}",
        color=sns.color_palette('viridis', len(tree_sizes))[list(tree_sizes).index(tree_size)],
        linestyle=line_style_map[tree_size]
    )

# ad theoretical expectation
ax6.plot([0, 1], [0, 1], linestyle='--', color='black', linewidth=3)
ax6.set_title('SPI')
ax6.set_xlabel(r'$P(Null \geq Observed)$', fontsize=12)
ax6.tick_params(axis='x', labelsize=12)

# Matching Split Distance
line_styles = ['-', '--', '-.', ':']
tree_sizes = data.loc[data['metric'] == 'MSD']['tree.size'].unique()
line_style_map = {size: line_styles[i % len(line_styles)] for i, size in enumerate(tree_sizes)}

# Plot with different line styles
for tree_size in tree_sizes:
    subset = data[(data['metric'] == 'MSD') & (data['tree.size'] == tree_size)]
    sns.ecdfplot(
        data=subset,
        x='p',
        ax=ax7,
        linewidth=3,
        alpha=0.8,
        label=f"{tree_size}",
        color=sns.color_palette('viridis', len(tree_sizes))[list(tree_sizes).index(tree_size)],
        linestyle=line_style_map[tree_size]
    )

# ad theoretical expectation
ax7.plot([0, 1], [0, 1], linestyle='--', color='black', linewidth=3)
ax7.set_title('MSD')
ax7.set_xlabel(r'$P(Null \geq Observed)$', fontsize=12)
ax7.tick_params(axis='x', labelsize=12)

# Matching Split Information Distance
line_styles = ['-', '--', '-.', ':']
tree_sizes = data.loc[data['metric'] == 'MSID']['tree.size'].unique()
line_style_map = {size: line_styles[i % len(line_styles)] for i, size in enumerate(tree_sizes)}

# Plot with different line styles
for tree_size in tree_sizes:
    subset = data[(data['metric'] == 'MSID') & (data['tree.size'] == tree_size)]
    sns.ecdfplot(
        data=subset,
        x='p',
        ax=ax8,
        linewidth=3,
        alpha=0.8,
        label=f"{tree_size}",
        color=sns.color_palette('viridis', len(tree_sizes))[list(tree_sizes).index(tree_size)],
        linestyle=line_style_map[tree_size]
    )

# ad theoretical expectation
ax8.plot([0, 1], [0, 1], linestyle='--', color='black', linewidth=3)
ax8.set_title('MSID')
ax8.set_xlabel(r'$P(Null \geq Observed)$', fontsize=12)
ax8.tick_params(axis='x', labelsize=12)

# add subplot labels
ax1.text(0,0.9, 'A', fontsize=15)
ax2.text(0,0.9, 'B', fontsize=15)
ax3.text(0,0.9, 'C', fontsize=15)
ax4.text(0,0.9, 'D', fontsize=15)
ax5.text(0,0.9, 'E', fontsize=15)
ax6.text(0,0.9, 'F', fontsize=15)
ax7.text(0,0.9, 'G', fontsize=15)
ax8.text(0,0.9, 'H', fontsize=15)

plt.tight_layout()
plt.subplots_adjust(hspace=0.2)
plt.savefig('../figures/error_ecdfs.png', dpi=600)
plt.savefig('../figures/error_ecdfs.pdf')
