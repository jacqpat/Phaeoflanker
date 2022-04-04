'''
written by Patrick Jacques the 23 of March 2022

Separated from selectEVEsOnly.py to correct a bug
'''
import sys
import common_code as cc

cc.check_and_make("./sizes")
parameter = sys.argv[1]
lines = cc.get_contigs(parameter)
ccstring = ''
for y in range(len(lines)):
    c_line = lines[y].split("\t")
    if len(c_line) >= 2: 
        ccstring = ccstring + c_line[0]+"\t"+c_line[1]+"\n"
cc.save_file(f"sizes/sizes_{parameter}_contigs.txt",ccstring)