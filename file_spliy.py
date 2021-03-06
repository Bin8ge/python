# -*- coding: cp936 -*-
import os
import time

def mkSubFile(lines,srcName,sub, head = ''):
    [des_filename, extname] = os.path.splitext(srcName)
    filename  = des_filename + '_' + str(sub) + extname
    print( 'make file: %s' %filename)
    fout = open(filename,'w')
    try:
        #fout.writelines([head])
        fout.writelines(lines)
        return sub + 1
    finally:
        fout.close()

def splitByLineCount(filename,count):
    fin = open(filename,'r')
    try:
        #head = fin.readline()
        buf = []
        sub = 1
        for line in fin:
            buf.append(line)
            if len(buf) == count:
                sub = mkSubFile(buf,filename,sub)
                buf = []
        if len(buf) != 0:
            sub = mkSubFile(buf,filename,sub)
    finally:
        fin.close()

if __name__ == '__main__':
    begin = time.time()
    splitByLineCount('F:/qq????/qq.txt',50000000)
    end = time.time()
    print('time is %d seconds ' % (end - begin))