import sqlite3
from functions import *

if __name__ == '__main__':
    name_db = 'MI_gem'

    df_tst = {"naam": "Gemeente 1", "cbscode": "GEM001", "plaatsen": ["WPL001"], "inwonersaantal": 100}

    cr_db = Gemeente.create_db(name_db)
    ins_rec = Gemeente.create(name_db, df_tst)
    ins_many = Gemeente.create_many(name_db, [{"naam": "Gemeente 1a", "cbscode": "GEM011", "plaatsen": ["WPL011"], "inwonersaantal": 125},
                     {"naam": "Gemeente 2a", "cbscode": "GEM012", "plaatsen": "WPL012", "inwonersaantal": 1509},
                     {"naam": "Gemeente 2a", "cbscode": "GEM012", "plaatsen": "WPL013", "inwonersaantal": 2512},
                     {"naam": "Gemeente 3a", "cbscode": "GEM013", "plaatsen": "WPL014","inwonersaantal": 125000}])

    read = Gemeente.read(name_db, 'GEM011')
    read_all = Gemeente.read_all(name_db)
    upd_rec = {"naam": "Gemeente 2", "cbscode": "GEM001", "plaatsen": "WPL001", "inwonersaantal": 100}
    crud_upd = Gemeente.update(name_db, upd_rec, "GEM002", '')

    fusie1 = {"naam": "Fusiegemeente", "cbscode": "GEM011", "plaatsen": ["WPL011"], "inwonersaantal": 125}
    fusie2= {"naam": "Fusiegemeente", "cbscode": "GEM012", "plaatsen": ["WPL012"], "inwonersaantal": 1509}
    fusie3 = {"naam": "Fusiegemeente", "cbscode": "GEM012", "plaatsen": ["WPL013"], "inwonersaantal": 125000}

    fusie4 = Gemeente.update(name_db, fusie1, "GEM100", "Fusiegemeente")
    fusie5 = Gemeente.update(name_db, fusie2, "GEM100", "Fusiegemeente")
    fusie6 = Gemeente.update(name_db, fusie3, "GEM100", "Fusiegemeente")

    print("..")
    ss2 = Gemeente.read_all(name_db)
    ss = Gemeente.read(name_db, 'GEM100')
    #ss2 = Gemeente.delete(name_db, 'GEM001')
