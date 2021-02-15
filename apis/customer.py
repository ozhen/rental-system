import datetime

from pymongo import MongoClient

client = MongoClient('localhost',
                      username='root',
                      password='rootpassword',
                      authSource='admin',
                      authMechanism='SCRAM-SHA-256')

db = client['dvd-rental-system']
customer_colln = db.customers

def get_all_customers():
    """Get all customer data from customer collection in db

    Returns:
        list: contain customers dicts with full name as key
    """
    customer_list = []

    for customer in customer_colln.find({}):
        full_name = f"{customer['First Name']} {customer['Last Name']}"
        customer_list.append(full_name)

    return customer_list

def get_rental_info(first_name, last_name):
    """Search for the selected film in film collection in db

    Args:
        first_name (str): First name of the seleceted customer
        last_name (str): Last name of the seleceted customer

    Returns:
        list: contain the seleceted customer's all rental data in dicts with
              film title as key
    """
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