#!/usr/bin/env Rscript

# initialize data storage
data <- data.frame(
  tree.size = integer(),
  replicate = integer(),
  iterations = integer(),
  metric = character(),
  p = numeric()
)

# define tree sizes
tree.sizes <- c(5, 10, 20, 40, 60, 80, 100)

# define iterations
iterations <- c(10^1, 10^2, 10^3, 10^4)

# define metrics
metrics <- c('RF', 'ICRF', 'JRF', 'MCI',
             'SPI', 'NS', 'MSD', 'MSID')

# iterate through tree sizes
for (tree.size in tree.sizes) {
  
  # repeat procedure 10 times for each tree size
  for (i in 1:10) {
    print(paste("Working on iteration", i, "for tree size", tree.size, "..."))
    
    # simulate two trees
    tree1 <- ape::write.tree(ape::rtopology(tree.size, rooted=FALSE))
    tree2 <- ape::write.tree(ape::rtopology(tree.size, rooted=FALSE))
  
    # run rtc test 10 times
    # for each metric and for each iterations
    for (j in 1:10) {
      for (metric in metrics) {
        for (iteration in iterations) {
          rtc.result <- manticore::rtc.test(tree1, tree2, metric, iteration)
        
          # assemble results
          entry <- data.frame(
            tree.size = tree.size,
            replicate.pair = i,
            replicate.run = j,
            iterations = iteration,
            metric = metric,
            p = rtc.result$p
          )
        
          # add to data frame
          data <- rbind(data, entry)
        }
      }
    }
  }
}

write.csv(data, "p_var_data.csv")
