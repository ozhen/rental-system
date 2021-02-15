# DVD Rentals

## Installation

### Mongodb Import
```
~/rental-system$./setup.sh
```

### Docker (Optional)
```
~/rental-system$docker-compose up -d
```
### Venv (Optional)
```
~/rental-system$python3.8 -m venv _venv
. _venv/bin/activate
```

## Running
```
~/rental-system$python3.8 -m venv _venv
. _venv/bin/activate
```

## Assumptions
1. There is only one payment from each rental in customers' collection
(confirmed with check_payment() in helper.py)
1. If return date is null, rented days is calculated from rent day to today
