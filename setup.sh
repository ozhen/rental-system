#!/bin/bash
mongoimport --db dvd-rental-system --collection customers --file ./data/DVDRentals-customers.json --authenticationDatabase admin -u root -p rootpassword

mongoimport --db dvd-rental-system --collection films --file ./data/DVDRentals-films.json --authenticationDatabase admin -u root -p rootpassword
