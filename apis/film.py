from pymongo import MongoClient

client = MongoClient('localhost',
                      username='root',
                      password='rootpassword',
                      authSource='admin',
                      authMechanism='SCRAM-SHA-256')

db = client['dvd-rental-system']
film_colln = db.films
customer_colln = db.customers

def get_all():
    """Get all films data from film collection in db

    Returns:
        list: contain film dicts
    """

    film_list = []

    for film in film_colln.find({}):
        film_info = {"rating": film['Rating']}
        film_info["description"] = film['Description']
        film_info["category"] = film['Category']
        film_info["rental_duration"] = film['Rental Duration']

        # add available film to the film list
        film_dict = { film["Title"]: film_info}

        film_list.append(film_info)

    return film_list


def get_film(film_name):
    """Search for the selected film in film collection in db

    Returns:
        dict: contain film rental histroy and other details
    """
    customer_list = []
    selected_film = {}

    # search the film in film collection
    for film in film_colln.find({"Title": film_name}):
        selected_film = film

    # returns when film is not in film collection
    if not selected_film:
        return {}

    # search each customer in customer collection
    for customer in customer_colln.find({}):
        rentals = customer['Rentals']

        # search each rental from each customer
        for rental in rentals:
            # add customer's full name onces the film is found
            if film_name in rental['Film Title']:
                full_name = f"{customer['First Name']} {customer['Last Name']}"
                customer_list.append(full_name)

    # remove duplicates in customer list
    selected_film["rental_history"] = list(set(customer_list))

    return selected_film

print(get_film('FIREBALL PHILADELPHIA'))
print(get_film('anime'))