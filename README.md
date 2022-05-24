# Phaeoflanker
Phaeoflanker is a Shell + python script originally developed to process algal genomic data with known viral elements in them. More broadly it can, from the fasta and gff files of your genomes, and by using a text file listing the names of all your genomes + another text file cataloguing all your sequences of interest and their position in the genome, extract these sequences, their flanking regions, produce multifasta and gff files for them, and do some further operations such as producing png images of their gene sequences. 
# To start with Phaeoflanker
Before launching Phaeoflanker, you must be sure that :
1) You have Bedtools installed on your computer.
2) You have the .fasta files and the .gff files of your genomes in separated folders.
3) You have modified phaeoflanker.sh f1 and f2 variables to be the paths of your .fa and .gff folders respectively.
[WIP]
