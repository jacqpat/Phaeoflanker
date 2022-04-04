'''
Written by Patrick Jacques the 01 March 2022

FOR ALL THE FLANKS GFF IN A FOLDER get : 
    the size of the contig
    the number of genes, the number of gene per
    nucleic base, and the number of viral genes
And resume it all in one matrix

python3 mkrMatrix4gff.py [FOLDER] [SAVE_FOLDER]
'''
import re
import os
import sys
import pathlib
import common_code as cc

def sort_file(filepath):
    sort2 = open(filepath,'r+')
    line2sort = sort2.readlines()
    line2sort.sort(key=lambda test_string : list(
    map(int, re.findall("contig(.*?)\:", test_string)))[0])
    srted = cc.array2string(line2sort)
    sort2.seek(0)
    sort2.write(srted)
    sort2.truncate()
    sort2.close()

cc.check_and_make('./matrices')

folder = sys.argv[1]
matrix = []
for f in pathlib.Path(folder).iterdir():
    if f.is_file():
        row = []
        g_nbr = 0
        g_vir = 0
        g_frac = 0
        filename = os.path.basename(f.name)
        start = int(re.search("\:(.*?)\-",filename).group(1))
        end = int(re.search("[0-9]\-(.*?)\_",filename).group(1))
        pos = re.search(f"{end}_(.*?).gff$",filename).group(1)
        length = end - start
        file_lines = cc.get_lines(f)
        for line in file_lines:
            split_line = line.split('\t')
            if 'mRNA_viral' in split_line[2]:
                g_nbr +=1
                g_vir += 1
            elif 'mRNA_' in split_line[2]:
                g_nbr += 1
        g_frac = round((g_nbr/length)*1000,2)
        row.append(f'{filename[:-4]}\t')
        row.append(f'{str(length)}\t')
        row.append(f'{str(g_nbr)}\t')
        row.append(f'{str(g_frac)}\t')
        row.append(f'{str(g_vir)}\n')
        matrix.append(row)
flat_mtrx = cc.flatten(matrix)
writ_mtrx = cc.array2string(flat_mtrx)
cc.save_file(sys.argv[2],writ_mtrx)
sort_file(sys.argv[2])