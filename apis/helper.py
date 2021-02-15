from pymongo import MongoClient

client = MongoClient('localhost',
                      username='root',
                      password='rootpassword',
                      authSource='admin',
                      authMechanism='SCRAM-SHA-256')

db = client['dvd-rental-system']
customer_colln = db.customers

# helper functions
def check_payments():
    for customer in customer_colln.find({}):
        full_name = f"{customer['First Name']} {customer['Last Name']}"
        rentals = customer['Rentals']

        for rental in rentals:
            if len(rental['Payments']) > 1:
                print(f"{full_name} has more than 1 payments")

