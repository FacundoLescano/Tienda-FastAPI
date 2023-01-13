import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["tienda-fastapi"]
#products_collection = mydb["products"]
#users_collection = mydb["users"]

def consult(collection):
    coll = mydb[collection]
    x = coll.find()
    for i in x:
        print(i)


def insert(collection, data):
    col = mydb[collection]
    x = col.insert_one(data)
    result = print(x.inserted_id)
    return result
# dato insert tipo DICT

#print(users_collection.find_one())
#x = mycol.insert_one(mydict)