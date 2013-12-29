#!/usr/bin/python
# coding: utf-8


import sys
import string
from os import listdir
from os.path import isfile, join
import numpy as np

def getlabel(img_path,vet,char_conta):
    
    all_char = 'enrofbmazilyjugstpENROFBMAZILYJUGSTP'


    name =  img_path.split('.')
    label_name = './orand/inf/' + img_path
    fp = open(label_name)
    line = fp.readline()
    
    label = line.split('|')
    
    for i in range (len(label[1])):
        if ( label[1][i] in all_char):
            ind = all_char.index(label[1][i])
            char_conta[ind] = char_conta[ind] + 1
        else:
            print 'Caracter nao encontrado: ', label[1][i]
    
    print label
    vet[int(label[0])] = vet[int(label[0])] +1
    fp.close
    return int(label[0])




if __name__ == "__main__":

    if len(sys.argv) != 2:
        sys.exit(" - Usage: cropfile")
    
    vet = [0,0,0,0,0,0,0,0,0]
    lab = []
    img = []

    char_conta = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

    onlyfiles = [ f for f in listdir(sys.argv[1]) if isfile(join(sys.argv[1],f)) ]
    for i in onlyfiles:
        #print i
        label = getlabel(i,vet, char_conta)

        img.append(i)
        lab.append(label)



#for i in range(9):
#        conta = 1
#        for j in range(len(lab)):
#            if(lab[j] == i):
#                conta = conta +1
#                if(conta >= vet[i] * .8 ):
#                    print img[j]


    print sum(vet)
    print char_conta










