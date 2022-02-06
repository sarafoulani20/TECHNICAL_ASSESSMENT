import os
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()
# use default mongo db uri if MONGO_URI is not set
client = MongoClient(os.getenv('MONGO_URI', 'mongodb://localhost:27017'))
db = client.test
collection = db.employee_attrition