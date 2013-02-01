#! /usr/bin/env python
#-1 3:1 11:1 14:1 19:1 39:1 42:1 55:1 64:1 67:1 73:1 75:1 76:1 80:1 83:1 

import sys
from nltk.tokenize import word_tokenize

fi = open(str(sys.argv[1]),'r')
fo = open(str(sys.argv[2]),'w')
pcount = 0
#terms = ''



for line in fi:	
	tags = word_tokenize(line)
	#print tags
	if (len(tags) == 0):
		fo.write(str(pcount) + '\n')
#		fo.write(terms + '\n')
#		terms = ''
		pcount = 0
		continue
	for i in xrange(len(tags)):
		if(tags[i] == '('):
			pcount += 1
		#elif(tags[i] == ')'):
		#	pcount -= 1
		#elif(pcount > 1 and pcount < 4):
		#	if(tags[i] == ':' or tags[i] == '``' or tags[i] == '.' or tags[i] == '\'\'' or tags[i] == ',' or tags[i] == '?' or tags[i] == '--'):
		#		if(tags[i-1] == 'PUNC'):
		#			continue
		#		tags[i] = 'PUNC'
		#	terms += str(tags[i])
		#	terms += ' '
fi.close()
fo.close()
