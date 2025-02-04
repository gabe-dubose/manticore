# load example trees
tree1 <- manticore::get.tree(1)
tree2 <- manticore::get.tree(2)

# run rtc test
rtc.results <- manticore::rtc.test(tree1, tree2, 'MCI', 1000,
                                   verbose=TRUE)

# print results
print(paste("Congruence =", rtc.results$observed.congruence,
      "P(Null >= Observed) =", rtc.results$p))

# visualize null distribution
hist(rtc.results$null.congruence.model,
     main=paste("P(Null >= Observed) =", rtc.results$p), 
     xlab='Congruence',
     freq = FALSE)
abline(v=rtc.results$observed.congruence,
       col='red', lty=2, lwd=2)

