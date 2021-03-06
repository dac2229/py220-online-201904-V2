#!/usr/bin/env python3
# pylint: disable = E1101
"""
grade lesson 5
"""

import os
import pytest
import sys
import database as l

@pytest.fixture
def _show_available_products():
    return{
        'prd001': {'description': '60-inch TV stand', 'product_type': 'livingroom', 'quantity_available': '3'},
        'prd003': {'description': 'Acacia kitchen table', 'product_type': 'kitchen', 'quantity_available': '7'},
        'prd004': {'description': 'Queen bed', 'product_type': 'bedroom', 'quantity_available': '10'},
        'prd005': {'description': 'Reading lamp', 'product_type': 'bedroom', 'quantity_available': '20'},
        'prd006': {'description': 'Portable heater', 'product_type': 'bathroom', 'quantity_available': '14'},
        'prd008': {'description': 'Smart microwave', 'product_type': 'kitchen', 'quantity_available': '30'},
        'prd010': {'description': '60-inch TV', 'product_type': 'livingroom', 'quantity_available': '3'}
        }

@pytest.fixture
def _show_rentals():
    return {
            'user008': {'name': 'Shirlene Harris', 'address': '4329 Honeysuckle Lane', 'phone_number': '206-279-5340', 'email': 'harrisfamily@gmail.com'},
            'user005': {'name': 'Dan Sounders', 'address': '861 Honeysuckle Lane', 'phone_number': '206-279-1723', 'email': 'soundersoccer@mls.com'}
            }


def test_import_data():
    """ import """
    cwd = os.path.abspath(os.path.join(os.path.dirname( __file__ )))
    print(cwd)
    db = l.database()
    added, errors = db.import_data(cwd+"/", "product.csv", "customers.csv", "rental.csv")
    print(added)
    for add in added:
        assert isinstance(add, int)

    for error in errors:
        assert isinstance(error, int)

    assert added == (10, 10, 9)
    assert errors == (0, 0, 0)
    f1 = open("timings.txt", "r")
    last_line = f1.readlines()[-1]
    last_line = last_line.split()
    assert float(last_line[2]) > 0
    f1.close()

def test_show_available_products(_show_available_products):
    """ available products """
    db = l.database()
    students_response = db.show_available_products()
    assert students_response == _show_available_products
    f1 = open("timings.txt", "r")
    last_line = f1.readlines()[-1]
    last_line = last_line.split()
    assert float(last_line[2]) > 0
    f1.close()

def test_show_rentals(_show_rentals):
    """ rentals """
    db = l.database()
    students_response = db.show_rentals("prd002")
    assert students_response == _show_rentals
    f1 = open("timings.txt", "r")
    last_line = f1.readlines()[-1]
    last_line = last_line.split()
    assert float(last_line[2]) > 0
    f1.close()

