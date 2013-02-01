'''
Generate the  training and test files from split files of reviews

Created on Nov 15, 2012

@author: Sarang Joshi

'''
ft1 = open('/Users/Wolfie/Desktop/My Docs/SBU/SBU Courses/NLP/Project/Data/authordetection/Data-2/train_bg', 'r')
ft2 = open('/Users/Wolfie/Desktop/My Docs/SBU/SBU Courses/NLP/Project/Data/authordetection/Data-2/train_bh', 'r')
ft3 = open('/Users/Wolfie/Desktop/My Docs/SBU/SBU Courses/NLP/Project/Data/authordetection/Data-2/train_jk', 'r')
ft4 = open('/Users/Wolfie/Desktop/My Docs/SBU/SBU Courses/NLP/Project/Data/authordetection/Data-2/train_mw', 'r')
ft5 = open('/Users/Wolfie/Desktop/My Docs/SBU/SBU Courses/NLP/Project/Data/authordetection/Data-2/train_pg', 'r')
ft6 = open('/Users/Wolfie/Desktop/My Docs/SBU/SBU Courses/NLP/Project/Data/authordetection/Data-2/train_others', 'r')

ftt1 = open('/Users/Wolfie/Desktop/My Docs/SBU/SBU Courses/NLP/Project/Data/authordetection/Data-2/test_bg', 'r')
ftt2 = open('/Users/Wolfie/Desktop/My Docs/SBU/SBU Courses/NLP/Project/Data/authordetection/Data-2/test_bh', 'r')
ftt3 = open('/Users/Wolfie/Desktop/My Docs/SBU/SBU Courses/NLP/Project/Data/authordetection/Data-2/test_jk', 'r')
ftt4 = open('/Users/Wolfie/Desktop/My Docs/SBU/SBU Courses/NLP/Project/Data/authordetection/Data-2/test_mw', 'r')
ftt5 = open('/Users/Wolfie/Desktop/My Docs/SBU/SBU Courses/NLP/Project/Data/authordetection/Data-2/test_pg', 'r')
ftt6 = open('/Users/Wolfie/Desktop/My Docs/SBU/SBU Courses/NLP/Project/Data/authordetection/Data-2/test_others', 'r')

Training1 = open('/Users/Wolfie/Desktop/My Docs/SBU/SBU Courses/NLP/Project/Data/new_bg/training1.txt', 'w')
Test1 = open('/Users/Wolfie/Desktop/My Docs/SBU/SBU Courses/NLP/Project/Data/new_bg/test1.txt', 'w')
Training2 = open('/Users/Wolfie/Desktop/My Docs/SBU/SBU Courses/NLP/Project/Data/new_bh/training1.txt', 'w')
Test2 = open('/Users/Wolfie/Desktop/My Docs/SBU/SBU Courses/NLP/Project/Data/new_bh/test1.txt', 'w')
Training3 = open('/Users/Wolfie/Desktop/My Docs/SBU/SBU Courses/NLP/Project/Data/new_jk/training1.txt', 'w')
Test3 = open('/Users/Wolfie/Desktop/My Docs/SBU/SBU Courses/NLP/Project/Data/new_jk/test1.txt', 'w')
Training4 = open('/Users/Wolfie/Desktop/My Docs/SBU/SBU Courses/NLP/Project/Data/new_mw/training1.txt', 'w')
Test4 = open('/Users/Wolfie/Desktop/My Docs/SBU/SBU Courses/NLP/Project/Data/new_mw/test1.txt', 'w')
Training5 = open('/Users/Wolfie/Desktop/My Docs/SBU/SBU Courses/NLP/Project/Data/new_pg/training1.txt', 'w')
Test5 = open('/Users/Wolfie/Desktop/My Docs/SBU/SBU Courses/NLP/Project/Data/new_pg/test1.txt', 'w')
Training6 = open('/Users/Wolfie/Desktop/My Docs/SBU/SBU Courses/NLP/Project/Data/new_other/training1.txt', 'w')
Test6 = open('/Users/Wolfie/Desktop/My Docs/SBU/SBU Courses/NLP/Project/Data/new_other/test1.txt', 'w')

data_truth1 = ft1.read()
ft1.close()
data_truth2 = ft2.read()
ft2.close()
data_truth3 = ft3.read()
ft3.close()
data_truth4 = ft4.read()
ft4.close()
data_truth5 = ft5.read()
ft5.close()
data_truth6 = ft6.read()
ft6.close()

data_deceptive1 = ftt1.read()
ftt1.close()
data_deceptive2 = ftt2.read()
ftt2.close()
data_deceptive3 = ftt3.read()
ftt3.close()
data_deceptive4 = ftt4.read()
ftt4.close()
data_deceptive5 = ftt5.read()
ftt5.close()
data_deceptive6 = ftt6.read()
ftt6.close()

Training1.write(data_truth1+data_truth2+data_truth3+data_truth4+data_truth5+data_truth6)
Training1.close()

Test1.write(data_deceptive1+data_deceptive2+data_deceptive3+data_deceptive4+data_deceptive5+data_deceptive6)
Test1.close()

Training2.write(data_truth2+data_truth1+data_truth3+data_truth4+data_truth5+data_truth6)
Training2.close()

Test2.write(data_deceptive2+data_deceptive1+data_deceptive3+data_deceptive4+data_deceptive5+data_deceptive6)
Test2.close()

Training3.write(data_truth3+data_truth2+data_truth1+data_truth4+data_truth5+data_truth6)
Training3.close()

Test3.write(data_deceptive3+data_deceptive2+data_deceptive1+data_deceptive4+data_deceptive5+data_deceptive6)
Test3.close()

Training4.write(data_truth4+data_truth2+data_truth3+data_truth1+data_truth5+data_truth6)
Training4.close()

Test4.write(data_deceptive4+data_deceptive2+data_deceptive3+data_deceptive1+data_deceptive5+data_deceptive6)
Test4.close()

Training5.write(data_truth5+data_truth2+data_truth3+data_truth4+data_truth1+data_truth6)
Training5.close()

Test5.write(data_deceptive5+data_deceptive2+data_deceptive3+data_deceptive4+data_deceptive1+data_deceptive6)
Test5.close()

Training6.write(data_truth6+data_truth2+data_truth3+data_truth4+data_truth5+data_truth1)
Training6.close()

Test6.write(data_deceptive6+data_deceptive2+data_deceptive3+data_deceptive4+data_deceptive5+data_deceptive1)
Test6.close()

print('CONGRATULATIONS - YOU ARE DONE!!')