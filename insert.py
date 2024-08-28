import pymongo


if __name__ == "__main__":app.run(debug=True)
print("welcome to pymongo")
client = pymongo.MongoClient("mongodb://localhost:27017/")
print(client)

db = client['harry']
collection = db['mycollection']
# dictionary = {'name':'harry', 'marks':50}
# collection.insert_one(dictionary)

# dictionary2 = {'name':'harry2', 'marks':150}
# collection.insert_one(dictionary2)
     
insertThese = [
    {'_id':1,'name':'harry','city':'agra','mark':23},
    {'_id':2,'name':'nandu','city':'delhi','mark':33},
    {'_id':3,'name':'riya','city':'mathura','mark':25},
    {'_id':4,'name':'madhav','city':'jaipur','mark':80},      
    {'_id':4,'name':'madhav','city':'agra','mark':80},      
]

collection.insert_many(insertThese)