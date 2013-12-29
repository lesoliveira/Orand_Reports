#!/usr/bin/python
# -*- encoding: iso-8859-1 -*-
# Esse programa recebe o arquivo resultado do SVM com classe e probabilidades
# e calcula a taxa de reconhecimento para verdadeiras e falsificasoes
# O arquivo de entrada tem 12000 linhas, 60 escritores * 5 referencias e 4 tipos de assinaturas
# verdadeira, e 3 falsificacoes
import sys
import os

def normalize(vet):

    sum = 0.0
    vetn = []
    for i in range(12):
        sum = sum + vet[i]

    for i in range(12):
        vetn.append(vet[i]/sum)

    return vetn

def maximo(v1, v2, v3):
	
	probs = []	
	for i in range (12):
		probs.append(max(v1[i], v2[i], v3[i]))
		
	return probs.index(max(probs))
	
def soma(v1, v2, v3):
		
	probs = []	
	for i in range (12):
		probs.append(v1[i]*v2[i]*v3[i])

	return probs.index(max(probs))

def media(v1, v2, v3):

		probs = []	
		for i in range (12):
			probs.append((v1[i]+v2[i]+v3[i])/3)

		return probs.index(max(probs))


def main(filename):

	fp12 = open('12')
	fp24 = open('24')
	fp36 = open('36')
	
	rec = 0 
	err = 0

	for i in range(400):
	
		line = fp12.readline()
		line = fp24.readline()
		line = fp36.readline()
		prob12 = []
		prob24 = []
		prob36 = []
		
		votes = [0,0,0,0,0,0,0,0,0,0,0,0]
		
		

		for j  in range(12):
			line = fp12.readline()
			l =	line.split()
			prob12.append(float(l[3]))

			line = fp24.readline()
			l =	line.split()
			prob24.append(float(l[3]))

			line = fp36.readline()
			l =	line.split()
			prob36.append(float(l[3]))

			
		line = fp12.readline()
		l = line.split()
		classe12 = int(l[3])
		
		line = fp24.readline()
		l = line.split()
		classe24 = int(l[3])
		
		line = fp36.readline()
		l = line.split()
		classe36 = int(l[3])		
		
		#print prob12
		out12 = prob12.index(max(prob12))
	
		
		#print prob24
		out24 = prob24.index(max(prob24))
	
		
		#print prob36
		out36 = prob36.index(max(prob36))
		
		
		votes[out12] = votes[out12] + 1 
		votes[out24] = votes[out24] + 1 
		votes[out36] = votes[out36] + 1
		
		decisao_votos = votes.index(max(votes))
		
		#if(decisao_votos == classe12):

		#	print 'Classe: ', classe12, votes, ' REC' 
		#	rec = rec+1
		#else:
		#	print 'Classe: ', classe12, votes, ' ERR' 
		#	err = err+1 
			
		#decisao_max =  maximo(prob12, prob24, prob36)
		decisao_max =  media(prob12, prob24, prob36)
		if(decisao_max == classe12):

			print 'Classe: ', classe12, decisao_max, ' REC' 
			rec = rec+1
		else:
			print 'Classe: ', classe12, decisao_max, ' ERR' 
			err = err+1
		
	print rec/400., err/400.
		
	fp12.close()
	fp24.close()
	fp36.close()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(" - Usage: sigver.py <file>")
    main(sys.argv[1])


