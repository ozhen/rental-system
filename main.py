from pymongo import MongoClient

client = MongoClient('localhost',
                      username='root',
                      password='rootpassword',
                      authSource='admin',
                      authMechanism='SCRAM-SHA-256')

db = client['dvd-rental-system']

print(db.list_collection_names())

customer_colln = db.customers
film_colln = db.films

print(customer_colln.count_documents({}))
print(film_colln.count_documents({}))