#!/bin/bash

dirs="./FLANKs/*/"

for d in $dirs ; do
    [ -L "${d%/}" ] && continue
    echo "$d"
    if [ -z "$(ls -A $d)" ]; then
        rm -r $d
        echo "deleted empty directory"
    else
        save="${d}sorted"
        echo "sorted files in : ${save}"
        python3 pycode/gffSorter.py $d
        ./shcode/gtsketch.sh $save
    fi
done