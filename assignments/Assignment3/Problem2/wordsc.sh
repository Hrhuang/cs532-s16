#!/bin/bash

#google match of word gamer: 150,000,000
#google's estimation of world wide web: 47.1 billion

IDF=`awk "BEGIN {printf \"%9.2f\n\", log(47100000000/150000000)/log(2)}"`

rm data1.txt
rm data2.txt
count=0
echo 'MW TW          LINK' > data1.txt
echo 'TFIDF    TF       IDF       LINK' > data2.txt

for file in `ls /home/hhuang/Documents/CS532/WebScienceAssig/HW3/Problem1/ProcessedHTMLs/processedHTMLs`; 
do
	totalwords=`wc -w "/home/hhuang/Documents/CS532/WebScienceAssig/HW3/Problem1/ProcessedHTMLs/processedHTMLs/"$file | cut -d' ' -f1`
	wordmatch=`grep -c "gamer" "/home/hhuang/Documents/CS532/WebScienceAssig/HW3/Problem1/ProcessedHTMLs/processedHTMLs/"$file`
	link=`grep -w $file "/home/hhuang/Documents/CS532/WebScienceAssig/HW3/Problem2/fileNumWithLink.txt" | awk '{ print $2}'`

	if [ $wordmatch -ne 0 ] && [ $count -lt 20 ]; 
		then
		count=$[$count+1]
		TF=`awk "BEGIN {printf \"%6.6f\n\", ($wordmatch/$totalwords)}"`
		TFIDF=`awk "BEGIN {printf \"%6.6f\n\", ($TF*$IDF)}"`
		echo $wordmatch $totalwords $link >> data1.txt
		echo $TFIDF $TF $IDF $link >> data2.txt
		
	fi
	
done

