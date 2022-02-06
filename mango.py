import os
import shutil
from pathlib import Path
from traceback import print_tb

from numpy import sort

def getfilepath():
    home = os.path.expanduser("~")
    print(home)
    os.chdir(home)
    print(os.getcwd())
    os.chdir('Downloads')
    print(os.getcwd())

getfilepath()

file_list = ""

def checkfilesinpath():
    global file_list
    file_list = os.listdir(os.getcwd())
    print(file_list)

checkfilesinpath()

sortby = ""
folder = ""

def sortlogic():
    global sortby
    sortbyinput = input('Sort files containing: ')
    sortby = sortbyinput.lower()
    print(sortby)
    global folder
    folderinput = input('What folder would you like to sort these files into: ')
    folder = folderinput.lower()

sortlogic()

def checkfolderexists():
    if os.path.isdir(folder) == False:
        os.mkdir(folder)

def sortfiles():
    sortedfilescount = 0
    sortedfiles = ([x for x in file_list if sortby in x])
    for eachfile in sortedfiles:
        sortedfilescount = sortedfilescount + 1
    
    if sortedfilescount >= 1:
        os.mkdir(folder)
        shutil.move(eachfile, folder)
    else:
        print('No files containing:', sortby) 

sortfiles()