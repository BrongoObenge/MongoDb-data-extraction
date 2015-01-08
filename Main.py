#!/usr/bin/python2.7
__author__ = 'j'
from manager import MongoDbManager
import sys
import re

mongoManager = MongoDbManager.MongoDbManager()
client = mongoManager.openDb()

coll = client['Hardware']['MEMORY']
cursor =  coll.find()
collLength = coll.count()

pattern = r'\"_id\":.ObjectId\(((.)+)\"\)'
pattern1 = r"(\\\\r\\\\n)"
pattern2 = r"(\\\\r\\\\n)"
pattern3 = r"(\\\\u2022\W)"
pattern4 = r'(\"\[\"\\?\"?)'
pattern5 = r'(\"]\"?)'
pattern6 = r'(\, })'
pattern7 = r'(u\\)'
pattern8 = r'(\"\"(?![,]))'
pattern9 = r'(,\s,)'
pattern10 = r'},\n]'
pattern11 = r'(,\W\"Bijzonderheden\":.+)\}'
pattern12 = r'("Golden\WSample")'
try:
    location = sys.argv[1]
except:
    location = 'mongodb-dumpMEMORY.php'

f = open(location, 'w')      #Needs to be .php extension for angularJS to interact with
f.write("[")
index = 0
while cursor.alive:
   index += 1

   try:
       line = str(cursor.next()).replace("\'", "\"")
       line = line.replace("u\"", "\"")
       try:
           line = re.sub(pattern, "", line)
           line = re.sub(pattern1, "", line)
           line = re.sub(pattern2, "", line)
           line = re.sub(pattern3, "", line)
           line = re.sub(pattern4, '"', line)
           line = re.sub(pattern5, '"', line)
           line = re.sub(pattern6, ' }', line)
           line = re.sub(pattern7, "", line)
           line = re.sub(pattern8, ", \n", line)
           line = re.sub(pattern9, ",", line)
           line = re.sub(pattern10, "}\n]", line)
           line = re.sub(pattern11, "}", line)
           line = re.sub(pattern12, "", line)
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












