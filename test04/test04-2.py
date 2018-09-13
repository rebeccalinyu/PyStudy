import os

os.chdir('d:\python\project\data\chapter3')

data = open('testdata.txt')

for each_line in data:

    print(each_line, end='')

data.close()