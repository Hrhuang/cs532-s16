#!/bin/bash

echo "http://f-measure.blogspot.com/" > blogList.txt 
echo "http://ws-dl.blogspot.com/" >> blogList.txt 

for (( i = 3; i < 400; i++ )); do
	#printf "blogPages$i.txt " >> blogList.txt
	curl -L -o uselesspage.txt -w %{url_effective} 'https://www.blogger.com/next-blog?navBar=true&blogID=3471633091411211117' >> blogList.txt
	printf "\n" >> blogList.txt
done