__author__ = "jrbattles"

import pymongo

uri = "mongodb://127.0.0.1:27017"
client = pymongo.MongoClient(uri)
database = client['fullstack']
collection = database['students']

students = [student['Mark'] for student in collection.find({})]

print(students)