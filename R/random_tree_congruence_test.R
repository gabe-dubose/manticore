# Internal function to check that inputs can be loaded correctly
input.check <- function(reference.tree, comparison.tree, congruence.metric, iterations) {
  
  # list to store loading status
  load.status <- list(reference.tree.check = 0, 
                      comparison.tree.check = 0,
                      metric.check = 0, 
                      iteration.check = 0,
                      reference.tree.format = 'None',
                      comparison.tree.format = 'None',
                      error = 'Errors:',
                      load.success = TRUE,
                      loaded.reference.tree = NULL,
                      loaded.comparison.tree = NULL,
                      loaded.congruence.metric = NULL,
                      loaded.iterations = NULL)

  # check that trees can be loaded
  reference.tree.file.test <- tryCatch({
    suppressWarnings(ape::read.tree(reference.tree))
  }, error = function(e) {
    return(NULL)
  })
  
  reference.tree.text.test <- tryCatch({
    suppressWarnings(ape::read.tree(text = reference.tree))
  }, error = function(e) {
    return(NULL)
  })
  
  comparison.tree.file.test <- tryCatch({
    suppressWarnings(ape::read.tree(comparison.tree))
  }, error = function(e) {
    return(NULL)
  })
  
  comparison.tree.text.test <- tryCatch({
    suppressWarnings(ape::read.tree(text = comparison.tree))
  }, error = function(e) {
    return(NULL)
  })

  # check reference tree
  if (!is.null(reference.tree.file.test)){
    load.status$reference.tree.check <- 1
    load.status$reference.tree.format <- 'file'
    # load reference tree
    load.status$loaded.reference.tree <- ape::read.tree(reference.tree)
  } else if (!is.null(reference.tree.text.test)) {
    load.status$reference.tree.check <- 1
    load.status$reference.tree.format <- 'text'
    # load reference tree
    load.status$loaded.reference.tree <- ape::read.tree(text = reference.tree)
  } else {
    load.status$error <- paste(load.status$error, 'Reference tree could not be read;')
    load.status$load.success <- FALSE
  }
  
  # check comparison tree
  if (!is.null(comparison.tree.file.test)){
    load.status$comparison.tree.check <- 1
    load.status$comparison.tree.format <- 'file'
    # load comparison tree
    load.status$loaded.comparison.tree <- ape::read.tree(comparison.tree)
  } else if (!is.null(comparison.tree.text.test)) {
    load.status$comparison.tree.check <- 1
    load.status$comparison.tree.format <- 'text'
    # load comparison tree
    load.status$loaded.comparison.tree <- ape::read.tree(text = comparison.tree)
  } else {
    load.status$error <- paste(load.status$error, 'Comparison tree could not be read;')
    load.status$load.success <- FALSE
  }
  
  # define metrics for check
  metrics <- c('RF', 'RF+n', 'ICRF', 'ICRF+n', 'JRF', 'JRF+n', 'MCI', 'MCI+n', 
               'SPI', 'SPI+n', 'NS', 'NS+n', 'MSD', 'MSD+n', 'MSID', 'MSID+n')
  
  # check that congruence metric is defined
  if (congruence.metric %in% metrics) {
    load.status$metric.check <- 1
    # load congruence metric
    load.status$loaded.congruence.metric <- congruence.metric
  } else {
    load.status$error <- paste(load.status$error, 'Unrecognized congruence metric specified;')
    load.status$load.success <- FALSE
  }

  # check that iteration specification is an integer
  iterations <- as.integer(iterations)
  if (is.integer(iterations)) {
    load.status$iteration.check <- 1
    # load iterations
    load.status$loaded.iterations <- iterations
  } else {
    load.status$error <- paste(load.status$error, '[iterations] parameter must be an integer;')
    load.status$load.success <- FALSE
  }
  
  return(load.status)  

}

