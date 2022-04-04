#!/bin/bash

if [ ! -d "./images" ]; then
    mkdir "./images"
fi
files="${1}/*"
for f in $files
do
    fext="${f##*.}" # file extension
    seek="gff"      # extension to match
    if [[ "$fext" == "$seek" ]]; then
        g=$(basename -- "$f")
        fname="${g%.*}"
        out1="${1}/${fname}.gff3"
        out2="./images/${fname}.png"
        if [ -f "out1" ]; then
            gt sketch -format png $out2 $out1
        else 
            gt gff3 -tidy yes -checkids yes -fixregionboundaries yes -addintrons yes -o $out1 $f
            gt sketch -format png $out2 $out1
        fi
    fi
done