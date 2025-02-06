# MANTICORE: Monte cArlo simulaioN algoriThm for assessIng tree COngRuencE
Manticore is an R library for implementing a Monte Carlo simulation approach for assessing the topological congruence between
phylogenetic trees. The general idea behind this approach is pretty simple. To statistically evaluate the congruence between two trees,
you can generate a null congruence distirbution by repeatedly simulating random trees and quantifyign how congruent they are 
with you tree of interest. You can then ask the question: <i>how often is the congruence between my tree of interest and random trees
greater than or equal to the congruence observed between my actual trees?</i> The answer to this question lies in the <i>P(Null $\geq$ Obseved)</i> 
value, which can help statistically contextualize the actual congruence value. For convention, I generally refer to this procedure as
a random tree congruence (rtc) test.

## Installation
#### From GitHub repository (most recent)
```r
devtools::install_github("gabe-dubose/manticore")
```

## Example
To conduct random tree congruence test, you first need to load your trees. The <i>rtc.test()</i> function can take file paths (as strings) or
trees in Newick format (also as strings). For the purposes of this example, I'll use the <i>get.tree()</i> function built into the 
<i>manticore</i> library, which just stores some trees as string in Newick format for examples and testing:

```r
# load manticore library
library(manticore)

# get trees
tree1 <- get.tree(1)
tree2 <- get.tree(2)
```

Printing the trees just shows that they are indeed strings in Newick format.
```r
> print(tree1)
[1] "(E:0.6030125057,(F:0.9897625113,(((G:0.9443907421,I:0.5512045701):0.178062907,(D:0.5385736986,(H:0.8108982465,B:0.6424617139):0.7985284778):0.05077014188):0.7699153256,C:0.257833373):0.9529942176):0.598905632,(A:0.08370447881,J:0.3042376931):0.4075395141);"
> print(tree2)
[1] "(E:0.8807457979,J:0.2588515345,(A:0.5110714179,((F:0.7630252142,(D:0.4388972835,((B:0.7929537457,(C:0.1264250765,H:0.6562405329):0.09945738246):0.221811289,G:0.3562049884):0.977532794):0.02143185376):0.4469005479,I:0.4462291533):0.7385474753):0.245398188);"
```

Now that the trees are loaded, we can run the <i>rtc.test()</i> function. For this example, I'll go with mutual clustering information (MCI) as congruence metric.
```r
rtc.results <- rtc.test(tree1, tree2, 'MCI', 1000, verbose=FALSE)
```

The <i>rtc.test()</i> function returns a list object with the value names <i>observed.congruence</i>, <i>p</i>, and <i>null.congruence.model</i>, which can be accessed with the <i>$</i> 
operator. For example, we can view the results:

```r
> print(paste("Congruence =", rtc.results$observed.congruence))
> print(paste("P(Null >= Observed) =", rtc.results$p))
```

which shows: 
```
[1] "Congruence = 2.77480542779449"
[1] "P(Null >= Observed) = 0.013"
```

We can also visualize the results along with the null model:
```r
hist(rtc.results$null.congruence.model,
     main=paste("P(Null >= Observed) =", rtc.results$p), 
     xlab='Congruence',
     freq = FALSE)
abline(v=rtc.results$observed.congruence,
       col='red', lty=2, lwd=2)
```


## Manual

### rtc.test()
<b>Description</b>:

Perform a random tree congruence test. This function uses Monte Carlo simulations to generate a null congruence distribution and then evaluates the proportion of null comparisons that showed congruence that was greater than or equal to that of the observed congruence.
The primary function offered by <i>manticore</i> is <i>rtc.test</i>, which conducts the previously describe random tree congruence test.

<b>Function usage</b>:
```r
rtc.test(
  reference.tree,
  comparison.tree,
  congruence.metric,
  iterations,
  verbose = FALSE
)

```

<b>Arguments</b>:
```
reference.tree  Path to reference tree file, or string in Newick format

comparison.tree  Path to comparison tree file, or string in Newick format

congruence.metric  Metric used to evaluate congruence. Options include:

    MCI: Mutual Clustering Information (Smith, 2020a)
    SPI: Shared Phylogenetic Information (Smith, 2020a)
    NS: Nye Similarity (Nye et al, 2006)
    JRF: Jaccard-Robinson-Foulds (Böcker et al, 2013)
    MSD: Matching Split Distance (Bogdanowicz and Giaro, 2012)
    MSID: Matching Split Information Distance (Smith, 2020a)
    RF: Robinson-Foulds (Robinson and Foulds, 1981)
    ICRF: Information-Corrected Robinson Foulds (Smith, 2020a)

iterations  The number of randomly simulated trees used to construct null distribution

verbose  Display run updates (TRUE of FALSE)
```

<b>Value</b>:

Function returns the random tree congruence test results. This is a list object that contains:

```
observed.congruence  The observed congruence between the reference and comparison trees (based on specified congruence metric)

p  The proportion of values in the null distribution that are greater than or equal to the observed congruence

null.congruence.model  A vector containing the null congruence values
```


<b>Details</b>:

The random tree congruence test can be used with a variety of congruence metrics that vary in what aspects of congruence they consider. The congruence metrics offered are all implemented by the TreeDist library (Smith 2020b). The random tree simulations are implemented by the ape library (Paradis and Schliep 2019). Any use of this library should include reference to these libraries as well (see References section). Furthermore, the specific congruence metric(s) used should also be referenced (see above list).

<b>References</b>:

Böcker S., Canzar S., Klau G.W. (2013) The Generalized Robinson-Foulds Metric. In Algorithms in Bioinformatics (eds A Darling, J Stoye), pp. 156–169. Berlin, Heidelberg: Springer Berlin Heidelberg.

Bogdanowicz D., Giaro K. (2012) Matching Split Distance for Unrooted Binary Phylogenetic Trees. IEEE/ACM Trans. Comput. Biol. and Bioinf. doi:10.1109/TCBB.2011.48

Nye T.M.W., Liò P., Gilks W.R. (2006) A novel algorithm and web-based tool for comparing two alternative phylogenetic trees. Bioinformatics. doi:10.1093/bioinformatics/bti720

Paraids E., Schliep K. (2019) ape 5.0: an environment for modern phylogenetics and evolutionary analyses in R. Bioinformatics. doi:10.1093/bioinformatics/bty633

Robinson D.F., Foulds L.R. (1981) Comparison of phylogenetic trees. Mathematical Biosciences. doi:10.1016/0025-5564(81)90043-2

Smith MR. (2020a) Information theoretic generalized Robinson–Foulds metrics for comparing phylogenetic trees. Bioinformatics. doi:10.1093/bioinformatics/btaa614

Smith M.R. (2020b) TreeDist: distances between phylogenetic trees. Comprehensive R Archive Network. doi: 10.5281/zenodo.3528123.

### get.tree()

<b>Description</b>:

Retrieve trees for testing and examples.

<b>Function usage</b>:
```r
get.tree(tree)

```

<b>Arguments</b>:
```
tree  Number corresponding to which tree to retrieve (1 or 2)
```

<b>Value</b>:

Function returns a phylogenetic tree in Newick format as a string object.
