#!/usr/bin/env Rscript

# initialize data storage
data <- data.frame(
  tree.size = integer(),
  replicate.pair = integer(),
  metric = character(),
  congruence = numeric(),
  p = numeric(),
  spr.dist = numeric(),
  movements = numeric()
)

# define tree sizes
tree.sizes <- c(5, 10, 20, 40, 60, 80, 100)

# define metrics
metrics <- c('RF', 'ICRF', 'JRF', 'MCI',
             'SPI', 'NS', 'MSD', 'MSID')

# function to define how many movements
divergence.values <- function(tree_size, percents = c(0, 0.1, 0.2, 0.3, 0.4, 0.5)) {
  round(tree_size * percents)
}

# simulate 1000 pairs of trees for each tree size
for (tree.size in tree.sizes) {
  # define divergence values
  divs <- divergence.values(tree.size)
  # iterate through divergence values
  for (div in divs) {
    # conduct 1000 iterations
    for (i in 1:50){
      print(paste("Working on tree.size = ", tree.size, ", moves = ", div, ", iteration = ", i))
      # generate initial tree
      tree1 <- ape::rtopology(tree.size, rooted=FALSE)
      # mutate initial tree if applicable
      if (div == 0){
        tree2 <- tree1
      } else {
        tree2 <- phangorn::rSPR(tree1, moves = div)
      }
    
      # calculate spr distance
      spr.distance <- as.double(phangorn::SPR.dist(tree1, tree2))
      print(spr.distance)
      # redefine as cahracters for testing
      tree1 <- ape::write.tree(tree1)
      tree2 <- ape::write.tree(tree2)
      
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
          p = rtc.result$p,
          spr.dist = spr.distance,
          movements = div
        ) 
        #add data
        data <- rbind(data, entry)
      }
    }
  }
}


write.csv(data, '../data/power_simulation_data.csv')
