# DVD Rentals

## Environments
1. Python 3.8.5
1. MongoDB 4.0
1. Ubuntu 20.04.2 LTS

## Installation

### Docker for MongoDB (Optional)
```
~/rental-system$docker-compose up -d
```
### Venv (Optional)
```
~/rental-system$python3.8 -m venv _venv
. _venv/bin/activate
```
### Mongodb Import
```
~/rental-system$./setup.sh
```
### Requirements
```
~/rental-system$pip install -r requirements.py
```

## Running
```
~/rental-system$python3.8 main.py
```

## Defaults
1. 'MARY SMITH' is the default value for get_rental_info()
1. 'FIREBALL PHILADELPHIA' is the default value for get_film()

## Assumptions
1. There is only one payment from each rental in customers' collection
(confirmed with check_payment() in helper.py)
1. If return date is null, rented days is calculated from rent day to today
