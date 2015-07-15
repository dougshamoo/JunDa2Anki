__author__ = 'dougs_000'
"""
A simple script for turning Junda's Chinese frequency list into an Anki deck.
"""

import csv
import codecs

junda = open("..\\junda10000-utf8.txt", "r")
anki_csv = open("..\\anki_junda.csv", "w")

for line in csv.reader(junda, delimiter= "\t"):
    hanzi = line[1]
    pinyin = line[4]
    if line[5] == '':
        meaning = '[Add meaning]'
    else:
        meaning = line[5]
    example = '[Add example]'
    anki_csv.write("{0}\t{1}\t{2}\t{3}\n".format(hanzi, pinyin, meaning, example))

junda.close()
anki_csv.close()
#anki_check = open("..\\anki_junda.csv", "r")
#for line in csv.reader(anki_check, delimiter="\t"):
#    print line