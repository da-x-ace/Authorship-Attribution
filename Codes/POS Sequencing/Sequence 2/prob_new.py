import nltk
import codecs
import sys
from nltk import bigrams
from nltk import trigrams


def processString(myString):
	myString = myString.lower()
	myString = myString.translate(None,'\'",;-)(*&^%#@!~`[]{}:<>?/\\')
	myString = myString.replace(".", " ")
	myString = myString.replace("$ ", " $ ")
	myString = myString.replace(" $", " $ ")
	return myString


def unigram_equivalent(path):
        fp = open(path, 'r')
        nestedDict = {}
        total_words = 0
        for line in fp:
                words = line.split()
                for word in words:
                        total_words = total_words+1
                        if word in nestedDict:
                                nestedDict[word] = nestedDict[word]+1
                        else:
                                nestedDict[word]=1


        fp.close()
        fp = open(r"train.arff","w")
        fp.write("@relation bigram-feature\n")
        fp.write("\n")
        for key,value in nestedDict.iteritems():
                fp.write("@attribute ")
                fp.write(key)
                fp.write(" REAL")
                fp.write("\n")
        fp.write("\n")
        fp.write("@attribute bigram-feature {Positive, Negative}\n")
        fp.write("\n")
        fp.write("@data\n")
        fp.write("\n")
        fi = open(path, 'r')
        t=[]
        for line in fi:
                t1= nltk.Text(nltk.word_tokenize(line))
                t.append(t1)

        col = nltk.TextCollection(t)

        fi.seek(0,0)

        reviews_count =0

        for element in t:
                for key,value in nestedDict.iteritems():
                        fp.write(str(float(col.tf_idf(key,element)))+",")
                if(reviews_count < 91):
                        fp.write("Positive\n")
                else:
                        fp.write("Negative\n")
                reviews_count = reviews_count + 1


        fi.close()
        fp.close()

        
                


fp = open(r'train','r')
outputfile_1 = open(r"train_processed","w")
for line in fp:
	newLine = processString(line)
	outputfile_1.write(newLine)

	
fp.close()
outputfile_1.close()


fp = open(r'train_processed','r')
fo = open(r'pos_input','w')

myList = []
tempString = ""

for line in fp:
    words = nltk.word_tokenize(line)
    myList = nltk.pos_tag(words)
    for element in myList:
        tempString= tempString+element[1]+" "
    tempString.strip()
    fo.write(tempString)
    fo.write("\n")
    tempString=""

fp.close()
fo.close()

fp = open(r'pos_input','r')

myDict={}
total_words = 0
dictIndex=1

fp.seek(0,0)
for line in fp:
        tokens = line.split()
        for data in bigrams(tokens):
                total_words = total_words+1
                if data in myDict:
                        myDict[data] = dictIndex
                else:
                        myDict[data]=dictIndex
                dictIndex = dictIndex +1


fp.close()

#dictIndex = {}
#dictId = 1

#for key,value in myDict.iteritems():
#        dictIndex[key] = dictId
#        dictId = dictId + 1

fp = open(r'pos_input','r')
fo = open(r'pos_indexed','w')

tempString = ""

for line in fp:
        tokensNew = line.split()
        for data in bigrams(tokensNew):
                tempString=tempString+str(myDict[data])+" "
        tempString = tempString.strip()
        fo.write(tempString)
        fo.write("\n")
        tempString = ""

fp.close()
fo.close()

unigram_equivalent(r'pos_indexed')


