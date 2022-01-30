import pandas as pd
import numpy as np
import sqlite3

# eigenschappen; naam ,cbscode, gemeente, inwonersaantal

# check of cbs code uit 6 tekens betsaat en met WPL begint, en dan 3 cijfers.

class Plaatsen:
    def check_plaats(plaats_data: dict):
        plaats = plaats_data.copy()
        naam = plaats.get('naam')
        gemeente = plaats.get('gemeente')
        cbscode = plaats.get('cbscode')
        inwonersaantal = plaats.get('inwonersaantal')

        cbs_char = str(cbscode)[:3]
        cbs_num = str(cbscode[3:])
        if str(cbs_char) == 'WPL':
            if len(cbs_num) > 3:
                print(f'Invalid CBS Code, {cbscode} will not be created')
            num_check = []
            for i in cbs_num:
                num_check.append(i.isdigit())
            if all(num_check) == True:
                #pass #number is OK.
                return plaats
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
            cur.execute(f'''CREATE TABLE {db_name} (
            cbscode text PRIMARY KEY,
            naam text NOT NULL,
            gemeente text,
            inwonersaantal INTEGER);''')
            print(f'Succesfully created database: {db_name}')
        except:
            print('error in operation, no database created.')
            db.rollback()
        db.close()
        return db

    def create(db_name: str, data_plaats: dict):
        data = data_plaats.copy()
        data = Plaatsen.check_plaats(data)

        naam = data.get('naam')
        gemeente = data.get('plaatsen')
        gemeente = str(gemeente)
        cbscode = data.get('cbscode')
        inwonersaantal = data.get('inwonersaantal')

        db = sqlite3.connect(f'{db_name}.db')
        qry = f"INSERT INTO {db_name} (cbscode, naam, gemeente, inwonersaantal) VALUES {cbscode, naam, gemeente, inwonersaantal};"
        try:
            cur = db.cursor()
            cur.execute(qry)
            db.commit()
            print(f"one record added successfully, added: {data_plaats}")
        except:
            print("error in operation")
            db.rollback()
        db.close()
        return db

    def create_many(db_name: str ,data_gemeente: list[dict]):
        data_gemeente_new = data_gemeente.copy()
        for item in data_gemeente_new:
            create_one = Plaatsen.create(db_name, item)

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

    def update(db_name: str, update_plaats: dict):
        data = update_plaats.copy()
        data = Plaatsen.check_plaats(data)
        naam = data.get('naam')
        gemeente = data.get('gemeente')
        gemeente = str(gemeente)
        cbscode = data.get('cbscode')
        inwonersaantal = data.get('inwonersaantal')

        db = sqlite3.connect(f'{db_name}.db')
        qry = f"update {db_name} set naam=?, gemeente=?, inwonersaantal=? where cbscode=?;"
        try:
            cur = db.cursor()
            cur.execute(qry, (naam, gemeente, inwonersaantal, cbscode))
            db.commit()
            print("record updated successfully")
        except:
            print("error in operation")
            db.rollback()
        db.close()

    def delete(db_name: str, cbs_code: str):
        cbs_delete = cbs_code
        print(cbs_delete)
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

if __name__ == '__main__':

    name_db = 'plaats04'

    tt1 = Plaatsen.create_db(name_db)
    df_tst = {"naam": "Nuenen", "cbscode": "WPL011", "gemeente": "WPL002", "inwonersaantal": 1001}
    #tt2 = Plaatsen.create(name_db, df_tst)

    rr = Plaatsen.create_many(name_db, [{"naam": "Mijn gemeetesss", "cbscode": "WAL002", "gemeente": "GEM001", "inwonersaantal": 1001},
                      {"naam": "Mijn gemeete2", "cbscode": "WPL003", "gemeente": "GEM001", "inwonersaantal": 1011},
                      {"naam": "Tester", "cbscode": "WPL043", "gemeente": "GEM002", "inwonersaantal": 2000}])

    ss = Plaatsen.read(name_db, 'WPL003')
    ss2 = Plaatsen.read_all(name_db)

    test_update = {"naam": "Tester2", "cbscode": "WPL043", "gemeente": "WPL223", "inwonersaantal": 12000}
    ee = Plaatsen.update(name_db, test_update)
    ss = Plaatsen.read(name_db, 'WPL223')
    ss2 = Plaatsen.delete(name_db, 'WPL223')

    # [{ "naam": "Mijn gemeente", "cbscode": "WPL001", "inwonersaantal": 1000, "gemeente": "Harderwerken"}] )
