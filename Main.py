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







