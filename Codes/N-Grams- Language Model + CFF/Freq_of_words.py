'''
Main code to generate all training and test files in arff format
 
Created on Dec 15, 2012

@author: Sarang Joshi

'''

import nltk
from nltk import bigrams
from nltk import trigrams
import codecs
import random
import re
import nltk.corpus
from operator import itemgetter

def write_attr_to_arff(filename, relation_name, attribute_list):
    file=codecs.open(filename,encoding='utf-8',mode='w')
    file.write('@RELATION ' + relation_name + '\n\n')  
    
    print('writing attributes...\n')
    
    for attribute in attribute_list:
        file.write('@ATTRIBUTE '+str(attribute)+' NUMERIC'+'\n')
    
    #file.write('@ATTRIBUTE '+'UNK'+' NUMERIC'+'\n')
    file.write('@ATTRIBUTE '+relation_name+' {True, False}' + '\n\n')
    file.close()
    
def write_data_to_arff(filename, tdidf_val_list_of_list):
    file=codecs.open(filename,encoding='utf-8',mode='a')
    file.write('@DATA\n\n')
    
    print('writing td-idf...\n')
    
    for list in tdidf_val_list_of_list:
        #print('list - '+str(len(list)))
        for ele in list:
            if ele not in ['True','False']:
                file.write(str(ele)+',')
            else:
                file.write(ele+'\n')
    
    file.close()
                
def nltk_processing_for_training_trff(inputFName, trffFName, dsplitLocation, dict_all, IsTraining, nGrams):
        print('running nGrams = '+str(nGrams)+'on File - '+inputFName + '\n')
        
        nltk_review_array = []
        f1=open(inputFName,'r')
        
        print('preparing dictionary for all the words...')    
        punctuation = re.compile(r'[\',/<>()|0-9\#@$%^*+]')

#Punctuation not considered - "'-.!:;?'"
        temp_dict = {}
        temp_dict1 = {}
        temp_dict2 = {}
        nline = 0
        for line in f1:   
            nline += 1
            line = punctuation.sub("", line)
            if (nGrams == 1):
                word_list2 = nltk.word_tokenize(line)
            elif (nGrams == 2):
                token_list = bigrams(nltk.word_tokenize(line))
                word_list2 =  [''.join(token).lower() for token in token_list]
            elif (nGrams == 3):
                token_list = trigrams(nltk.word_tokenize(line))
                word_list2 =  [''.join(token).lower() for token in token_list]
                
            nltk_review_array.append(word_list2)
            if IsTraining == True:
                for word in word_list2: 
                    if nline < dsplitLocation:                
                        if word not in temp_dict:
                            temp_dict[word] = 1
                        else:
                            temp_dict[word] += 1
                    else:
                        if word not in temp_dict1:
                            temp_dict1[word] = 1
                        else:
                            temp_dict1[word] += 1
          
        '''Frequency of words logic:
                We take the common features between two authors. Here we store
                features of each author in separate dictionaries and then take
                intersection of two dictionaries.'''  
        if IsTraining == True:              
            for k,v in temp_dict.iteritems():
                if k in temp_dict1:
                    temp_dict2[k] = v
            
            for k,v in temp_dict2.iteritems():
                dict_all[k] = v
                    
        #print(dict_all)
        #print('Before sorting\n')
        #print(dict_all)
        sorted(dict_all.iterkeys())
        #print('After sorting\n')
        #print(dict_all)
        '''Write attributes to the file'''
        write_attr_to_arff(trffFName, 'relation-sent-analysis', dict_all)
        #print('After function call\n')
        #print(dict_all)
        collection = nltk.TextCollection(nltk_review_array)
        
        '''Compute the tf-idf now'''
        f1.seek(0,0)
        list_of_lists = []
        countReviews = 1
        
        print("Computing tf_idf...\n")
        for line1 in f1:
            list = []
            line1 = punctuation.sub("", line1)

            if (nGrams == 1):
                word_list2 = nltk.word_tokenize(line1)
            elif (nGrams == 2):
                token_list = bigrams(nltk.word_tokenize(line1))
                word_list2 =  [''.join(token).lower() for token in token_list]
            elif (nGrams == 3):
                token_list = trigrams(nltk.word_tokenize(line1))
                word_list2 =  [''.join(token).lower() for token in token_list]
                
            for word in dict_all.keys():
                if (len(word_list2) != 0):
                    tfidf_value = collection.tf_idf(word, word_list2)
                    list.append(tfidf_value)
                else:
                    list.append(0.0) 
            
            '''Put Unk word for unknown words'''    
            countUnk = 0.0
                             
            if(countReviews < dsplitLocation):
                list.append('True')
            else:
                list.append('False')
            
            list_of_lists.append(list)
            countReviews += 1
        
        random.shuffle(list_of_lists)

        write_data_to_arff(trffFName,list_of_lists)
        f1.close()
    
'''main function calling'''
i = 1
dict_all = {}

'''Write training file'''
fnam = ['pg-jk','pg-mw','pg-bh','jk-mw','jk-bh']
tr = [90,90,90,81,81]
testtt = [25,25,25,21,21]
for i in range(0,1):
    dict_all = {}
    path = '/Users/Wolfie/Desktop/My Docs/SBU/SBU Courses/NLP/Project/Data/new_pg_freq/'
    inputFNameTraining = path+'training1-jk-bh.txt'
    trffFName = path+'unigram/arff_training1-jk-bh.arff'
    #inputFNameTraining = path+'trial_data/training'+str(i)+'.txt'
    #trffFName = path+'trial_data/arff_training'+str(i)+'.arff'
    nltk_processing_for_training_trff(inputFNameTraining, trffFName, 82, dict_all, True, 1)
    
    ''' Now process test data '''
    inputFNameTest = path+'test1-jk-bh.txt'
    trffFName = path+'unigram/arff_test1-jk-bh.arff'
    #inputFNameTest = path+'trial_data/test'+str(i)+'.txt'
    #trffFName = path+'trial_data/arff_test'+str(i)+'.arff'
    nltk_processing_for_training_trff(inputFNameTest, trffFName, 22, dict_all, False, 1)
    
''' 
print('CONGRATULATIONS - YOU ARE DONE!!')