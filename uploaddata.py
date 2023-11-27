import pymongo
import json
from pymongo import MongoClient, InsertOne

# Replace these placeholders with your actual values
connection_string = "<CONNECTION STRING>"
database_name = "college_critic"
collection_name = "<COLLECTION>"
file_path = "<FILENAME>"

# Connect to MongoDB
client = MongoClient(connection_string)
db = client[database_name]
collection = db[collection_name]

# Check if the collection exists, create it if not
if collection_name not in db.list_collection_names():
    db.create_collection(collection_name)

# List to store bulk write requests
requesting = []

# Open and read the JSON file
with open(file_path) as f:
    for jsonObj in f:
        try:
            myDict = json.loads(jsonObj)
            requesting.append(InsertOne(myDict))
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")

# Perform bulk write
try:
    result = collection.bulk_write(requesting)
    print(f"Documents inserted: {result.inserted_count}")
except pymongo.errors.BulkWriteError as bwe:
    print(f"Bulk write error: {bwe.details}")

# Close the MongoDB connection
client.close()
