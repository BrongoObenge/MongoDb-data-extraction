#!/usr/bin/python2.7
__author__ = 'j'
from manager import MongoDbManager
import sys
import re
from ConfigParser import SafeConfigParser
conf=SafeConfigParser()
conf.readfp(open('manager/Config.conf'))

mongoManager = MongoDbManager.MongoDbManager()
client = mongoManager.openDb()

hardwarePool = [
    'GRAPHICSCARD',
    'PROCESSOR',
    'MEMORY',
    'HDD',
    'SSD',
    'SOUNDCARD',
    'OPTICALDRIVE',
    'PSU',
    'MOTHERBOARD',
    'CASE',
]
for x in range(len(hardwarePool)):
    coll = client['Hardware'][hardwarePool[x]]
    cursor =  coll.find()
    collLength = coll.count()

    pat1 = r'\"_id\":.ObjectId\(((.)+)\"\)'
    pat2 = r'(\\\\r\\\\n)'
    pat3 = r'(\\\\r\\\\n)'
    pat4 = r"(\\\\u2022\W)"
    pat5 = r'(\"\[\"\\?\"?)'
    pat6 = r'(\"]\"?)'
    pat7 = r'(\, })'
    pat8 = r'(u\\)'
    pat9 = r'(\"\"(?![,]))'
    pat10 = r'(,\s,)'
    pat11 = r'(\\\\xef)'
    pat12 = r'(,\W\"Bijzonderheden\":.+)\}'
    pat13 = r'("Golden\WSample")'
    pat14 = r'(D410",\W"",)'
    pat15 = r'(2.5")'
    pat16 = r'("",)'
    pat17 = r'("3.5")'
    pat18 = r'("3.5,\W")'
    pat19 = r'("2.5,\W")'
    pat20 = r'\((3.5")\)'
    pat21 = r'("5.25")'
    pat22 = r'("5.25,\W")'
    pat23 = r'("19")'
    pat24 = r'("19,\W")'
    pat25 = r'(\W3.5")'
    pat26 = r'2.5",\W"'
    pat27 = r'(3.5,\W")'
    pat28 = r'("Inter-Tech\W19")'
    pat29 = r'(3582,5,\W")'
    pat30 = r'(:\W\W3.5",\W")'
    pat31 = r'(5.25",\W5.25",)'
    pat32 = r'(2-140mm",\W"1x)'
    pat33 = r'(0421342,5,\W")'
    pat34 = r'(jde",\W"Aan)'
    pat35 = r'(:\W""2.5")'
    pat36 = r'(":\W"2.5"",)'
    pat37 = r'(\W2,5"",)'
    pat38 = r'(\W2.5"",)'
    pat39 = r'(Intel 530 2,5"\W)'
    pat40 = r'(Toshiba\W2.5"\W)'
    pat41 = r'(DC\W2.5"\WS37)'
    pat42 = r'("1,8"\WSlim")'
    pat43 = r'(":\W"1.8"",)'
    pat44 = r' 2.5"\WS'
    pat45 = r' 2.5"\WM'
    pat46 = r'(":\W"3.5"",)'
    pat47 = r'(TA\W2.5"\W)'
    pat48 = r'(\W\(2,5"\)",)'
    pat49 = r'(\W\(1,8"\)",)'
    pat50 = r'(6\W2,5"\W)'
    pat51 = r'(S\W3.5"\W)'
    pat52 = r'(s\W3.5"\W)'
    pat53 = r'(end\W2.5"\W)'
    pat54 = r'(C300\W2.5"\W)'
    pat55 = r'(a\W1.8")'
    pat56 = r'(A\W1.8")'
    pat57 = r'(C\W2,5")'
    pat58 = r'(end\W1"\W)'
    pat59 = r'(SSD\W2.5"\W\()'
    pat60 = r'(C\W1.8"\WS)'
    pat61 = r'(D\W2,5"\W)'
    pat62 = r'(SATA2\W2.5"\W)'
    pat63 = r'(SATA\W3.5"\W)'
    pat64 = r'(SAS\W2.5"\W)'
    pat65 = r'(IBM\W1.8"\W)'
    pat66 = r'("HP\W2.5"\W)'
    pat67 = r'(FDE\W2.5"\W)'
    try:
        location = sys.argv[1]
    except:
        location = hardwarePool[x]+'.json'

    f = open(location, 'w')
    f.write("[")
    index = 0
    while cursor.alive:
       index += 1

       try:
           line = str(cursor.next()).replace("\'", "\"")
           line = line.replace("u\"", "\"")
           try:
               line = re.sub(pat1, "", line)
               line = re.sub(pat2, "", line)
               line = re.sub(pat3, "", line)
               line = re.sub(pat4, "", line)
               line = re.sub(pat5, '"', line)
               line = re.sub(pat6, '"', line)
               line = re.sub(pat7, ' }', line)
               line = re.sub(pat8, "", line)
               line = re.sub(pat9, ", \n", line)
               line = re.sub(pat10, ",", line)
               line = re.sub(pat11, "i", line)
               line = re.sub(pat12, "}", line)
               line = re.sub(pat13, "", line)
               line = re.sub(pat14, 'D410",', line)
               if hardwarePool[x] == "CASE":
                   line = re.sub(pat15, "2,5", line)
                   line = re.sub(pat16, '",', line)
                   line = re.sub(pat17, '"3.5', line)
                   line = re.sub(pat18, '"3.5", "', line)
                   line = re.sub(pat19, '2.5", "', line)
                   line = re.sub(pat20,'(3.5)', line )
                   line = re.sub(pat21, '"5.25', line)
                   line = re.sub(pat22, '"5,25", "', line)
                   line = re.sub(pat23, '"19', line)
                   line = re.sub(pat24, '"19", "', line)
                   line = re.sub(pat25, ' 3.5', line)
                   line = re.sub(pat26, '"2.5", "', line)
                   line = re.sub(pat27, '3.5", "', line)
                   line = re.sub(pat28,'"Inter-Tech 19', line)
                   line = re.sub(pat29, '3582,5", "', line)
                   line = re.sub(pat30, ': "3.5", "', line)
                   line = re.sub(pat31, '5.25",', line)
                   line = re.sub(pat32, '2-140mm, 1x', line)
                   line = re.sub(pat33, '0421342,5", "', line)
                   line = re.sub(pat34, 'jde, Aan', line)
                   line = re.sub(pat35, ': "2.5"', line)
               if hardwarePool[x] == "SSD":
                   line = re.sub(pat36, '": "2.5",', line)
                   line = re.sub(pat37, ' 2,5",', line)
                   line = re.sub(pat38, ' 2.5",', line)
                   line = re.sub(pat39, 'Intel 530 2,5 ', line)
                   line = re.sub(pat40, 'Toshiba 2.5 ', line)
                   line = re.sub(pat41, 'DC 2.5 S37', line)
                   line = re.sub(pat42, '"1,8 Slim"', line)
                   line = re.sub(pat43, '": "1.8",', line)
                   line = re.sub(pat44, ' 2.5 S', line)
                   line = re.sub(pat45, ' 2.5 M', line)
                   line = re.sub(pat46, '": "3.5",', line)
                   line = re.sub(pat47, 'TA 2.5 ', line)
                   line = re.sub(pat48, ' (2,5)", ', line)
                   line = re.sub(pat49, ' (1,8)", ', line)
                   line = re.sub(pat50, '6 2,5 ', line)
                   line = re.sub(pat51, 'S 3.5 ', line)
                   line = re.sub(pat52, 's 3.5 ', line)
                   line = re.sub(pat53, 'end 2.5 ', line)
                   line = re.sub(pat54, 'C300 2.5 ', line)
                   line = re.sub(pat55, 'a 1.8', line)
                   line = re.sub(pat56, 'A 1.8', line)
                   line = re.sub(pat57, 'C 2,5', line)
                   line = re.sub(pat58, 'end 1 ', line)
                   line = re.sub(pat59, 'SSD 2.5 (', line)
                   line = re.sub(pat60, 'C 1.8 S', line)
                   line = re.sub(pat61, 'D 2,5 ', line)
                   line = re.sub(pat62, 'SATA2 2.5 ', line)
                   line = re.sub(pat63, 'SATA 3.5 ', line)
                   line = re.sub(pat64, 'SAS 2.5 ', line)
                   line = re.sub(pat65, 'IBM 1.8 ', line)
                   line = re.sub(pat66, '"HP 2.5 ', line)
                   line = re.sub(pat67, 'FDE 2.5 ', line)



           except:
               print "no"
           if(index == collLength):
                f.write(line + "\n")
           else:
                f.write(line + ",\n")
       except:
           pass



    f.write("]")
    client.close()







