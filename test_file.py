import pandas as pd
import numpy as np
import sqlite3

def update(gemeente: list[dict], lst_nieuwe_gemeente: list[dict]):
    gemeente_new = gemeente.copy()
    update_gem = gemeente_new + lst_nieuwe_gemeente
    return update_gem


# import the sqlite3 package
# create a database

def create(db):
    # create a table named Gemeentes
    db.execute('''CREATE TABLE gemeentes(
    Naam TEXT,
    CBSCODE TEXT,
    PLAATSEN TEXT,
    Inw_aantal INT,
    ACCURACY REAL);''')

    return db



if __name__ == '__main__':

    cnt = sqlite3.connect("Gemeenten2.dp")

    create = create(cnt)

    query = '''INSERT INTO gemeentes(Naam, CBSCODE, PLAATSEN, Inw_aantal) VALUES(
    'Test1', 'GEM001', ['WPL001', 'WPL002'], 100);'''
    # insert in different order
    cnt.execute(query)

    cnt.commit()

    cursor = cnt.execute('''SELECT * FROM gemeentes''')

    for i in cursor:
        print(i[0]+"    "+str(i[1])+"   "+str(i[2]))

# print(cursor)

# with open('Gemeenten.dp') as f:
#   bestandsdata = f.read()
#   print(bestandsdata)


# print('Hi')
#
# gem1 = [{'GEM001' : 'AA'}]
# gem2= [{'GEM001' : 'CCC'}]
# inw1 = 100
# inw2 = 300
# test = mult(inw1, inw2)
# lst_gem = update(gem1, gem2)
# print(test)
# print(lst_gem)