from pymongo import MongoClient
from bson.objectid import ObjectId
import urllib.parse

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, username, password):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections. 
        self.username = username
        self.password = password
        self.client = MongoClient(f'mongodb://{self.username}:{self.password}@localhost:37032/?authSource=AAC')
        # where xxxx is your unique port number
        self.database = self.client['AAC']

# Create method to implement the C in CRUD.
    def create_one_document(self, data):
        if data is not None:
            self.database.animals.insert_one(data)  # data should be dictionary 
            return True
        else:
            raise Exception("False. Nothing to save, because data parameter is empty.")
            
# Read method to implement the R in CRUD. 
# if data parameter is a key/value pair - {key:value} - it will return a cursor with just one document
# if data is left None it will return a cursor containing all the documents
    def read(self, *args, noArgs=False):
        if noArgs:
            return self.database.animals.find()
        elif not noArgs:
            return self.database.animals.find(*args)
        else:
            raise Exception("False. Invalid entry.")
            
    def readAll(self, data={}):
        return self.database.animals.find(data,{"_id": 0})
            
# Update method to implement the U in CRUD
    def update(self, filter_data, new_data, isSingle):
        if filter_data and new_data is not None:
            if isSingle:
                self.database.animals.update_one(filter_data, new_data)
                return True
            elif isSingle is False:
                self.database.animals.update_many(filter_data, new_data)
                return True
        else:
            raise Exception("Invalid input. Please try again.")

# Delete method to implement the D in CRUD
    def delete(self, data, isSingle=True):
        if data is not None:
            if isSingle:
                self.database.animals.delete_one(data)
                return True
            elif not isSingle:
                self.database.animals.delete_many(data)
                return True
        else:
            raise Exception("Value does not exist.")



"""
Test data:

{'1': , 'age_upon_outcome': , 'animal_id': , 'animal_type': , 'breed': , 'color': , 'date_of_birth': , 'datetime': , 
'monthyear': , 'name': '', 'outcome_subtype': , 'outcome_type': , 'sex_upon_outcome': , 'location_lat': , 
'location_long': , 'age_upon_outcome_in_weeks': }

{'_id': ObjectId('63c5d4a946805ca89a0c9e8e'), '1': 1, 'age_upon_outcome': '3 years', 'animal_id': 'A746874', 
'animal_type': 'Cat', 'breed': 'Domestic Shorthair Mix', 'color': 'Black/White', 'date_of_birth': '2014-04-10', 
'datetime': '2017-04-11 09:00:00', 'monthyear': '2017-04-11T09:00:00', 'name': '', 'outcome_subtype': 'SCRP', 
'outcome_type': 'Transfer', 'sex_upon_outcome': 'Neutered Male', 'location_lat': 30.5066578739455, 
'location_long': -97.3408780722188, 'age_upon_outcome_in_weeks': 156.767857142857}

{'1': 10001, 'age_upon_outcome': '7 years', 'animal_id': 'A893523', 'animal_type': 'Cat', 'breed': 'Domestic Shorthair Mix', 
'color': 'Yellow', 'date_of_birth': '2016-07-25', 'datetime': '2017-04-11 09:00:00', 
'monthyear': '2017-04-11T09:00:00', 'name': 'Spotty', 'outcome_subtype': 'SCRP', 'outcome_type': 'Transfer', 
'sex_upon_outcome': 'Neutered Male', 'location_lat': 30.5066578739455, 'location_long': -97.3408780722188, 
'age_upon_outcome_in_weeks': 156.767857142857}

"""
            
