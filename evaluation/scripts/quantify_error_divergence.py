#!/usr/bin/env python3

import pandas as pd
from scipy.stats import ks_1samp

# Load data
data = pd.read_csv('../data/random_pairs_data.csv', index_col=0)
data = data.sort_values(by='tree.size', ascending=True)

# Robinson-Foulds
tree_sizes = data.loc[data['metric'] == 'RF']['tree.size'].unique()

for tree_size in tree_sizes:
    print(f"Kolmogorov-Smirnov Test Results for RF with tree of size {tree_size}")
    subset = data[(data['metric'] == 'RF') & (data['tree.size'] == tree_size)]['p']
    
    # perform KS test against uniform CDF
    ks_stat, p_value = ks_1samp(subset, lambda x: x)
    print(f"KS Statistic = {ks_stat:.4f}, p-value = {p_value:.4e}\n")


# Information-corrected Robinson-foulds
for tree_size in tree_sizes:
    print(f"Kolmogorov-Smirnov Test Results for ICRF with tree of size {tree_size}")
    subset = data[(data['metric'] == 'ICRF') & (data['tree.size'] == tree_size)]['p']
    
    # perform KS test against uniform CDF
    ks_stat, p_value = ks_1samp(subset, lambda x: x)
    print(f"KS Statistic = {ks_stat:.4f}, p-value = {p_value:.4e}\n")


# Jaccard Robinson-foulds
for tree_size in tree_sizes:
    print(f"Kolmogorov-Smirnov Test Results for JRF with tree of size {tree_size}")
    subset = data[(data['metric'] == 'JRF') & (data['tree.size'] == tree_size)]['p']

    # perform KS test against uniform CDF
    ks_stat, p_value = ks_1samp(subset, lambda x: x)
    print(f"KS Statistic = {ks_stat:.4f}, p-value = {p_value:.4e}\n")


# Nye similarity
for tree_size in tree_sizes:
    print(f"Kolmogorov-Smirnov Test Results for NS with tree of size {tree_size}")
    subset = data[(data['metric'] == 'NS') & (data['tree.size'] == tree_size)]['p']

    # perform KS test against uniform CDF
    ks_stat, p_value = ks_1samp(subset, lambda x: x)
    print(f"KS Statistic = {ks_stat:.4f}, p-value = {p_value:.4e}\n")


# Mutual Clustering Information
for tree_size in tree_sizes:
    print(f"Kolmogorov-Smirnov Test Results for MCI with tree of size {tree_size}")
    subset = data[(data['metric'] == 'MCI') & (data['tree.size'] == tree_size)]['p']
    
    # perform KS test against uniform CDF
    ks_stat, p_value = ks_1samp(subset, lambda x: x)
    print(f"KS Statistic = {ks_stat:.4f}, p-value = {p_value:.4e}\n")


# Shared Phylogenetic Information
for tree_size in tree_sizes:
    print(f"Kolmogorov-Smirnov Test Results for SPI with tree of size {tree_size}")
    subset = data[(data['metric'] == 'SPI') & (data['tree.size'] == tree_size)]['p']
    
    # perform KS test against uniform CDF
    ks_stat, p_value = ks_1samp(subset, lambda x: x)
    print(f"KS Statistic = {ks_stat:.4f}, p-value = {p_value:.4e}\n")


# Matching Split Distance
for tree_size in tree_sizes:
    print(f"Kolmogorov-Smirnov Test Results for MSD with tree of size {tree_size}")
    subset = data[(data['metric'] == 'MSD') & (data['tree.size'] == tree_size)]['p']
    
    # perform KS test against uniform CDF
    ks_stat, p_value = ks_1samp(subset, lambda x: x)
    print(f"KS Statistic = {ks_stat:.4f}, p-value = {p_value:.4e}\n")


# Matching Split Information Distance
for tree_size in tree_sizes:
    print(f"Kolmogorov-Smirnov Test Results for MSID with tree of size {tree_size}")
    subset = data[(data['metric'] == 'MSID') & (data['tree.size'] == tree_size)]['p']
    
    # perform KS test against uniform CDF
    ks_stat, p_value = ks_1samp(subset, lambda x: x)
    print(f"KS Statistic = {ks_stat:.4f}, p-value = {p_value:.4e}\n")