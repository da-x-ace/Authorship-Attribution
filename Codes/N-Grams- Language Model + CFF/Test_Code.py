'''
Main code to generate all training and test files in arff format
 
Created on Sep 13, 2012

@author: Sarang Joshi

'''
import nltk
import re
from operator import itemgetter

'''
f = open("/Users/Wolfie/Desktop/My Docs/SBU/SBU Courses/NLP/Project/Data/authordetection/Data/train_pg", 'r')
'''

f = open("/Users/Wolfie/Desktop/My Docs/SBU/SBU Courses/NLP/Project/Data/Nov19/training1.txt", 'r')
fw = open("/Users/Wolfie/Desktop/My Docs/SBU/SBU Courses/NLP/Project/Data/Nov19/dict_output.txt", 'w')
punctuation = re.compile(r'[-.?!,":;/<>()|0-9\'#@$%^*+]')    
            
list = []
myList = []
dict = {}
dict_false = {}
linecnt = 0
for line in f:
    linecnt += 1
    line = punctuation.sub("", line)
    list = nltk.word_tokenize(line)
    myList = nltk.pos_tag(list)
    for element in myList:
        if element[1] != 'NNP':
            if element[0] != 'the':
                if linecnt < 91:
                    if element[0] not in dict:
                        dict[element[0]] = 1
                    else:
                        dict[element[0]] += 1
                else:
                     if element[0] not in dict_false:
                        dict_false[element[0]] = 1
                     else:
                        dict_false[element[0]] += 1

print('***********searching in dictionary***************\n')   
print(sorted(dict.items(), key=itemgetter(1)))
print('*************false data***********\n')
print(sorted(dict_false.items(), key=itemgetter(1)))
'''             
count = 0     
for ele in dict:
    if dict[ele] > count:
        strtmp = ele
        count = dict[ele]
'''
#print(strtmp)
#print(count)        
#print('SARANG:string = ' + strtmp + 'count=' + str(count)) 

fw.close()       
f.close()
print('CONGRATULATIONS - YOU ARE DONE!!')