#!/bin/bash
i=1;
while read line;
do
    curl -L -o blogPage$i.txt "$line"
    i=$[$i+1];
done < unique.txt