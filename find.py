import pymongo

if __name__ == "__main__":app.run(debug=True)
print("welcome to pymongo")
client = pymongo.MongoClient("mongodb://localhost:27017/")
print(client)

db = client['harry']
collection = db['mycollection']
   

# one = collection.find_one({'name':'nandu'})
# print(one)


oneall = collection.find({'name':'madhav'},{'_id':0})
for item in oneall:
    print(item)

allDocs = collection.find({'name':'harry'})
for i in allDocs:
    print(i)