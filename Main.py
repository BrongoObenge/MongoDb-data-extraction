#!/usr/bin/python2.7
__author__ = 'j'
from manager import MongoDbManager
import sys
mongoManager = MongoDbManager.MongoDbManager()
client = mongoManager.openDb()

coll =  client['Hardware']['hardware-collection']
cursor =  coll.find()

try:
    location = sys.argv[1]
except:
    location = 'mongodb-dump.php'
f = open(location,'w')      #Needs to be .php extension for angularJS to interact with
f.write("[")
while cursor.alive:
   try:
       line = str(cursor.next()).replace("\"", "\'")
       line = line.replace("u\'", "\'")
       f.write( line + ",\n")
   except:
       pass

f.write("]")
client.close()












