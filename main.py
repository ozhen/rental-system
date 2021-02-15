from apis.customer import get_all_customers, get_rental_info
from apis.film import get_all_films, get_film

# customers
print(get_all_customers())
print(get_rental_info('MARY', 'SMITH'))

# films
print(get_all_films())
print(get_film('FIREBALL PHILADELPHIA'))
print(get_film('ONE PIECE'))