#! /usr/bin/env python

import sys

fo = open('pg/pg.tc','w')
terms = ''

print len(sys.argv)

for i in range(1,len(sys.argv)):
	fi = open(str(sys.argv[i]),'r')
	for f in fi:
		terms += str(f).rstrip() + '\\\\ '
	fi.close()
	fo.write(terms+'\n')
fo.close()
