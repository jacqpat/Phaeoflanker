'''
Written by Patrick Jacques the 22/02/2022

python3 getEVEs_sequences.py [GFF_PATH] [WINDOW_SIZE] [TXT SIZES] [GFF_NAME] [PARAM]
'''
import os
import sys
import common_code as cc

def writeFile(naming_scheme,dictionary,status):
    if status == 'flank':
        f = open(f'BED/FLANKS_of_{sys.argv[5]}_{naming_scheme}_{sys.argv[2]}.bed','w')
        for key,value in dictionary.items():
            f.write(f'{key}\t{value["start_upstream"]}\t{value["end_upstream"]}\n{key}\t{value["start_downstream"]}\t{value["end_downstream"]}\n')
    else :
        f = open(f'BED/EVEs_of_{naming_scheme}.bed','w')
        for key,value in dictionary.items():
            f.write(f'{key}\t{value["start"]}\t{value["end"]}\n')
    f.close()

def getEVE_StartEnd(gff,key):
    '''
    Written as it is, this mean the gff given was already
    filtered to only keep genes from the same contig
    '''
    s = []
    e = []
    for g in gff:
        g = g.split("\t")
        if g[0] == key:
            s.append(int(g[3]))
            e.append(int(g[4]))
    Min = min(s)
    Max = max(e)
    return Min,Max

def removeLineBreaks(arr):
    for i in range(len(arr)):
        arr[i] = arr[i].replace("\n", "")
    arr = list(filter(lambda x: x != "", arr))
    return arr

cc.check_and_make('./BED')
window_size = int(sys.argv[2])

genes = cc.get_lines(sys.argv[1])
genes = removeLineBreaks(genes)

ctg_sizes = cc.get_lines(sys.argv[3])
ctg_sizes = removeLineBreaks(ctg_sizes)

contigs = []
for x in genes:
    g = x.split("\t")
    contigs.append(g[0])
set_contigs = set(contigs)
dict_eves = {el:{'start':0,'end':0} for el in set_contigs}
dict_flanks = {el:{'start_upstream':0,'end_upstream':0,'start_downstream':0,'end_downstream':0} for el in set_contigs}

for el in dict_eves:
    start = 0
    end = 0
    start,end = getEVE_StartEnd(genes,el)
    dict_eves[el]['start'] = start
    dict_eves[el]['end'] = end

for el in dict_flanks:
    dict_flanks[el]['end_upstream'] = dict_eves[el]['start'] 
    dict_flanks[el]['start_upstream'] = dict_flanks[el]['end_upstream'] - window_size
    if dict_flanks[el]['start_upstream'] < 0:
        dict_flanks[el]['start_upstream'] = 0
    dict_flanks[el]['start_downstream'] = dict_eves[el]['end']
    dict_flanks[el]['end_downstream'] = dict_flanks[el]['start_downstream'] + window_size

for z in ctg_sizes:
    sz = z.split("\t")
    if sz[0] in set_contigs:
        if dict_flanks[sz[0]]['end_downstream'] > int(sz[1]):
            dict_flanks[sz[0]]['end_downstream'] = int(sz[1])

naming_scheme = f"{sys.argv[4][:-4]}"
writeFile(naming_scheme,dict_eves,'eve')
writeFile(naming_scheme,dict_flanks,'flank')