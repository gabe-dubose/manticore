#!/usr/bin/env Rscript

# initialize data storage
data <- data.frame(
  tree.size = integer(),
  replicate.pair = integer(),
  metric = character(),
  congruence = numeric(),
  p = numeric()
)

# define tree sizes
tree.sizes <- c(5, 10, 20, 40, 60, 80, 100)

# define metrics
metrics <- c('RF', 'ICRF', 'JRF', 'MCI',
             'SPI', 'NS', 'MSD', 'MSID')

# simulate 1000 pairs of trees for each tree size
for (tree.size in tree.sizes) {
  for (i in 1:1000) {
    print(paste("Working on replicate pair", i, "for tree size of", tree.size, "."))
    # simulate two trees
    tree1 <- ape::write.tree(ape::rtopology(tree.size, rooted=FALSE))
    tree2 <- ape::write.tree(ape::rtopology(tree.size, rooted=FALSE))
  
    # run rtc test for each metric with 1000 iterations
    for (metric in metrics) {
      rtc.result <- manticore::rtc.test(tree1, tree2, metric, 
                                        iterations=1000, verbose=FALSE)
      
      # assemble results
      entry <- data.frame(
        tree.size = tree.size,
        replicate.pair = i,
        metric = metric,
        congruence = rtc.result$observed.congruence,
        p = rtc.result$p
      )
      
      # add to data frame
      data <- rbind(data, entry)
    }
  }
}

write.csv(data, "random_pairs_data.csv")
