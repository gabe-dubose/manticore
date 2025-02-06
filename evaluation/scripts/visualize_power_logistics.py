#!/usr/bin/env python3

import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import scipy.special

sns.set_style('whitegrid')
fig, [[ax1,ax2,ax3,ax4], [ax5,ax6,ax7,ax8]] = plt.subplots(2, 4, figsize=(10,5), sharey=True, sharex=True)

# define colors and line styles
viridis = sns.color_palette("viridis", 7)
lines = ['-', '--', '-.', ':', (0, (3, 1, 1, 1)), (0, (3, 1, 1, 1, 1, 1)), (0, (1, 1))]
tree_sizes = [5,10,20,40,60,80,100]

# define axes limits
ax1.set_ylim(-0.025,1.025)

# Robinson-Foulds

# Tree size = 5: NA/couldn't fit function, too sparse
style = 0
ax1.axhline(y=0, color=viridis[style], linestyle=lines[style], linewidth=3)
# Tree size = 10: NA/couldn't fit function, too sparse
style = 1
ax1.axhline(y=0, color=viridis[style], linestyle=lines[style], linewidth=3)
# Tree size = 20: NA/couldn't fit function, too sparse
style = 2
ax1.axhline(y=0, color=viridis[style], linestyle=lines[style], linewidth=3)
# Tree size = 40: NA/couldn't fit function, too sparse
style = 3
ax1.axhline(y=0, color=viridis[style], linestyle=lines[style], linewidth=3)
# Tree size = 60: NA/couldn't fit function, too sparse
style = 4
ax1.axhline(y=0, color=viridis[style], linestyle=lines[style], linewidth=3)
# Tree size = 80: NA/couldn't fit function, too sparse
style = 5
ax1.axhline(y=0, color=viridis[style], linestyle=lines[style], linewidth=3)
# Tree size = 100: NA/couldn't fit function, too sparse
style = 6
ax1.axhline(y=0, color=viridis[style], linestyle=lines[style], linewidth=3)

ax1.axhline(y=0.8, color='tab:gray', linestyle='-', linewidth=1.5)
ax1.axvline(x=0.8, color='tab:gray', linestyle='-', linewidth=1.5)
ax1.set_title('RF')

ax1.set_ylabel(r'$\hat{P}_{significant}$ ($\alpha=0.05$)', fontsize=12)
ax1.set_xticks([0, 0.25, 0.5, 0.75, 1])
ax1.tick_params(axis='y', labelsize=12)

# Information-Corrected Robinson Foulds
# Tree size = 5: NA/couldn't fit function, too sparse
style = 0
ax2.axhline(y=0, color=viridis[style], linestyle=lines[style], linewidth=3)
# Tree size = 10: NA/couldn't fit function, too sparse
style = 1
ax2.axhline(y=0, color=viridis[style], linestyle=lines[style], linewidth=3)
# Tree size = 20
intercept, slope, style = -9.8933, 11.0120, 2
ax2.plot(np.linspace(0, 1, 100), scipy.special.expit(intercept + slope * np.linspace(0, 1, 100)), 
         color=viridis[style], linewidth=3, linestyle=lines[style])
#Tree size = 40
intercept, slope, style = -11.1307, 17.1234, 3
ax2.plot(np.linspace(0, 1, 100), scipy.special.expit(intercept + slope * np.linspace(0, 1, 100)), 
         color=viridis[style], linewidth=3, linestyle=lines[style])
#Tree size = 60
intercept, slope, style = -9.0681, 11.3525, 4
ax2.plot(np.linspace(0, 1, 100), scipy.special.expit(intercept + slope * np.linspace(0, 1, 100)), 
         color=viridis[style], linewidth=3, linestyle=lines[style])
#Tree size = 80
intercept, slope, style = -10.2190, 12.0841, 5
ax2.plot(np.linspace(0, 1, 100), scipy.special.expit(intercept + slope * np.linspace(0, 1, 100)), 
         color=viridis[style], linewidth=3, linestyle=lines[style])
#Tree size = 100
intercept, slope, style = -9.2381, 10.3768, 6
ax2.plot(np.linspace(0, 1, 100), scipy.special.expit(intercept + slope * np.linspace(0, 1, 100)), 
         color=viridis[style], linewidth=3, linestyle=lines[style])

ax2.axhline(y=0.8, color='tab:gray', linestyle='-', linewidth=1.5)
ax2.axvline(x=0.8, color='tab:gray', linestyle='-', linewidth=1.5)
ax2.set_title('ICRF')