# Internal function to generate null congruence distribute for reference tree
generate.null.model <- function(reference.tree, metric, iterations, normalize) {
  #initialize vector to store congruence values
  null.congruence.model <- c()
  
  # store tip labels and count for tree simulation
  tip.labels <- reference.tree$tip.label
  tip.count <- length(tip.labels)
  
  #generate null model using Robinson-Foulds Distance
  if (metric == 'RF') {
    for (i in 1:iterations) {
      #simulate random tree
      simulated.tree <- ape::rtopology(tip.count, rooted=FALSE, tip.label=tip.labels)
      #evaluate congruence with reference tree
      congruence.value <- TreeDist::RobinsonFoulds(reference.tree, simulated.tree, normalize=normalize)
      #add congruence value to null model vector
      null.congruence.model <- c(null.congruence.model, as.numeric(congruence.value))
    }
  }
  
  #generate null model using Information-Corrected Robinson-Foulds Distance
  if (metric == 'ICRF') {
    for (i in 1:iterations) {
      #simulate random tree
      simulated.tree <- ape::rtopology(tip.count, rooted=FALSE, tip.label=tip.labels)
      #evaluate congruence with reference tree
      congruence.value <- TreeDist::InfoRobinsonFoulds(reference.tree, simulated.tree, normalize=normalize)
      #add congruence value to null model vector
      null.congruence.model <- c(null.congruence.model, as.numeric(congruence.value))
    }
  }
  
  #generate null model using Jaccard-Robinson-Foulds Distance
  if (metric == 'JRF') {
    for (i in 1:iterations) {
      #simulate random tree
      simulated.tree <- ape::rtopology(tip.count, rooted=FALSE, tip.label=tip.labels)
      #evaluate congruence with reference tree
      congruence.value <- TreeDist::JaccardRobinsonFoulds(reference.tree, simulated.tree, normalize=normalize)
      #add congruence value to null model vector
      null.congruence.model <- c(null.congruence.model, as.numeric(congruence.value))
    }
  }
  
  #generate null model using Matching Split Distance
  if (metric == 'MSD') {
    for (i in 1:iterations) {
      #simulate random tree
      simulated.tree <- ape::rtopology(tip.count, rooted=FALSE, tip.label=tip.labels)
      #evaluate congruence with reference tree
      congruence.value <- TreeDist::MatchingSplitDistance(reference.tree, simulated.tree, normalize=normalize)
      #add congruence value to null model vector
      null.congruence.model <- c(null.congruence.model, as.numeric(congruence.value))
    }
  }
  
  #generate null model using Matching Split Information Distance
  if (metric == 'MSID') {
    for (i in 1:iterations) {
      #simulate random tree
      simulated.tree <- ape::rtopology(tip.count, rooted=FALSE, tip.label=tip.labels)
      #evaluate congruence with reference tree
      congruence.value <- TreeDist::MatchingSplitInfoDistance(reference.tree, simulated.tree, normalize=normalize)
      #add congruence value to null model vector
      null.congruence.model <- c(null.congruence.model, as.numeric(congruence.value))
    }
  }
  
  #generate null model using Mutual Clustering Information
  if (metric == 'MCI') {
    for (i in 1:iterations) {
      #simulate random tree
      simulated.tree <- ape::rtopology(tip.count, rooted=FALSE, tip.label=tip.labels)
      #evaluate congruence with reference tree
      congruence.value <- TreeDist::MutualClusteringInfo(reference.tree, simulated.tree, normalize=normalize)
      #add congruence value to null model vector
      null.congruence.model <- c(null.congruence.model, as.numeric(congruence.value))
    }
  }
  
  #generate null model using Shared Phylogenetic Information
  if (metric == 'SPI') {
    for (i in 1:iterations) {
      #simulate random tree
      simulated.tree <- ape::rtopology(tip.count, rooted=FALSE, tip.label=tip.labels)
      #evaluate congruence with reference tree
      congruence.value <- TreeDist::SharedPhylogeneticInfo(reference.tree, simulated.tree, normalize=normalize)
      #add congruence value to null model vector
      null.congruence.model <- c(null.congruence.model, as.numeric(congruence.value))
    }
  }
  
  #generate null model using Nye Similarity
  if (metric == 'NS') {
    for (i in 1:iterations) {
      #simulate random tree
      simulated.tree <- ape::rtopology(tip.count, rooted=FALSE, tip.label=tip.labels)
      #evaluate congruence with reference tree
      congruence.value <- TreeDist::NyeSimilarity(reference.tree, simulated.tree, normalize=normalize)
      #add congruence value to null model vector
      null.congruence.model <- c(null.congruence.model, as.numeric(congruence.value))
    }
  }
  
  #sort null model and return
  null.congruence.model <- sort(null.congruence.model)
  return(null.congruence.model)
}

