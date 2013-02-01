'''
Main code to generate all training and test files in arff format
 
Created on Nov 13, 2012

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
        punctuation = re.compile(r'[-.?!,":;/<>()|0-9\'#@$%^*+]')
        for line in f1:      
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
                    if word not in dict_all:
                        dict_all[word] = 1
                    else:
                        dict_all[word] += 1
        
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
            
            '''    
            if(nGrams == 2):
                print('SARANG:dict_all\n')
                print(dict_all)
                print('SARANG:word_list2\n')
                print(word_list2)
                #t1 = nltk.Text(word_list2)
                #dict_for_each_review = {}
            '''
                
            for word in dict_all.keys():
                if (len(word_list2) != 0):
                    tfidf_value = collection.tf_idf(word, word_list2)
                    list.append(tfidf_value)
                else:
                    list.append(0.0) 
            
            '''Put Unk word for unknown words'''    
            countUnk = 0.0 
            
            '''
            for wordinreview in word_list2:
                if wordinreview not in dict_all:
                    countUnk += 1.0
            #list.append(float(countUnk))
            list.append(float(0.0))
            '''
                             
            if(countReviews < dsplitLocation):
                list.append('True')
            else:
                list.append('False')
            
            list_of_lists.append(list)
            countReviews += 1
        
        random.shuffle(list_of_lists)
        write_data_to_arff(trffFName,list_of_lists)
        f1.close()

'''function nltk_processing_for_trff(inputFName, trffFName, dict_all) ends here'''
    
'''main function calling'''
i = 1
dict_all = {}

'''Write training file'''
temp = ['new_bg','new_bh']
fnam = ['new_jk','new_mw','new_pg','new_other']
tr = [82,90,91,84]
testtt = [22,29,26,22]
for i in range(0,4):
    dict_all = {}
    path = '/Users/Wolfie/Desktop/My Docs/SBU/SBU Courses/NLP/Project/Data/' + fnam[i] + '/'
    inputFNameTraining = path+'training1.txt'
    trffFName = path+'unigram/arff_training1.arff'
    #inputFNameTraining = path+'trial_data/training'+str(i)+'.txt'
    #trffFName = path+'trial_data/arff_training'+str(i)+'.arff'
    print('SARANG - File namessss!!')
    print(inputFNameTraining)
    print(trffFName)
    print(tr[i])
    print(testtt[i])
    nltk_processing_for_training_trff(inputFNameTraining, trffFName, tr[i], dict_all, True, 1)
    
    ''' Now process test data '''
    inputFNameTest = path+'test1.txt'
    trffFName = path+'unigram/arff_test1.arff'
    #inputFNameTest = path+'trial_data/test'+str(i)+'.txt'
    #trffFName = path+'trial_data/arff_test'+str(i)+'.arff'
    nltk_processing_for_training_trff(inputFNameTest, trffFName, testtt[i], dict_all, False, 1)
    
    '''
    Bigram computation
    '''
    dict_all = {}
    trffFName = path+'bigram/arff_training1.arff'
    #trffFName = path+'trial_data/bigram_arff_training'+str(i)+'.arff'
    nltk_processing_for_training_trff(inputFNameTraining, trffFName, tr[i], dict_all, True, 2)
    
    '''Now process test data'''
    trffFName = path+'bigram/arff_test1.arff'
    #trffFName = path+'trial_data/bigram_arff_test'+str(i)+'.arff'
    nltk_processing_for_training_trff(inputFNameTest, trffFName, testtt[i], dict_all, False, 2)
    
    '''
    Trigram computation
    '''
    dict_all = {}
    trffFName = path+'trigram/arff_training1.arff'
    #trffFName = path+'trial_data/trigram_arff_training'+str(i)+'.arff'
    nltk_processing_for_training_trff(inputFNameTraining, trffFName, tr[i], dict_all, True, 3)
    
    '''Now process test data'''
    trffFName = path+'trigram/arff_test1.arff'
    #trffFName = path+'trial_data/trigram_arff_test'+str(i)+'.arff'
    nltk_processing_for_training_trff(inputFNameTest, trffFName, testtt[i], dict_all, False, 3)

print('CONGRATULATIONS - YOU ARE DONE!!')