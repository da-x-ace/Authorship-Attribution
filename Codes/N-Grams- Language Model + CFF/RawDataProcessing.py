'''
Generate the  training and test files from split files of reviews

Created on Sep 15, 2012

@author: Sarang Joshi

'''
p = '/Users/Wolfie/Desktop/My Docs/SBU/SBU Courses/NLP/Project/Data/authordetection/document_Josh_Kopelman/'

path = p + 'documents_1.txt'
f2 = open(path, 'a')
'''
for i in range(1,26):    
    path = p + 'rawdata/p' + str(i) + '.txt'
    print('processing' + path)
    f1 = open(path, 'r')
    data = f1.read().replace('\n', ' ') + '\n'
    f2.seek(2)
    f2.write(data)
    f1.close()
    
for i in range(1,26):    
    path = p + 'rawdata/w' + str(i)
    print('processing' + path)
    f1 = open(path, 'r')
    data = f1.read().replace('\n', ' ') + '\n'
    f2.seek(2)
    f2.write(data)
    f1.close()
'''
for i in range(1,2):    
    path = p + 'documents.txt'
    print('processing' + path)
    f1 = open(path, 'r')
    '''data = f1.read().replace('\n', ' ') + '\n' '''
    data = f1.read().replace('###################', '\n')
    f2.seek(2)
    f2.write(data)
    f1.close()
        
f2.close()
        
print('CONGRATULATIONS - YOU ARE DONE!!')