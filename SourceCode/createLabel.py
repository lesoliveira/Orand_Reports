import os

fname = []
labels = []
fp = open('labels.txt')
month = ['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre' ]

linha  = fp.readline()
while linha:
	l = linha.split()
	l1 = l[0].split('/')
	fname.append(l1[2])
	labels.append(l[1])
	linha =  fp.readline()
	print linha

for filename in os.listdir('./data/otsu/'):
	print filename
	ind = fname.index(filename)
	print labels[ind], ind
	fileout = filename.split('.')
	fileout = './data/inf/' + fileout[0] + '.inf'
	fout = open(fileout, 'w')
	m_lowercase = (labels[ind]).lower()
	index = month.index(m_lowercase)
        fout.write( '%d|%s|' % (index, labels[ind]) )

	fout.close()

fp.close()