# Jaccard Robinson-Foulds
# Tree size = 5: NA/couldn't fit function, too sparse
style = 0
ax3.axhline(y=0, color=viridis[style], linestyle=lines[style], linewidth=3)
# Tree size = 10
intercept, slope, style = -102.7691, 111.5063, 1
ax3.plot(np.linspace(0, 1, 100), scipy.special.expit(intercept + slope * np.linspace(0, 1, 100)), 
         color=viridis[style], linewidth=3, linestyle=lines[style])
# Tree size = 20
intercept, slope, style = -84.8484, 94.0039, 2
ax3.plot(np.linspace(0, 1, 100), scipy.special.expit(intercept + slope * np.linspace(0, 1, 100)), 
         color=viridis[style], linewidth=3, linestyle=lines[style])
#Tree size = 40
intercept, slope, style = -44.2672, 50.1590, 3
ax3.plot(np.linspace(0, 1, 100), scipy.special.expit(intercept + slope * np.linspace(0, 1, 100)), 
         color=viridis[style], linewidth=3, linestyle=lines[style])
#Tree size = 60
intercept, slope, style = -33.6336, 41.7099, 4
ax3.plot(np.linspace(0, 1, 100), scipy.special.expit(intercept + slope * np.linspace(0, 1, 100)), 
         color=viridis[style], linewidth=3, linestyle=lines[style])
#Tree size = 80
intercept, slope, style = -23.4646, 26.7147, 5
ax3.plot(np.linspace(0, 1, 100), scipy.special.expit(intercept + slope * np.linspace(0, 1, 100)), 
         color=viridis[style], linewidth=3, linestyle=lines[style])
#Tree size = 100
intercept, slope, style = -24.0605, 30.7602, 6
ax3.plot(np.linspace(0, 1, 100), scipy.special.expit(intercept + slope * np.linspace(0, 1, 100)), 
         color=viridis[style], linewidth=3, linestyle=lines[style])

ax3.axhline(y=0.8, color='tab:gray', linestyle='-', linewidth=1.5)
ax3.axvline(x=0.8, color='tab:gray', linestyle='-', linewidth=1.5)
ax3.set_title('JRF')


# Nye Similarity
# Tree size = 5
intercept, slope, style = -32.1354, 28.4341, 0
ax4.plot(np.linspace(0, 1, 100), scipy.special.expit(intercept + slope * np.linspace(0, 1, 100)), 
         color=viridis[style], linewidth=3, linestyle=lines[style])
# Tree size = 10
intercept, slope, style = -48.3070, 87.0383, 1
ax4.plot(np.linspace(0, 1, 100), scipy.special.expit(intercept + slope * np.linspace(0, 1, 100)), 
         color=viridis[style], linewidth=3, linestyle=lines[style])
# Tree size = 20
intercept, slope, style = -48.1304, 84.1187, 2
ax4.plot(np.linspace(0, 1, 100), scipy.special.expit(intercept + slope * np.linspace(0, 1, 100)), 
         color=viridis[style], linewidth=3, linestyle=lines[style])
#Tree size = 40
intercept, slope, style = -33.0505, 57.6112, 3
ax4.plot(np.linspace(0, 1, 100), scipy.special.expit(intercept + slope * np.linspace(0, 1, 100)), 
         color=viridis[style], linewidth=3, linestyle=lines[style])
#Tree size = 60
intercept, slope, style = -23.0839, 34.0898, 4
ax4.plot(np.linspace(0, 1, 100), scipy.special.expit(intercept + slope * np.linspace(0, 1, 100)), 
         color=viridis[style], linewidth=3, linestyle=lines[style])
#Tree size = 80
intercept, slope, style = -17.2369, 25.4592, 5
ax4.plot(np.linspace(0, 1, 100), scipy.special.expit(intercept + slope * np.linspace(0, 1, 100)), 
         color=viridis[style], linewidth=3, linestyle=lines[style])
#Tree size = 100
intercept, slope, style = -20.6019, 27.0331, 6
ax4.plot(np.linspace(0, 1, 100), scipy.special.expit(intercept + slope * np.linspace(0, 1, 100)), 
         color=viridis[style], linewidth=3, linestyle=lines[style])

ax4.axhline(y=0.8, color='tab:gray', linestyle='-', linewidth=1.5)
ax4.axvline(x=0.8, color='tab:gray', linestyle='-', linewidth=1.5)
ax4.set_title('NS')


# Mutual Clustering Information
# Tree size = 5: NA/couldn't fit function, too sparse
style = 0
ax5.axhline(y=0, color=viridis[style], linestyle=lines[style], linewidth=3)
# Tree size = 10
intercept, slope, style = -57.9179, 108.8080, 1
ax5.plot(np.linspace(0, 1, 100), scipy.special.expit(intercept + slope * np.linspace(0, 1, 100)), 
         color=viridis[style], linewidth=3, linestyle=lines[style])
