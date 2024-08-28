import pymongo

if __name__ == "__main__":app.run(debug=True)
print("welcome to pymongo")
client = pymongo.MongoClient("mongodb://localhost:27017/")

# print(client)


allDatabases = client.list_database_names()
print(allDatabases)

for item in allDatabases:
    print(item)

db = client['harry']
collection = db['mycollection']
   

