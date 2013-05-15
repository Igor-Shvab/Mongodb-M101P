import pymongo
import sys

connection = pymongo.Connection("mongodb://localhost", safe=True)

db = connection.students    # attach to db
collection = db.grades      # specify the colllection


query = {'type':'homework'}
sort = [('student_id', pymongo.ASCENDING), \
        ('score',pymongo.ASCENDING)]

cursor = collection.find(query).sort(sort)
def find():
    count = 0
    delete_count = 0
    previous_student_id = None
    for doc in cursor:
        count +=1
        must_delete = ''
        if (doc['student_id'] != previous_student_id):
            delete_count +=1
            previous_student_id = doc['student_id']
            must_delete = '<- [ DEL THIS ! ]'
            print collection.remove({'_id':doc['_id']}), 'deleted';
        print doc, previous_student_id, must_delete


    print 'Total docs:', count
    print ' ... of which to delete:', delete_count

find()
