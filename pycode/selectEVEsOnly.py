'''
Written by Patrick Jacques the 22/02/2022

python3 selectEVEsOnly.py [GFF] [good/maybe/provirus] [[GFF_without_path]]
'''
import sys
import common_code as cc

path = sys.argv[1]
parameter = sys.argv[2]
name_of_gff = sys.argv[3]
name_of_fold1 = "./genes_of_EVEs"
name_of_fold2 = "./sizes"
name_of_fold3 = "./fasta_of_genes"
name_of_fold4 = "./EVEs"
name_of_fold5 = "./FLANKs"

cc.check_and_make(name_of_fold1)
cc.check_and_make(name_of_fold2)
cc.check_and_make(name_of_fold3)
cc.check_and_make(name_of_fold4)
cc.check_and_make(name_of_fold5)

while parameter not in ["good","maybe","provirus"]:
    parameter = input("You want the genes coming from which kind of contigs ?\n Type 'good', 'maybe', or 'provirus' \n").lower()

if parameter == "provirus":
    lines = cc.get_lines("contigs/contigs_provirus.txt")
elif parameter == "maybe":
    lines = cc.get_lines("contigs/contigs_maybe.txt")
else :
    lines = cc.get_lines('contigs/contigs_good.txt')
lines = cc.stripNewLine(lines)

gff_lines = cc.get_lines(path)

dump = [0]*len(gff_lines)
for i in range(len(gff_lines)):
    g = gff_lines[i].split("\t")
    for y in range(len(lines)):
        c_line = lines[y].split("\t")
        if (g[0] == c_line[0]) \
            and ((int(g[3]) >= int(c_line[-2]) and int(g[3]) <= int(c_line[-1])) or (int(g[4]) >= int(c_line[-2]) and int(g[4]) <= int(c_line[-1]))):
            dump[i] += 1
for z in sorted(range(len(gff_lines)), reverse=True):
    if dump[z] == 0:
        gff_lines.pop(z)

bbstring = ''
for e in gff_lines:
    bbstring = bbstring + e + '\n'
cc.save_file(f"{name_of_fold1}/{parameter}_{name_of_gff}",bbstring)
