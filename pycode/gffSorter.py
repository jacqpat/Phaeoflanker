'''
Written by Patrick Jacques the 01 March 2022

post processing of the flanks gff files so that
genes are ordered on the 5' -> 3' orientation

python3 gffSorter.py [FOLDER2SORT]
'''
import os
import sys
import pathlib
import common_code as cc

dir2stock = f'{sys.argv[1]}sorted'
cc.check_and_make(dir2stock)

folder = f'{sys.argv[1]}'
for f in pathlib.Path(folder).iterdir():
    if f.is_file():
        current_name = os.path.basename(f.name)
        current_lines = cc.get_lines(f)
        for i in range(len(current_lines)):
            current_lines[i] = current_lines[i].split('\t')
        sort_lines = sorted(current_lines, key=lambda x: int(x[3]))
        flat_lines = cc.flatten(sort_lines)
        org_lines = cc.array2string(flat_lines)
        filepath = os.path.join(dir2stock, f'{current_name[:-4]}.gff')
        cc.save_file(filepath,org_lines)