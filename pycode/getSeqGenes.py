'''
Written by Patrick Jacques the 24/02/2022

This script makes a GFF file of all the genes
in a sequence (from a FASTA file) using a list
of genes in another GFF.

As in, we compare the genes positions in a GFF to
the name and position of a sequence, and if it match
we record them in a new GFF file.

Very inefficient parsing

python3 getSeqGenes.py [GFF] [FASTA] [NAME_DIR]
'''
import re
import os
import sys
import common_code as cc

cc.check_and_make(f'./{sys.argv[3]}')
linesGFF = cc.get_lines(sys.argv[1])
linesFST = cc.get_lines(sys.argv[2])

for l in linesFST:
    if l[0] == ">":
        bigBadString = ""
        s_contig = re.search(">(.*?):",l).group(1)
        s_start = int(re.search("\:(.*?)\-",l).group(1))
        s_end = int(re.search("[0-9]\-(.*?)\_",l).group(1))
        for n in linesGFF:
            g = n.split('\t')
            if (s_contig == g[0]) and \
                ((int(g[3]) > s_start and int(g[3]) < s_end) or (int(g[4]) > s_start and int(g[4]) < s_end)):
                bigBadString = bigBadString + n
        filepath = os.path.join(f'./{sys.argv[3]}', f'{l[1:-1]}.gff')
        cc.save_file(filepath,bigBadString)
