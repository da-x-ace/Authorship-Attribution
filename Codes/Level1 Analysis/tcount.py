import nltk

fp = open(r"train_alle","r")
myDict = {}
total_words = 0
for line in fp:
        words = line.split('\\')
        words = [word.strip(' ') for word in words]
        for word in words:
            if len(word) > 0:
                total_words = total_words+1
                if word in myDict:
                    myDict[word] = myDict[word]+1
                else:
                    myDict[word] = 1
								
#print len(myDict)
#print total_words
fp.close()


fp = open(r"test.arff", "w")
fp.write("@relation pos-feature\n")
fp.write("\n")
i = 1
for key,value in myDict.iteritems():
	fp.write("@attribute ")
	#fp.write(key)
	fp.write(str(i))
	i += 1
	fp.write(" REAL")
	fp.write("\n")

fp.write("\n")
fp.write("@attribute pos-feature {Positive, Negative}\n")
fp.write("\n")
fp.write("@data\n")
fp.write("\n")

fi = open(r'test_alle','r')
fi.seek(0,0)
t=[]
for line in fi:
        words = line.split('\\')
        words = [word.strip(' ') for word in words]
        t1 = nltk.Text(words)
        t.append(t1)

col = nltk.TextCollection(t)

fi.seek(0,0)

reviews_count=0

for element in t:
	for key,value in myDict.iteritems():
		fp.write(str(float(col.tf_idf(key, element)))+",")
	if(reviews_count < 27):
		fp.write("Positive\n")
	else:
		fp.write("Negative\n")
	reviews_count= reviews_count+1

reviews_count
fi.close()
fp.close()
