import pymongo

if __name__ == "__main__":app.run(debug=True)
print("welcome to pymongo")
client = pymongo.MongoClient("mongodb://localhost:27017/")
print(client)

db = client['harry']
collection = db['mycollection']
   
# rec = {'name':'madhav'}
# collection.delete_many(rec)

rec2 = {'name':'harry2'}
collection.delete_many(rec2)