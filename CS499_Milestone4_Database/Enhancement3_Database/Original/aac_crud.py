from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object): 
    """ CRUD operations for Animal collection in MongoDB """ 

    def __init__(self, username, password): 
        
        self.client = MongoClient('mongodb://%s:%s@localhost:27017/?authSource=aac' %(username, password)) 
        self.database = self.client['aac'] 
        self.collection = self.database['animals'] 
            
    # Complete this create method to implement the C in CRUD. 
    def create(self, data):
        if data is not None: 
            insert_result = self.collection.insert_one(data)
            if insert_result.acknowledged:
                print(f" Record inserted successfully with_id: {insert_result.inserted_id}")
                return {"success": True, "inserted_id": str(insert_result.inserted_id)}
            else:
                print(" Insertion failed.")
                return {"success": False, "inserted_id": None}
        else:
            raise Exception("Nothing to save, because data parameter is empty") 

    # Read method
    def read(self, searchData):
        if searchData is not None:
            data = list(self.collection.find(searchData, {"_id": False}))
        else:
            data = list(self.collection.find({}, {"_id": False}))
            
        count = len(data)
        print(f" Found {count} record(s) matching your query.")
        return data
        
    def update(self, searchData, updateData):
        if searchData is not None and updateData is not None:
            result = self.collection.update_many(searchData, {"$set": updateData})
            print(f" Updated {result.modified_count} record(s).")
            return {"success": True, "modified_count": result.modified_count}
        else:
            raise Exception("Both searchData and updateData parameters are required.")
    
    def delete(self, deleteData):
        if deleteData is not None:
            result = self.collection.delete_many(deleteData)
            return {"success": True, "deleted_count": resutl.deleted_count}
        else:
            raise Exception("deleteData parameter is required.")