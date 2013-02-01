'''
Code to generate POS tags for files and replace words with tag NNP
with keyword NNP.
 
Created on Nov 13, 2012

@author: Sarang Joshi

'''

import nltk

fnam = ['new_bh','new_jk','new_mw','new_pg','new_other']

for i in range(0,1):
    path = '/Users/Wolfie/Desktop/My Docs/SBU/SBU Courses/NLP/Project/Data/' + fnam[i] + '/'
    inputFNameTraining = path+'training.txt'
    outTraining = path+'training1.txt'
    
    f1 = open(inputFNameTraining,'r')
    f2 = open(outTraining,'w')
    
    print(inputFNameTraining)
    
    myList = []
    tempString = ""
    
    for line in f1:
        words = nltk.word_tokenize(line)
        myList = nltk.pos_tag(words)
        for element in myList:
            if element[1] == 'NNP':
                tempString = tempString+element[1]+" "
            else:
                tempString = tempString+element[0]+" "
                
        tempString.strip()
        f2.write(tempString)
        f2.write("\n")
        tempString=""
    
    f1.close()
    f2.close()
    
    inputFNameTraining = path+'test.txt'
    outTraining = path+'test1.txt'
        
    f3 = open(inputFNameTraining,'r')
    f4 = open(outTraining,'w')
    
    print(inputFNameTraining)
    
    myList = []
    tempString = ""
    
    for line in f3:
        words = nltk.word_tokenize(line)
        myList = nltk.pos_tag(words)
        for element in myList:
            if element[1] == 'NNP':
                tempString = tempString+element[1]+" "
            else:
                tempString = tempString+element[0]+" "
                
        tempString.strip()
        f4.write(tempString)
        f4.write("\n")
        tempString=""
    
    f3.close()
    f4.close()

print("DONE!!!!")
