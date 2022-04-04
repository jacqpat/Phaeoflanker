'''
Written by Patrick Jacques the 21 March 2022

post processing of the EVEs gff files so that
genes are ordered on the 5' -> 3' axis

Something of a duplicate of the previous one for
the Flanks, but I need some slight changes.

Note : once it's over, think of merging anything
in common between the two gffSorters into
common_code.py functions.

Note : DO NOT filter ONLY with int(x[3]) when you have
multiple contigs you stupid !

python3 gffSorter4main.py [good/maybe/provirus]
'''
import os
import sys
import pathlib
import common_code as cc

dirlist = os.listdir()
quality = f'{sys.argv[1]}'

cc.check_and_make(f'./sorted_{quality}_gff')
for f in dirlist:
    if f.startswith(quality) and f.endswith('.gff') :
        temp = []
        fl = cc.get_lines(f)
        for i in range(len(fl)):
            if len(fl[i]) > 1:
                temp.append(fl[i].split('\t'))
        sl = sorted(temp, key=lambda x: (x[0],int(x[3])))
        flat_lines = cc.flatten(sl)
        org_lines = cc.array2string(flat_lines)
        filepath = os.path.join(f'./sorted_{quality}_gff', f'sorted_{f}')
        cc.save_file(filepath,org_lines)