import datetime

from pymongo import MongoClient

client = MongoClient('localhost',
                      username='root',
                      password='rootpassword',
                      authSource='admin',
                      authMechanism='SCRAM-SHA-256')

db = client['dvd-rental-system']
customer_colln = db.customers

def get_all():
    customer_list = []

    for customer in customer_colln.find({}):
        full_name = f"{customer['First Name']} {customer['Last Name']}"
        customer_list.append(full_name)

    return customer_list

def getCustomerMovieInfo(first_name, last_name):
    rental_info = {}

    for customer in customer_colln.find({'First Name': first_name,
                                         'Last Name': last_name}):
        rental_info = customer['Rentals']

    print(len(rental_info))

    for movie in rental_info:
        print(movie)
        print(movie['Film Title'])
        rental_date_str = movie['Rental Date']
        rental_date_obj = datetime.datetime.strptime(rental_date_str, '%Y-%m-%d %H:%M:%S.%f')
        print(rental_date_obj.date())

        return_date_str = movie['Return Date']
        return_date_obj = datetime.datetime.strptime(return_date_str, '%Y-%m-%d %H:%M:%S.%f')
        print(return_date_obj.date())

        # round
        print(movie['Payments'][0]['Amount'])
        break

# complated
#print(getAll())

# testing
getCustomerMovieInfo('GRACE', 'ELLIS')

'''
def checkPayments():
    for customer in customer_colln.find({}):
        full_name = f"{customer['First Name']} {customer['Last Name']}"
        rental_info = customer['Rentals']

        for movie in rental_info:
            if len(movie['Payments']) > 1:
                print(f"{full_name} has more than 1 payments")
#checkPayments()
'''