# Tree size = 20
intercept, slope, style = -63.8108, 116.8081, 2
ax5.plot(np.linspace(0, 1, 100), scipy.special.expit(intercept + slope * np.linspace(0, 1, 100)), 
         color=viridis[style], linewidth=3, linestyle=lines[style])
#Tree size = 40
intercept, slope, style = -51.2984, 72.8831, 3
ax5.plot(np.linspace(0, 1, 100), scipy.special.expit(intercept + slope * np.linspace(0, 1, 100)), 
         color=viridis[style], linewidth=3, linestyle=lines[style])
#Tree size = 60
intercept, slope, style = -80.8385, 131.9994, 4
ax5.plot(np.linspace(0, 1, 100), scipy.special.expit(intercept + slope * np.linspace(0, 1, 100)), 
         color=viridis[style], linewidth=3, linestyle=lines[style])
#Tree size = 80
intercept, slope, style = -57.4355, 83.1211, 5
ax5.plot(np.linspace(0, 1, 100), scipy.special.expit(intercept + slope * np.linspace(0, 1, 100)), 
         color=viridis[style], linewidth=3, linestyle=lines[style])
#Tree size = 100
intercept, slope, style = -52.8209, 80.1754, 6
ax5.plot(np.linspace(0, 1, 100), scipy.special.expit(intercept + slope * np.linspace(0, 1, 100)), 
         color=viridis[style], linewidth=3, linestyle=lines[style])

ax5.axhline(y=0.8, color='tab:gray', linestyle='-', linewidth=1.5)
ax5.axvline(x=0.8, color='tab:gray', linestyle='-', linewidth=1.5)
ax5.set_title('MCI')
ax5.set_ylabel(r'$\hat{P}_{significant}$ ($\alpha=0.05$)', fontsize=12)
ax5.set_xlabel('Scaled Congruence', fontsize=12)
ax5.tick_params(axis='y', labelsize=12)
ax5.tick_params(axis='x', labelsize=12)

# Shared Phylogenetic Information
# Tree size = 5
intercept, slope, style = -43.3586, 38.9518, 0
ax6.plot(np.linspace(0, 1, 100), scipy.special.expit(intercept + slope * np.linspace(0, 1, 100)), 
         color=viridis[style], linewidth=3, linestyle=lines[style])
# Tree size = 10
intercept, slope, style = -49.0206, 89.8005, 1
ax6.plot(np.linspace(0, 1, 100), scipy.special.expit(intercept + slope * np.linspace(0, 1, 100)), 
         color=viridis[style], linewidth=3, linestyle=lines[style])
# Tree size = 20
intercept, slope, style = -62.9976, 136.3855, 2
ax6.plot(np.linspace(0, 1, 100), scipy.special.expit(intercept + slope * np.linspace(0, 1, 100)), 
         color=viridis[style], linewidth=3, linestyle=lines[style])
#Tree size = 40
intercept, slope, style = -63.0061, 99.8518, 3
ax6.plot(np.linspace(0, 1, 100), scipy.special.expit(intercept + slope * np.linspace(0, 1, 100)), 
         color=viridis[style], linewidth=3, linestyle=lines[style])
#Tree size = 60
intercept, slope, style = -42.7417, 77.6178, 4
ax6.plot(np.linspace(0, 1, 100), scipy.special.expit(intercept + slope * np.linspace(0, 1, 100)), 
         color=viridis[style], linewidth=3, linestyle=lines[style])
#Tree size = 80
intercept, slope, style = -47.9057, 67.8887, 5
ax6.plot(np.linspace(0, 1, 100), scipy.special.expit(intercept + slope * np.linspace(0, 1, 100)), 
         color=viridis[style], linewidth=3, linestyle=lines[style])
#Tree size = 100
intercept, slope, style = -28.4679, 45.5794, 6
ax6.plot(np.linspace(0, 1, 100), scipy.special.expit(intercept + slope * np.linspace(0, 1, 100)), 
         color=viridis[style], linewidth=3, linestyle=lines[style])

ax6.axhline(y=0.8, color='tab:gray', linestyle='-', linewidth=1.5)
ax6.axvline(x=0.8, color='tab:gray', linestyle='-', linewidth=1.5)
ax6.set_title('SPI')
ax6.set_xlabel('Scaled Congruence', fontsize=12)
ax6.tick_params(axis='x', labelsize=12)

# Matching Split Distance
# Tree size = 5: NA/couldn't fit function, too sparse
style = 0
ax7.axhline(y=0, color=viridis[style], linestyle=lines[style], linewidth=3)
# Tree size = 10
intercept, slope, style = -36.1453, 41.8630, 1
ax7.plot(np.linspace(0, 1, 100), scipy.special.expit(intercept + slope * np.linspace(0, 1, 100)), 
         color=viridis[style], linewidth=3, linestyle=lines[style])
