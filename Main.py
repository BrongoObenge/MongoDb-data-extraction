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
while cursor.alive:
   try:
        f.write(str(cursor.next()) + "\n")
   except:
       pass














