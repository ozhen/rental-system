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
    customer_list = []

    for customer in customer_colln.find({}):
        rentals = customer['Rentals']

        for rental in rentals:
            if film_name in rental['Film Title']:
                full_name = f"{customer['First Name']} {customer['Last Name']}"
                customer_list.append(full_name)

    for film in film_colln.find({"Title": film_name}):
        selected_film = film

    # remove duplicates in customer list
    selected_film["rental_history"] = list(set(customer_list))

    return selected_film

print(get_film('FIREBALL PHILADELPHIA'))