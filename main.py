#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pprint import pprint
import tltk
import os.path

def readData(file):
    Mfile = open(file, 'r')
    text = Mfile.read().strip()
    Mfile.close()
    return text

def segmentText(text):
    return tltk.nlp.word_segment(text)

def generatePosTag(text):
    return tltk.nlp.pos_tag(text)

def writeFile(filename, text):
    f = open(filename, "w")
    f.write(text)
    f.close()

def writeList(filename, myList):
    f = open(filename, "w")
    for item in myList:
        f.write("%s\n" % item)

data = readData('my_file.txt')
splited_text = segmentText(data)
pos_text = generatePosTag(data)

print('\n')
pprint(splited_text)
print('\n')

print('\n')
pprint(pos_text)
print('\n')

writeFile('segmentation.txt',splited_text)
writeList('posTagging.txt',pos_text)