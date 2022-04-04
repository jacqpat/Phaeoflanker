'''
Written by Patrick Jacques the 14/03/22

regroup common functions used in at least
two other scripts.
'''
import os

def check_and_make(foldername):
    ''' if a folder with that name does not exist : create it'''
    if not os.path.exists(foldername):
        os.makedirs(foldername)

def flatten(t):
    ''' turn a list of lists into a simple list '''
    return [item for sublist in t for item in sublist]

def get_lines(namefile):
    ''' get all the lines within a file '''
    f = open(namefile, "r")
    l = f.readlines()
    f.close()
    return l

def save_file(filepath,bigBadString):
    ''' save a prepared string within a file '''
    save = open(filepath,"w")
    save.write(bigBadString)
    save.close()

def array2string(l,str2start = ''):
    ''' transform a list into a string '''
    strn = f'{str2start}'
    for e in l:
        if e[-1] == "\n":
            strn += e
        else:
            strn += e + '\t'
    return strn

def stripNewLine(list):
    ''' get rid of newline at the end of string '''
    for i in range(len(list)):
        list[i] = list[i].rstrip("\n")
    return list

def removeLineBreaks(arr):
    ''' get rid of every new line in a string '''
    for i in range(len(arr)):
        arr[i] = arr[i].replace("\n", "")
    arr = list(filter(lambda x: x != "", arr))
    return arr

def get_contigs(parameter):
    if parameter == "provirus":
        lines = get_lines("contigs/contigs_provirus.txt")
    elif parameter == "maybe":
        lines = get_lines("contigs/contigs_maybe.txt")
    else :
        lines = get_lines('contigs/contigs_good.txt')
    lines = stripNewLine(lines)
    return lines