#!/usr/bin/python2.7
__author__ = 'j'
from manager import MongoDbManager
import sys
import re

mongoManager = MongoDbManager.MongoDbManager()
client = mongoManager.openDb()

coll =  client['Hardware']['hardware-collection']
cursor =  coll.find()
pattern = r"\"_id\":.ObjectId\(((.)+)\"\)"
try:
    location = sys.argv[1]
except:
    location = 'mongodb-dump.php'
f = open(location,'w')      #Needs to be .php extension for angularJS to interact with
f.write("[")
i = 0
while cursor.alive:
   try:
       line = str(cursor.next()).replace("\'", "\"")
       line = line.replace("u\"", "\"")
       try:
           line =  re.sub(pattern, "" ,line)
       except:
           print "no"
           pass
       f.write(line + ",\n")
   except:
       pass

f.write("]")
client.close()












