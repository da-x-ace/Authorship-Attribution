#! /usr/bin/env python
#-1 3:1 11:1 14:1 19:1 39:1 42:1 55:1 64:1 67:1 73:1 75:1 76:1 80:1 83:1 

fi = open('train_bh','r')

linecount = 0

for line in fi:	
	linecount += 1
	fo = open('bh/'+str(linecount),'w')
	fo.write(line)
	fo.close()
fi.close()

fi = open('train_jk','r')

linecount = 0

for line in fi:	
	linecount += 1
	fo = open('jk/'+str(linecount),'w')
	fo.write(line)
	fo.close()
fi.close()

fi = open('train_mw','r')

linecount = 0

for line in fi:	
	linecount += 1
	fo = open('mw/'+str(linecount),'w')
	fo.write(line)
	fo.close()
fi.close()

fi = open('train_others','r')

linecount = 0

for line in fi:	
	linecount += 1
	fo = open('others/'+str(linecount),'w')
	fo.write(line)
	fo.close()
fi.close()

fi = open('train_pg','r')

linecount = 0

for line in fi:	
	linecount += 1
	fo = open('pg/'+str(linecount),'w')
	fo.write(line)
	fo.close()
fi.close()
