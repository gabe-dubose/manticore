# Evaluating random tree congruence testing
This directory within the <i>manticore</i> primary directory contains the scripts used and figures generated for methodological evaluations. 

## scripts

```error_simulations.R```: script used for running null simulations (under $H_0$). In summary, random tree congruence tests using a 
variety of congruence metrics are perfomred on random pairs of sampled trees of 5, 10, 20, 40, 60, 80, and 100 leaves. 

```power_simulations.R```: script used to running alternative simulations (under $H_A$). In summary, random tree congruence tests using
a variety of congruence metrics are performed on pairs of trees where one tree is initially a copy of the other but undergoes 
varying degrees subtree pruning and regrafting (to simulate noise). This procedure was conducted across the same tree sizes
described above. 

```visualize_error.py```: script used to calculate and visualize type 1 error rates from $H_0$ simulations conducted using the
<i>error_simulations.R</i> script. 

```visualize_power.py```: script used to calculate and visualize power as a function of noise from $H_A$ simulations conducted 
using the <i>power_simulations.R</i> script.

```visualize_roc_curves.py```: script used to calcualte and visualize receiver operating characteristic (ROC) curves,
as well as the areas under said curves. This relies on both output from $H_0$ and $H_A$ simulations conducted using
the <i>error_simulations.R</i> and <i>power_simulations.R</i> scripts, respectively. 

```visualize_agreement.py```: script used to calculate and visualize the proportion of agreements regarding statistical
support for a phylosymbiotic signal between each pair of congruence metric evaluated. This relies on both output from $H_0$ 
and $H_A$ simulations conducted using the <i>error_simulations.R</i> and <i>power_simulations.R</i> scripts, respectively. 

```neutral_assembly_tree_evaluations.R```: script used to simulate microbial communities that were neutrally assembled with respect to host phylogeny, construct congruence distributions, and compare said distributions to those obtained via uniform tree sampling. 

```sensitivity_simulations.R```: script used to perform sensitivity testing simulations.

```visualize_null_neutral_agreement.py```: script used to visualize agreement between neutral assembly null distributions and random tree null distributions. This script uses output from <i>neutral_assembly_tree_evaluations.R</i>.

```visualize_sensitivity.py```: script used to visualize sensitivity. This script relies on output from <i>`sensitivity_simulations.R</i>.

## figures
```error.pdf```: figure visualizing type 1 error rate from $H_0$ simulations conducted using the the <i>error_simulations.R</i> script.

```power_curves.pdf```: figure visualizing power as a function of noise from $H_A$ simulations conducted using the
<i>power_simulations.R</i> script.

```roc_curves.pdf```: figure visualising the ROC curves calcualted from the $H_0$ and $H_A$ simulations as implemented in the 
<i>error_simulations.R</i> and <i>power_simulations.R</i> scripts, respectively. 

```auc_roc_curves.pdf```: figure visualizing the area under the ROC curves depicted in <i>roc_curves.pdf</i>.

```pct_agreement.pdf```: figure visualizing the proportion of agreements regarding statistical 
support for a phylosymbiotic signal between each pair of congruence metric evaluated.


