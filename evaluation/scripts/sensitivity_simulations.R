#!/usr/bin/env Rscript

# define tree sizes
tree.sizes <- c(20, 60, 100)

# define metrics
metrics <- c('RF', 'ICRF', 'JRF', 'MCI',
             'SPI', 'NS', 'MSD', 'MSID')

# prepare nested list to store results
results <- list()
for (metric in metrics) {
  results[[metric]] <- list()
  for (tree.size in tree.sizes) {
    results[[metric]][[as.character(tree.size)]] <- list()  # now empty list to store simulations
  }
}

set.seed(123)
# iterate through tree sizes
for (tree.size in tree.sizes){
  for (i in 1:20) {
    print(paste("Working on iteration", i, "for tree of size", tree.size))
    # generate trees
    tree1 <- ape::rtopology(tree.size)
    tree2 <- phangorn::rSPR(tree1, moves = tree.size * 0.05)
    tree1 <- ape::write.tree(tree1)
    tree2 <- ape::write.tree(tree2)
    
    for (metric in metrics){
      rtc.results <- manticore::rtc.test(tree1, tree2, metric, 1000, verbose=FALSE)
      sensitivity.check <- manticore::rtc.sensitivity.test(
        reference.tree = tree1,
        comparison.tree = tree2,
        null.congruence.model = rtc.results$null.congruence.model,
        metric = metric,
        iterations = 100
      )
      
      # store simulation run
      results[[metric]][[as.character(tree.size)]][[i]] <- list(
        integrated.p = sensitivity.check$integrated.p,
        prop.div = sensitivity.check$prop.div
      )
    }
  }
}

# save to JSON
jsonlite::write_json(results, "../data/rtc_sensitivity_results.json", auto_unbox = TRUE, pretty = TRUE)
