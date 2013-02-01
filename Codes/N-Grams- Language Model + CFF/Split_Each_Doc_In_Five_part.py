'''
Split the True and False files in to FIVE parts

Convention:
Paul Graham - True
Ben Hotowitz - False

Created on Nov 13, 2012

@author: Sarang Joshi

'''
ft = open('/Users/Wolfie/Desktop/My Docs/SBU/SBU Courses/NLP/Project/Data/Dec02/training1.txt', 'r')

ft1 = open('/Users/Wolfie/Desktop/My Docs/SBU/SBU Courses/NLP/Project/Data/Dec02/ft1.txt', 'w')
ft2 = open('/Users/Wolfie/Desktop/My Docs/SBU/SBU Courses/NLP/Project/Data/Dec02/ft2.txt', 'w')
ft3 = open('/Users/Wolfie/Desktop/My Docs/SBU/SBU Courses/NLP/Project/Data/Dec02/ft3.txt', 'w')
ft4 = open('/Users/Wolfie/Desktop/My Docs/SBU/SBU Courses/NLP/Project/Data/Dec02/ft4.txt', 'w')
ft5 = open('/Users/Wolfie/Desktop/My Docs/SBU/SBU Courses/NLP/Project/Data/Dec02/ft5.txt', 'w')

fd1 = open('/Users/Wolfie/Desktop/My Docs/SBU/SBU Courses/NLP/Project/Data/Dec02/fd1.txt', 'w')
fd2 = open('/Users/Wolfie/Desktop/My Docs/SBU/SBU Courses/NLP/Project/Data/Dec02/fd2.txt', 'w')
fd3 = open('/Users/Wolfie/Desktop/My Docs/SBU/SBU Courses/NLP/Project/Data/Dec02/fd3.txt', 'w')
fd4 = open('/Users/Wolfie/Desktop/My Docs/SBU/SBU Courses/NLP/Project/Data/Dec02/fd4.txt', 'w')
fd5 = open('/Users/Wolfie/Desktop/My Docs/SBU/SBU Courses/NLP/Project/Data/Dec02/fd5.txt', 'w')

i = 1
for line in ft:
    if (i < 19):
        ft1.write(line)
    elif (i < 37):
        ft2.write(line)
    elif (i < 55):
        ft3.write(line)
    elif (i < 73):
        ft4.write(line)
    elif (i < 91):
        ft5.write(line)
    elif (i < 137):
        fd1.write(line)
    elif (i < 183):
        fd2.write(line)
    elif (i < 228):
        fd3.write(line)
    elif (i < 275):
        fd4.write(line)
    elif (i < 324):
        fd5.write(line)
        
    i = i + 1

ft5.close()
ft4.close()
ft3.close()
ft2.close()
ft1.close()
fd5.close()
fd4.close()
fd3.close()
fd2.close()
fd1.close()
ft.close()

print('CONGRATULATIONS - YOU ARE DONE!!')