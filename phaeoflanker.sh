#!/bin/bash

f="./sources/names.txt"
f1="./sources_fa"
f2="./sources_gff"
param="good"
wdw="50000"
lines=$(cat $f)

python3 pycode/size_of_contigs.py $param
sze="./sizes/sizes_${param}_contigs.txt"

for l in $lines
do
    echo $l
    fst="$l.fa"
    gff="$l.gff"
    sfst="${f1}/${fst}"
    sgff="${f2}/${gff}"
    gff2="./genes_of_EVEs/${param}_${gff}"
    fst2="./fasta_of_genes/${param}_${fst}"
    bed1="./BED/EVEs_of_$l.bed"
    bed2="./BED/FLANKS_of_${param}_${l}_${wdw}.bed"
    out1="./EVEs/EVEs_of_${param}_${fst}"
    out2="./FLANKs/FLANKS_of_${param}_${fst}"
    fname="FlankingGENES_${param}EVEs_${wdw}_$l"
    fld="./FLANKs/${fname}"
    mtrx="./matrices/${fname}"
    python3 pycode/selectEVEsOnly.py $sgff $param $gff
    python3 pycode/getBED_of_EVEs.py $gff2 $wdw $sze $gff $param
    bedtools getfasta -name -fi $sfst -bed $gff2 -fo $fst2
    bedtools getfasta -fi $sfst -bed $bed1 -fo $out1
    bedtools getfasta -fi $sfst -bed $bed2 -fo $out2
    python3 pycode/rnmFlanksSeq.py $out2
    python3 pycode/getSeqGenes.py $sgff $out2 $fld
    python3 pycode/mkrMatrix4gff.py $fld $mtrx 
done
./shcode/sort_and_drawFlanks.sh
