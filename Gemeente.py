import pandas as pd
import numpy as np
import sqlite3

#eigenschappen: naam, cbscode, plaatsen, inwonersaantal

# check of cbs code uit 6 tekens betsaat en met GEM begint, en dan 3 cijfers.

# Input /Created
#{“naam”: “Mijn gemeete”, “cbscode”: “GEM001”, “plaatsen”: [“WPL001”, “WPL002”], "inwonersaantal": 1000}
class Gemeente:
    def check_gemeente(gemeente_data: dict):
        gemeente = gemeente_data.copy()
        naam = gemeente.get('naam')
        plaatsen = gemeente.get('plaatsen')
        cbscode = gemeente.get('cbscode')
        inwonersaantal = gemeente.get('inwonersaantal')

        cbs_char = str(cbscode)[:3]
        cbs_num = str(cbscode[3:])
        if str(cbs_char) == 'GEM':
            if len(cbs_num) > 3:
                print(f'Invalid CBS Code, {cbscode} will not be created')
            num_check = []
            for i in cbs_num:
                num_check.append(i.isdigit())
            if all(num_check) == True:
                pass #number is OK.
                return gemeente
            else:
                print(f'Invalid CBS Code, number is invalid. {cbscode} will not be created')
                return{}
        else:
            print(f'Invalid CBS Code, code is geen gemeente {cbscode}, this code will not be created')
            return {}

    def create_db(db_name: str):
        db = sqlite3.connect(f'{db_name}.db')
        cur = db.cursor()
        try:
            #create DB
            cur.execute(f'''CREATE TABLE IF NOT EXISTS {db_name} (
            cbscode text NOT NULL,
            naam text NOT NULL,
            plaatsen text,
            inwonersaantal INTEGER,
            PRIMARY KEY (cbscode, naam, plaatsen))
            ;''')
            print(f'Succesfully created database: {db_name}')
        except:
            print('error in operation, no database created.')
            db.rollback()
        db.close()
        return db

    def create(db_name: str, data_gemeente: dict):
        data = data_gemeente.copy()
        data = Gemeente.check_gemeente(data)
        naam = data.get('naam')
        plaatsen = data.get('plaatsen')
        plaatsen = str(plaatsen)
        cbscode = data.get('cbscode')
        inwonersaantal = data.get('inwonersaantal')

        db = sqlite3.connect(f'{db_name}.db')
        qry = f"INSERT INTO {db_name} (cbscode, naam, plaatsen, inwonersaantal) VALUES {cbscode, naam, plaatsen, inwonersaantal};"
        try:
            cur = db.cursor()
            cur.execute(qry)
            db.commit()
            print(f"one record added successfully, added: {data_gemeente}")
        except:
            print("error in operation")
            db.rollback()

        db.close()
        return db

    def create_many(db_name: str ,data_gemeente: list[dict]):
        data_gemeente_new = data_gemeente.copy()
        for item in data_gemeente_new:
            create_one = Gemeente.create(db_name, item)

    def read(db_name: str, cbs_code: str):
        db = sqlite3.connect(f'{db_name}.db')
        sql = f"SELECT * from {db_name} where cbscode = '{cbs_code}';"
        cur = db.cursor()
        cur.execute(sql)
        while True:
            record = cur.fetchone()
            if record == None:
                break
            print(record)
        db.close()
        return record

    def read_all(db_name: str):
        db = sqlite3.connect(f'{db_name}.db')
        sql = f"SELECT cbscode from {db_name};"
        cur = db.cursor()
        cur.execute(sql)

        cbs_codes  = cur.fetchall()
        for rec in cbs_codes:
            print(rec)
        return cbs_codes

    def update(db_name: str, update_gemeente: dict, new_cbs_code: str, new_name: None):
        data = update_gemeente.copy()
        data = Gemeente.check_gemeente(data)

        if new_name != None:
            naam = new_name
        else:
            naam = data.get('naam')
        plaatsen = data.get('plaatsen')
        plaatsen = str(plaatsen)
        cbscode = data.get('cbscode')
        inwonersaantal = data.get('inwonersaantal')



        db = sqlite3.connect(f'{db_name}.db')
        qry = f"update {db_name} set cbscode = ?, naam=?, plaatsen=?, inwonersaantal=? where cbscode=?;"
        try:
            cur = db.cursor()
            cur.execute(qry, (new_cbs_code, naam, plaatsen, inwonersaantal, cbscode))
            db.commit()
            print("record updated successfully")
        except:
            print("error in operation")
            db.rollback()

        qry_empty_gem = f"DELETE FROM {db_name} WHERE plaatsen IS NULL OR trim(plaatsen) = '';"
        try:
            cur = db.cursor()
            cur.execute(qry_empty_gem)
            db.commit()
            print(f"Gemeente {cbscode} did not have any WPL left. So is deleted")
        except:
            print("Empty 'gemeente' not deleted")
            db.rollback()

        db.close()
        return db

    def delete(db_name: str, cbs_code: str):
        cbs_delete =cbs_code
        db = sqlite3.connect(f'{db_name}.db')
        qry = f"DELETE from {db_name} where cbscode='cbs_delete' ;"
        try:
            cur = db.cursor()
            cur.execute(qry)
            db.commit()
            print(f"Record deleted successfully {cbs_code}")
        except:
            print("error in operation")
            db.rollback()
        db.close()
        return db

if __name__ == '__main__':



