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

def get_rental_info(first_name, last_name):
    rental_list = []

    # search for selected customer's rental info
    for customer in customer_colln.find({'First Name': first_name,
                                         'Last Name': last_name}):
        rentals = customer['Rentals']

    for rental in rentals:
        rental_date_str = rental['Rental Date']
        rental_date_obj = datetime.datetime.strptime(rental_date_str, '%Y-%m-%d %H:%M:%S.%f')

        return_date_str = rental['Return Date']

        # checks if the movie has been returned
        if return_date_str:
            # when movie has returned
            return_date_obj = datetime.datetime.strptime(return_date_str, '%Y-%m-%d %H:%M:%S.%f')
            rented_days = return_date_obj.date() - rental_date_obj.date()
        else:
            today = datetime.date.today()
            rented_days = today - rental_date_obj.date()

        rental_info = {"rented_days": rented_days.days}

        # round cost to 2 decimals
        rental_info["cost"] = round(rental['Payments'][0]['Amount'], 2)

        # add rented movie to the movie list
        rented_movie = { rental["Film Title"]: rental_info}
        rental_list.append(rented_movie)
    
    return rental_list


# complated
#print(getAll())
#print(get_rental_info('MARY', 'SMITH'))

# testing

'''
# helper functions
def checkPayments():
    for customer in customer_colln.find({}):
        full_name = f"{customer['First Name']} {customer['Last Name']}"
        rentals = customer['Rentals']

        for rental in rentals:
            if len(rental['Payments']) > 1:
                print(f"{full_name} has more than 1 payments")
#checkPayments()
'''