pdf("TwitterFollowerslg.pdf")

data = read.table(file.choose(), head=F, sep = "")


plot(type="p", data$V1, xlab = "Followers", ylab="Follower Counts", 
     main = "Twitter Friendship Paradox", xlim=c(0, 500), 
     ylim=c(1, 75000), las=0, col="red", pch=16, cex=0.3, log='y')
muser=which(data$V2 == "phonedude_mln")
abline(v=muser, col=84, lty = 1)
y = c(0, 10, 100, 1000, 10000, 100000)

legend(x=.1,y=70000,c("Michael L. Nelson"),
       col = 84, lty = 1)

mean(data$V1)
#1045.867

median(data$V1)
#259

sd(data$V1)
#4146.195

dev.off()