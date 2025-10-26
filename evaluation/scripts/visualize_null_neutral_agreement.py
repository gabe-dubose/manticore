#!/usr/bin/env python3

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from scipy.optimize import curve_fit

# load data
data = pd.read_csv('../data/neutral_assembly_comparisons.csv', index_col=0)

# define satuating function

def exp_saturating(x, a, b):
    return a * (1 - np.exp(-b * x))

sns.set_style('whitegrid')
fig, [[ax1, ax2, ax3, ax4], [ax5, ax6, ax7, ax8]] = plt.subplots(2, 4, figsize=(12, 5), sharey=True)
axes = [ax1, ax2, ax3, ax4, ax5, ax6, ax7, ax8]
metrics = ["RF", "ICRF", "JRF", "NS", "MCI", "SPI", "MSD", "MSID"]

# iterate through metrics
for ax, metric in zip(axes, metrics):
    subset = data[data['metric'] == metric]
    x = subset["tree.size"].values
    y = subset["norm.diff"].values

    # plot points
    sns.scatterplot(x=x, y=y, ax=ax, s=20, color=sns.color_palette('viridis', 7)[0], edgecolor='none', alpha=0.25)

    # fit saturating function
    p0 = [max(y), 0.1]
    popt, _ = curve_fit(exp_saturating, x, y, p0, maxfev=10000)

    x_fit = np.linspace(min(x), max(x), 200)
    y_fit = exp_saturating(x_fit, *popt)

    ax.plot(x_fit, y_fit, color=sns.color_palette('viridis', 7)[0], lw=2)

    ax.set_title(metric)
    ax.set_ylabel(r'Norm. difference ($D^*$)', fontsize=12)
    ax.tick_params(axis='x', labelsize=12)
    ax.tick_params(axis='y', labelsize=12)
    ax.set_xticks([5, 10, 20, 40, 60, 80, 100])

ax5.set_xlabel(r'$n_{leaves}$', fontsize=12)
ax6.set_xlabel(r'$n_{leaves}$', fontsize=12)
ax7.set_xlabel(r'$n_{leaves}$', fontsize=12)
ax8.set_xlabel(r'$n_{leaves}$', fontsize=12)

plt.tight_layout()
#plt.show()
plt.savefig('../figures/null_neutral_agreement.png', dpi=600)
