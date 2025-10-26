#!/usr/bin/env Rscript

# function to neutrally assemble host microbial communities
simulate.neutral.assembly.tree <- function(n.hosts, n.microbial.taxa, community.size){
  # initialize matrix for storing data
  microbial.community.matrix <- matrix(0, nrow = n.hosts, ncol = n.microbial.taxa)
  # name rows and columns
  rownames(microbial.community.matrix) <- paste0("t", 1:n.hosts)
  colnames(microbial.community.matrix) <- paste0("m", 1:n.microbial.taxa)
  
  # iterate through each host
  for (host in 1:n.hosts){
    # assembly microbal communities
    microbial.community <- sample(1:n.microbial.taxa, community.size, replace = TRUE)
    # add counts to matrix
    counts <- table(microbial.community)
    microbial.community.matrix[host, as.numeric(names(counts))] <- counts
  }
  # compute dissimilarity matrix
  dissimilarity.matrix <- vegan::vegdist(microbial.community.matrix, method = "bray")
  # compute dendrogram
  dendrogram <- hclust(dissimilarity.matrix, method = "average")
  return(dendrogram)
}

# function to generate neutral assembly null model
neutral.assembly.model <- function(host.tree, n.microbial.taxa, community.size, congruence.metric, iterations){
  # initialize vector to store null model
  null.model <- c()
  
  # read host tree and define number of hosts
  host.tree <- ape::read.tree(text=host.tree)
  n.hosts <- length(host.tree$tip.label)
  
  # generate null model
  # RF
  if (congruence.metric == 'RF'){
    for (i in 1:iterations){
      # generate neutral assembly tree
      neutral.tree <- ape::as.phylo(simulate.neutral.assembly.tree(n.hosts, n.microbial.taxa, community.size))
      # evaluate congruence
      congruence.value <- TreeDist::RobinsonFoulds(host.tree, neutral.tree)
      null.model <- c(null.model, congruence.value)
    }
  }
  
  # ICRF
  if (congruence.metric == 'ICRF'){
    for (i in 1:iterations){
      # generate neutral assembly tree
      neutral.tree <- ape::as.phylo(simulate.neutral.assembly.tree(n.hosts, n.microbial.taxa, community.size))
      # evaluate congruence
      congruence.value <- TreeDist::InfoRobinsonFoulds(host.tree, neutral.tree)
      null.model <- c(null.model, congruence.value)
    }
  }
  
  # JRF
  if (congruence.metric == 'JRF'){
    for (i in 1:iterations){
      # generate neutral assembly tree
      neutral.tree <- ape::as.phylo(simulate.neutral.assembly.tree(n.hosts, n.microbial.taxa, community.size))
      # evaluate congruence
      congruence.value <- TreeDist::JaccardRobinsonFoulds(host.tree, neutral.tree)
      null.model <- c(null.model, congruence.value)
    }
  }
  
  # MSD
  if (congruence.metric == 'MSD'){
    for (i in 1:iterations){
      # generate neutral assembly tree
      neutral.tree <- ape::as.phylo(simulate.neutral.assembly.tree(n.hosts, n.microbial.taxa, community.size))
      # evaluate congruence
      congruence.value <- TreeDist::MatchingSplitDistance(host.tree, neutral.tree)
      null.model <- c(null.model, congruence.value)
    }
  }
  
  # MSID
  if (congruence.metric == 'MSID'){
    for (i in 1:iterations){
      # generate neutral assembly tree
      neutral.tree <- ape::as.phylo(simulate.neutral.assembly.tree(n.hosts, n.microbial.taxa, community.size))
      # evaluate congruence
      congruence.value <- TreeDist::MatchingSplitInfoDistance(host.tree, neutral.tree)
      null.model <- c(null.model, congruence.value)
    }
  }
  
  # MCI
  if (congruence.metric == 'MCI'){
    for (i in 1:iterations){
      # generate neutral assembly tree
      neutral.tree <- ape::as.phylo(simulate.neutral.assembly.tree(n.hosts, n.microbial.taxa, community.size))
      # evaluate congruence
      congruence.value <- TreeDist::MutualClusteringInfo(host.tree, neutral.tree)
      null.model <- c(null.model, congruence.value)
    }
  }
  
  # SPI
  if (congruence.metric == 'SPI'){
    for (i in 1:iterations){
      # generate neutral assembly tree
      neutral.tree <- ape::as.phylo(simulate.neutral.assembly.tree(n.hosts, n.microbial.taxa, community.size))
      # evaluate congruence
      congruence.value <- TreeDist::SharedPhylogeneticInfo(host.tree, neutral.tree)
      null.model <- c(null.model, congruence.value)
    }
  }
  
  # NS
  if (congruence.metric == 'NS'){
    for (i in 1:iterations){
      # generate neutral assembly tree
      neutral.tree <- ape::as.phylo(simulate.neutral.assembly.tree(n.hosts, n.microbial.taxa, community.size))
      # evaluate congruence
      congruence.value <- TreeDist::NyeSimilarity(host.tree, neutral.tree)
      null.model <- c(null.model, congruence.value)
    }
  }
  
  return(null.model)
}

