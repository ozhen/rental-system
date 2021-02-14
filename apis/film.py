from pymongo import MongoClient

client = MongoClient('localhost',
                      username='root',
                      password='rootpassword',
                      authSource='admin',
                      authMechanism='SCRAM-SHA-256')

db = client['dvd-rental-system']
film_colln = db.films

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
