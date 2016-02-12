data2 = read.table(file.choose(), header = F)

r = hist(data2$V1, ylim = c(0, 1000), breaks = seq(from=0, to=20000, by=400), 
         plot = F)

r$counts = log10(r$counts+1)


plot(r, main="Histogram of Count of Mementos", xlab = "Number of Mementos",
     ylab = "URLs(log of 10)")