import pymongo

if __name__ == "__main__":app.run(debug=True)
print("welcome to pymongo")
client = pymongo.MongoClient("mongodb://localhost:27017/")
print(client)

db = client['harry']
collection = db['mycollection']
   

prev={'name':'riya'}
nextt={'$set':{'city':'pune'}}
collection.update_one(prev , nextt)

for x in collection.find():
    print(x)