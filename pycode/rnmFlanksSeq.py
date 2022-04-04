'''
Written by Patrick Jacques the 24/02/22

Add upstream and downstream to the names of
a fasta file. Only use with the sequences
of flanking regions.
'''
import sys
import common_code as cc

for fasta in sys.argv[1:]:
    side = 0
    bigBadString = ""
    lines = cc.get_lines(fasta)
    for line in lines:
        if line[0] == ">" and side == 0:
            line = line[:-1]+"_upstream\n"
            side = 1
        elif line[0] == ">" and side == 1:
            line = line[:-1]+"_downstream\n"
            side = 0
        bigBadString = bigBadString + line
    cc.save_file(fasta,bigBadString)