# function to run simulations for comparing null congruence distributions
# between neutral assembly model and rtree model
comps.simulation <- function(tree.size, n.microbial.taxa, community.size, congruence.metric, iterations){
  
  normalized.differences <- c()
  
  for (i in 1:iterations){
    # simulate a host tree and microbial community tree
    host.tree <- ape::write.tree(ape::rtopology(tree.size, rooted=FALSE))
    community.tree <- ape::write.tree(ape::rtopology(tree.size, rooted=FALSE))
  
    # run rtc test
    rtc.null.model <- sort(manticore::rtc.test(host.tree, community.tree, congruence.metric, iterations=1000)$null.congruence.model)
  
    # run neutral assembly null 
    neutral.assembly.null.model <- sort(neutral.assembly.model(host.tree, n.microbial.taxa=100, community.size=1000, congruence.metric, iterations=1000))
  
    # calculate empirical cumulative density functions
    F1 <- ecdf(rtc.null.model)
    F2 <- ecdf(neutral.assembly.null.model)
    
    # get unique points
    x.all <- sort(unique(c(rtc.null.model, neutral.assembly.null.model)))

    # approximate integrated difference with Riemann sum
    dx <- diff(range(x.all)) / length(x.all)
    int.diff <- sum(abs(F1(x.all) - F2(x.all))) * dx
    # relativize to x range
    norm.diff <- int.diff / diff(range(x.all))
    # add to data
    normalized.differences <- c(norm.diff, normalized.differences)
  }
  return(normalized.differences)
}

# function to run simulations
run.simulations <- function(metrics, tree.sizes, n.microbial.taxa, community.size, iterations){
  # initialize dataframe to store data
  simulation.data <- data.frame(
    norm.diff = numeric(),
    metric = character(),
    tree.size = numeric(),
    stringsAsFactors = FALSE
  )
  
  # iterate through metrics
  for (metric in metrics){
    # iterate through tree sizes
    for (tree.size in tree.sizes){
      print(paste("Working on tree.size", tree.size, "for", metric))
      # run comparison
      norm.diff <- comps.simulation(tree.size, n.microbial.taxa, community.size, metric, iterations)
      # add to data
      run.data <- data.frame(
        norm.diff = norm.diff,
        metric = metric,
        tree.size = tree.size,
        stringsAsFactors = FALSE
      )
      simulation.data <- rbind(simulation.data, run.data)
    }
  }
  return(simulation.data)
}

metrics <- c("RF", "ICRF", "JRF", "MSD", "MSID", "MCI", "SPI", "NS")
tree.sizes <- c(5, 10, 20, 40, 60, 80, 100)

set.seed(123)
sim.data <- run.simulations(metrics, tree.sizes, n.microbial.taxa=100, community.size=1000, iterations=100)
write.csv(sim.data, '../data/neutral_assembly_comparisons.csv')