# Tree size = 20
intercept, slope, style = -16.5307, 22.2469, 2
ax7.plot(np.linspace(0, 1, 100), scipy.special.expit(intercept + slope * np.linspace(0, 1, 100)), 
         color=viridis[style], linewidth=3, linestyle=lines[style])
#Tree size = 40
intercept, slope, style = -13.1179, 17.6936, 3
ax7.plot(np.linspace(0, 1, 100), scipy.special.expit(intercept + slope * np.linspace(0, 1, 100)), 
         color=viridis[style], linewidth=3, linestyle=lines[style])
#Tree size = 60
intercept, slope, style = -11.1956, 13.8335, 4
ax7.plot(np.linspace(0, 1, 100), scipy.special.expit(intercept + slope * np.linspace(0, 1, 100)), 
         color=viridis[style], linewidth=3, linestyle=lines[style])
#Tree size = 80
intercept, slope, style = -9.7185, 11.7608, 5
ax7.plot(np.linspace(0, 1, 100), scipy.special.expit(intercept + slope * np.linspace(0, 1, 100)), 
         color=viridis[style], linewidth=3, linestyle=lines[style])
#Tree size = 100
intercept, slope, style = -10.6702, 12.9323, 6
ax7.plot(np.linspace(0, 1, 100), scipy.special.expit(intercept + slope * np.linspace(0, 1, 100)), 
         color=viridis[style], linewidth=3, linestyle=lines[style])

ax7.axhline(y=0.8, color='tab:gray', linestyle='-', linewidth=1.5)
ax7.axvline(x=0.8, color='tab:gray', linestyle='-', linewidth=1.5)
ax7.set_title('MSD')
ax7.set_xlabel('Scaled Congruence', fontsize=12)
ax7.tick_params(axis='x', labelsize=12)

# Matching Split Information Distance
# Tree size = 5: NA/couldn't fit function, too sparse
style = 0
ax8.axhline(y=0, color=viridis[style], linestyle=lines[style], linewidth=3)
# Tree size = 10
intercept, slope, style = -43.4658, 55.1396, 1
ax8.plot(np.linspace(0, 1, 100), scipy.special.expit(intercept + slope * np.linspace(0, 1, 100)), 
         color=viridis[style], linewidth=3, linestyle=lines[style])
# Tree size = 20
intercept, slope, style = -24.1900, 27.6694, 2
ax8.plot(np.linspace(0, 1, 100), scipy.special.expit(intercept + slope * np.linspace(0, 1, 100)), 
         color=viridis[style], linewidth=3, linestyle=lines[style])
#Tree size = 40
intercept, slope, style = -16.9594, 24.4382, 3
ax8.plot(np.linspace(0, 1, 100), scipy.special.expit(intercept + slope * np.linspace(0, 1, 100)), 
         color=viridis[style], linewidth=3, linestyle=lines[style])
#Tree size = 60
intercept, slope, style = -10.3124, 12.9644, 4
ax8.plot(np.linspace(0, 1, 100), scipy.special.expit(intercept + slope * np.linspace(0, 1, 100)), 
         color=viridis[style], linewidth=3, linestyle=lines[style])
#Tree size = 80
intercept, slope, style = -12.9686, 17.3113, 5
ax8.plot(np.linspace(0, 1, 100), scipy.special.expit(intercept + slope * np.linspace(0, 1, 100)), 
         color=viridis[style], linewidth=3, linestyle=lines[style])
#Tree size = 100
intercept, slope, style = -10.5698, 11.8186, 6
ax8.plot(np.linspace(0, 1, 100), scipy.special.expit(intercept + slope * np.linspace(0, 1, 100)), 
         color=viridis[style], linewidth=3, linestyle=lines[style])

ax8.axhline(y=0.8, color='tab:gray', linestyle='-', linewidth=1.5)
ax8.axvline(x=0.8, color='tab:gray', linestyle='-', linewidth=1.5)
ax8.set_title('MSID')
ax8.set_xlabel('Scaled Congruence', fontsize=12)
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

# plot legend
legend_handles = [
    Line2D([0], [0], color=viridis[i], linestyle=lines[i], linewidth=3, label=f"{tree_sizes[i]}")
    for i in range(len(tree_sizes))
]
ax4.legend(handles=legend_handles, bbox_to_anchor=(1.05, 1.04), loc='upper left', title='n Leaves',
           fontsize=12, title_fontsize=12)

plt.tight_layout()
plt.savefig('../figures/power_logistics.pdf')
plt.savefig('../figures/power_logistics.png', dpi=600)