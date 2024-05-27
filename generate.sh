#!/bin/bash

rm -rf input
rm -rf output

mkdir input
mkdir output

n=0

if [ $# -eq 0 ]; then
    n=10
else
    n=$1
fi

for ((i=0; i<$n; i++))
do
    python3 random-gen.py > input/$i
    python3 main.py < input/$i > output/$i
done