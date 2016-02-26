pdf("FaceFriends.pdf")

data2 = read.table(file.choose(), head=F, sep = ",")


plot(type="p", data2$V1, xlab = "Friends", ylab="Friend Counts", 
     main = "Facebook Friendship Paradox", xlim=c(0, 160), 
     ylim=c(0, 3500), las=0, col="red", pch=16, cex=0.3)
muser=which(data2$V2 == "Michael L. Nelson")
abline(v=muser, col=84, lty = 1)


legend(x=55,y=3400,c("Michael L. Nelson"),
       col = 84, lty = 1)

mean(data2$V1)
#357.74

median(data2$V1)
#259

sd(data2$V1)
#370.7

dev.off()