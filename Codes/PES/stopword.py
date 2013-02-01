import nltk
import operator
from collections import OrderedDict

def processString(myString):
	myString = myString.lower()
	myString = myString.translate(None,'\',;_*&^%#@!~`$<>?/\\')
	myString = myString.replace("(", " ( ")
	myString = myString.replace(")", " ) ")
	myString = myString.replace("[", " [ ")
	myString = myString.replace("]", " ] ")
	myString = myString.replace("{", " { ")
	myString = myString.replace("}", " } ")
	myString = myString.replace("-", " - ")
	myString = myString.replace('"', ' " ')
	return myString

fp = open(r'train','r')
outputfile_1 = open(r"train_processed","w")
for line in fp:
	newLine = processString(line)
	outputfile_1.write(newLine)

	
fp.close()
outputfile_1.close()
fp = open(r"stopwords","r")
myDict = {}
total_words = 0
for line in fp:
	words = line.split()
	for word in words:
		if len(word) > 0:
			total_words = total_words+1
			if word in myDict:
				myDict[word] = myDict[word]+1
			else:
				myDict[word] = 1
				

				
len(myDict)
total_words
fp.close()

#sorted_dict = sorted(myDict.iteritems(), key=operator.itemgetter(1))
#d_sorted_by_value = OrderedDict(sorted(myDict.items(), key=lambda x: x[1]))

i=0

fp = open(r"train.arff", "w")
fp.write("@relation unigram-feature\n")
fp.write("\n")
for key,value in myDict.iteritems():
	fp.write("@attribute ")
	fp.write(str(i))
	i=i+1
	fp.write(" REAL")
	fp.write("\n")

fp.close()
fp = open(r"train.arff", "a")
fp.write("\n")
fp.write("@attribute unigram-feature {Positive, Negative}\n")
fp.write("\n")
fp.write("@data\n")
fp.close()
fp = open(r"train.arff", "a")
fp.write("\n")
fi = open(r'train_processed','r')
fi.seek(0,0)
t=[]
for line in fi:
        t1 = nltk.Text(nltk.word_tokenize(line))
        t.append(t1)


col = nltk.TextCollection(t)

fi.seek(0,0)

reviews_count=0
for element in t:
        for key,value in myDict.iteritems():
                fp.write(str(float(col.tf_idf(key, element)))+",")
        if(reviews_count < 91):
                fp.write("Positive\n")
        else:
                fp.write("Negative\n")
        reviews_count= reviews_count+1



reviews_count
fi.close()
fp.close()