# Internal function to calcualte observed congruence
observed.congruence <- function(reference.tree, comparison.tree, metric, normalize) {
  # Robinson-Foulds Distance
  if (metric == 'RF') {
    congruence.value <- TreeDist::RobinsonFoulds(reference.tree, comparison.tree, normalize=normalize)
  }
  
  # Information-Corrected Robinson-Foulds Distance
  if (metric == 'ICRF') {
    congruence.value <- TreeDist::InfoRobinsonFoulds(reference.tree, comparison.tree, normalize=normalize)
  }
  
  # Jaccard-Robinson-Foulds Distance
  if (metric == 'JRF') {
    congruence.value <- TreeDist::JaccardRobinsonFoulds(reference.tree, comparison.tree, normalize=normalize)
  }
  
  # Matching Split Distance
  if (metric == 'MSD') {
    congruence.value <- TreeDist::MatchingSplitDistance(reference.tree, comparison.tree, normalize=normalize)
  }
  
  # Matching Split Information Distance
  if (metric == 'MSID') {
    congruence.value <- TreeDist::MatchingSplitInfoDistance(reference.tree, comparison.tree, normalize=normalize)
  }
  
  # Mutual Clustering Information
  if (metric == 'MCI') {
    congruence.value <- TreeDist::MutualClusteringInfo(reference.tree, comparison.tree, normalize=normalize)
  }
  
  # Shared Phylogenetic Information
  if (metric == 'SPI') {
    congruence.value <- TreeDist::SharedPhylogeneticInfo(reference.tree, comparison.tree, normalize=normalize)
  }
  
  # Nye Similarity
  if (metric == 'NS') {
    congruence.value <- TreeDist::NyeSimilarity(reference.tree, comparison.tree, normalize=normalize)
  }
  
  return(congruence.value)
}

#' Random Tree Congruence Test
#' 
#' @param reference.tree Path to reference tree file, or string in Newick format
#' @param comparison.tree Path to comparison tree file, or string in Newick format
#' @param congruence.metric Metric used to evaluate congruence. Options include:
#' 
#' - MCI: Mutual Clustering Information
#'
#' - SPI: Shared Phylogenetic Information
#'
#' - NS: Nye Similarity
#'
#' - JRF: Jaccard-Robinson-Foulds
#'
#' - MSD: Matching Split Distance
#'
#' - MSID: Matching Split Information Distance
#'
#' - RF: Robinson-Foulds
#'
#' - ICRF: Information-Corrected Robinson Foulds
#' 
#' Note: add '+n' to metric abbreviation to perform normalization. For example,
#' for normalized JRF, use 'JRF+n'
#' 
#' @param iterations The number of randomly simulated trees used to construct null distribution
#' @param verbose Display run updates (TRUE of FALSE)
#' @return Function returns the random tree congruence test results. This is a list object that contains: 
#' 
#' <b>observed.congruence</b>: The observed congruence between the reference and comparison trees (based on specified congruence metric)
#' 
#' <b>p</b>: The proportion of values in the null distribution that are greater than or equal to the observed congruence
#' 
#' <b>null.congruence.model</b>: A vector containing the null congruence values
#' @export
rtc.test <- function(reference.tree, comparison.tree, congruence.metric, iterations, verbose=FALSE){
  
  # load input
  input <- input.check(reference.tree, comparison.tree, congruence.metric, iterations)
  
  # check that input was loaded correctly
  if (input$load.success == TRUE) {
    if (verbose == TRUE) {
      print("Input loaded.")
    }
    
    # determine normalization
    if (grepl("\\+n$", input$loaded.congruence.metric)) {
      normalize <- TRUE
      metric <- sub("\\+n$", "", input$loaded.congruence.metric)
    } else {
      normalize <- FALSE
      metric <- input$loaded.congruence.metric
    }
    
    if (verbose == TRUE) {
      print("Generating null congruence model...")
    }
    # generate null model
    null.congruence.model <- generate.null.model(input$loaded.reference.tree,
                                                 metric,
                                                 input$loaded.iterations,
                                                 normalize = normalize)
    if (verbose == TRUE) {
      print("Null model generation complete.")
      print("Running random tree congruence test...")
    }
    
    #calculate observed congruence
    observed <- observed.congruence(input$loaded.reference.tree, input$loaded.comparison.tree, metric, normalize = normalize)
    
    # calculate the number of null runs that showed greater than or equal to
    # congruence 
    p.null.geq.obs <- sum(null.congruence.model >= observed) / length(null.congruence.model)

    # assemble output and return
    rtc.results <- list(observed.congruence = observed,
                        p = p.null.geq.obs,
                        null.congruence.model = null.congruence.model)
    
    if (verbose == TRUE) {
      print("Complete.")
    }
    return(rtc.results)
    
  # show error if run fails    
  } else {
    print(input$error)
  }
}

