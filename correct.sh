#!/bin/bash

RED='\033[0;31m'
GREEN='\033[0;32m'
NC='\033[0m'

path=$1

rm -rf user_output
rm -rf wrongs

mkdir user_output
mkdir wrongs

files=`ls ./input`

correct=0
count=0
for file in $files
do
    python3 $path < ./input/$file > ./user_output/$file
    status=$(diff ./output/$file ./user_output/$file -w)
    if [[ -z ${status} ]] then
        printf "${file} ${GREEN}ACCEPTED${NC}\n"
        correct=$((correct + 1))
    else
        printf "${file} ${RED}WRONG ANSWER${NC}\n"
        echo $status > wrongs/$file 
    fi
    count=$((count + 1))
done

echo 'score: '$correct'/'$count