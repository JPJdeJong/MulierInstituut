import sqlite3


class Create():
    def create_db_gemeente(db_name: str):
        """
        Args:
            db_name: str, a string with the name of the db.
        Returns:
            db: a created sqlite database.
        """
        db = sqlite3.connect(f'{db_name}.db')
        cur = db.cursor()
        try:
            #create DB
            cur.execute(f'''CREATE TABLE IF NOT EXISTS {db_name} (
            cbscode text PRIMARY KEY,
            naam text NOT NULL,
            plaatsen text,
            inwonersaantal INTEGER);''')
            print(f'Succesfully created database: {db_name}')
        except:
            print('error in operation, no database created.')
            db.rollback()
        db.close()
        return db

    def create_db_plaats(db_name: str):
        """
        Args:
            db_name: str, a string with the name of the db.
        Returns:
            db: a created sqlite database.
        """
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