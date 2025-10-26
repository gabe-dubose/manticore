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
  metrics <- c('RF', 'ICRF', 'JRF', 'MCI', 
               'SPI', 'NS', 'MSD', 'MSID')
  
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

#' Perform random tree congruence test 
#' 
#' @description Perform a  
#' random tree congruence test. This function
#' uses Monte Carlo simulations to generate a
#' null congruence distribution and then 
#' evaluates the proportion of null comparisons 
#' that showed congruence that was greater than 
#' or equal to that of the observed congruence. 
#' 
#' @param reference.tree Path to reference tree file, or string in Newick format
#' @param comparison.tree Path to comparison tree file, or string in Newick format
#' @param congruence.metric Metric used to evaluate congruence. Options include:
#' 
#' - MCI: Mutual Clustering Information (Smith, 2020a)
#'
#' - SPI: Shared Phylogenetic Information (Smith, 2020a)
#'
#' - NS: Nye Similarity (Nye et al, 2006)
#'
#' - JRF: Jaccard-Robinson-Foulds (Böcker et al, 2013)
#'
#' - MSD: Matching Split Distance (Bogdanowicz and Giaro, 2012)
#'
#' - MSID: Matching Split Information Distance (Smith, 2020a)
#'
#' - RF: Robinson-Foulds (Robinson and Foulds, 1981)
#'
#' - ICRF: Information-Corrected Robinson Foulds (Smith, 2020a)
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
#' @details 
#' The random tree congruence test can be used with 
#' a variety of congruence metrics that vary in 
#' what aspects of congruence they consider. The
#' congruence metrics offered are all implemented 
#' by the <b><i>TreeDist</i></b> library (Smith 2020b).
#' The random tree simulations are implemented by the
#' <b><i>ape</i></b> library (Paradis and Schliep 2019).
#' Any use of this library should include reference to 
#' these libraries as well (see References section). 
#' Furthermore, the specific congruence metric(s) used
#' should also be referenced (see above list). 
#' 
#' @examples
#' tree1 <- 'path/to/tree1.nwk'
#' tree2 <- 'path/to/tree2.nwk'
#' rtc.test(reference.tree=tree1, comparison.tree=tree2, congruence.metric='MCI', iterations=1000, verbose=TRUE)
#' 
#' @references 
#' Böcker S., Canzar S., Klau G.W. (2013) The Generalized Robinson-Foulds Metric. In Algorithms in Bioinformatics (eds A Darling, J Stoye), pp. 156–169. Berlin, Heidelberg: Springer Berlin Heidelberg. 
#' 
#' Bogdanowicz D., Giaro K. (2012) Matching Split Distance for Unrooted Binary Phylogenetic Trees. IEEE/ACM Trans. Comput. Biol. and Bioinf. doi:10.1109/TCBB.2011.48
#' 
#' Nye T.M.W., Liò P., Gilks W.R. (2006) A novel algorithm and web-based tool for comparing two alternative phylogenetic trees. Bioinformatics. doi:10.1093/bioinformatics/bti720
#' 
#' Paraids E., Schliep K. (2019) ape 5.0: an environment for modern phylogenetics and evolutionary analyses in R. Bioinformatics. doi:10.1093/bioinformatics/bty633
#' 
#' Robinson D.F., Foulds L.R. (1981) Comparison of phylogenetic trees. Mathematical Biosciences. doi:10.1016/0025-5564(81)90043-2
#' 
#' Smith MR. (2020a) Information theoretic generalized Robinson–Foulds metrics for comparing phylogenetic trees. Bioinformatics. doi:10.1093/bioinformatics/btaa614
#' 
#' Smith M.R. (2020b) TreeDist: distances between phylogenetic trees. Comprehensive R Archive Network. doi: 10.5281/zenodo.3528123.
#' 
#' @export
rtc.test <- function(reference.tree, comparison.tree, congruence.metric, iterations, verbose=FALSE){
  
  # load input
  input <- input.check(reference.tree, comparison.tree, congruence.metric, iterations)
  
  # check that input was loaded correctly
  if (input$load.success == TRUE) {
    if (verbose == TRUE) {
      print("Input loaded.")
    }
    
    # define metric and normalization
    metric <- input$loaded.congruence.metric
    normalize <- FALSE
    
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
    
    # run rtc tests
    
    # metric: Robinson-Foulds
    # distance: greater value = less congruent (more dissimilar)
    #  => calculate the number of null runs that showed less than or equal to congruence
    if (metric == 'RF'){
      p.null.geq.obs <- sum(null.congruence.model <= observed) / length(null.congruence.model)
      # assemble output and return
      rtc.results <- list(observed.congruence = observed,
                          p = p.null.geq.obs,
                          null.congruence.model = null.congruence.model)
    }
    
    # metric:Information-Corrected Robinson-Foulds Distance
    # distance: greater value = less congruent (more dissimilar)
    # => calculate the number of null runs that showed less than or equal to congruence
    if (metric == 'ICRF'){
      p.null.geq.obs <- sum(null.congruence.model <= observed) / length(null.congruence.model)
      # assemble output and return
      rtc.results <- list(observed.congruence = observed,
                          p = p.null.geq.obs,
                          null.congruence.model = null.congruence.model)
    }
    
    # metric:Jaccard-Robinson-Foulds Distance
    # distance: greater value = less congruent (more dissimilar)
    # => calculate the number of null runs that showed less than or equal to congruence
    if (metric == 'JRF'){
      p.null.geq.obs <- sum(null.congruence.model <= observed) / length(null.congruence.model)
      # assemble output and return
      rtc.results <- list(observed.congruence = observed,
                        p = p.null.geq.obs,
                        null.congruence.model = null.congruence.model)
    }
    # metric: Matching Split Distance
    # distance: greater value = less congruent (more dissimilar)
    # => calculate the number of null runs that showed less than or equal to congruence
    if (metric == 'MSD'){
      p.null.geq.obs <- sum(null.congruence.model <= observed) / length(null.congruence.model)
      # assemble output and return
      rtc.results <- list(observed.congruence = observed,
                          p = p.null.geq.obs,
                          null.congruence.model = null.congruence.model)
    }
      
    # metric: Matching Split Information Distance
    # distance: greater value = less congruent (more dissimilar)
    # => calculate the number of null runs that showed less than or equal to congruence   
      
    if (metric == 'MSID'){
      p.null.geq.obs <- sum(null.congruence.model <= observed) / length(null.congruence.model)
      # assemble output and return
      rtc.results <- list(observed.congruence = observed,
                          p = p.null.geq.obs,
                          null.congruence.model = null.congruence.model)
    }
      
    # metric: Mutual Clustering Information
    # dissimilarity: higher value = more congruent
    # => calculate the number of null runs that showed greater than or equal to congruence      
      
    if (metric == 'MCI'){
      p.null.geq.obs <- sum(null.congruence.model >= observed) / length(null.congruence.model)
      # assemble output and return
      rtc.results <- list(observed.congruence = observed,
                          p = p.null.geq.obs,
                          null.congruence.model = null.congruence.model)
    }
      
    # metric: Shared Phylogenetic Information
    # dissimilarity: higher value = more congruent
    # => calculate the number of null runs that showed greater than or equal to congruence      
      
    if (metric == 'SPI'){
      p.null.geq.obs <- sum(null.congruence.model >= observed) / length(null.congruence.model)
      # assemble output and return
      rtc.results <- list(observed.congruence = observed,
                          p = p.null.geq.obs,
                          null.congruence.model = null.congruence.model)
    }
      
    # metric: Nye Similarity
    # dissimilarity: higher value = more congruent
    # => calculate the number of null runs that showed greater than or equal to congruence    
    if (metric == 'NS'){
      p.null.geq.obs <- sum(null.congruence.model >= observed) / length(null.congruence.model)
      # assemble output and return
      rtc.results <- list(observed.congruence = observed,
                          p = p.null.geq.obs,
                          null.congruence.model = null.congruence.model)
    }
       
    if (verbose == TRUE) {
      print("Complete.")
    }
    return(rtc.results)
    
  # show error if run fails    
  } else {
    print(input$error)
  }
}
