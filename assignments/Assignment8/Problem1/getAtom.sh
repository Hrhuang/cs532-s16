#!/bin/bash

while read line;
do
    test=`curl $line | grep 'rel="alternate"' | grep atom | sed 's/.*href=//' | sed 's/\/>//' | sed 's/"//g' | sed 's/ //g'` 
    echo $test >> atom.txt
done < unique.txt

