import pandas as pd
import numpy as np


#eigenschappen: naam, cbscode, plaatsen, inwonersaantal

# check of cbs code uit 6 tekens betsaat en met GEM begint, en dan 3 cijfers.

# Input /Created
#{“naam”: “Mijn gemeete”, “cbscode”: “GEM001”, “plaatsen”: [“WPL001”, “WPL002”]}
class Gemeente:
    def check_gemeente (gemeente_data: dict):
        gemeente = gemeente_data.copy()
        naam = gemeente.get('naam')
        plaatsen = gemeente.get('plaatsen')
        cbscode = gemeente.get('cbscode')
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


    def create(data_gemeente: list[dict]):
        data = data_gemeente.copy()
        lst_gemeente = []

        for item in data:
            test = Gemeente.check_gemeente(item)
            lst_gemeente.append(test)
            df = pd.DataFrame(lst_gemeente).dropna()

        return df

    def update(data, gem_update):
        data_new = data.copy()
        gem_upd = gem_update.copy()
        naam = gem_upd.get('naam')
        plaatsen = gem_upd.get('plaatsen')
        cbscode = gem_upd.get('cbscode')
        upd = pd.DataFrame([naam, cbscode, [plaatsen]]).T
        upd.columns = ['naam', 'cbscode', 'plaatsen']

        #delete old
        nn3 = gem_update.get('cbscode')
        data_updated = data_new[data_new.cbscode != nn3]


        data_updated = pd.concat([data_updated,upd])

        return data_updated






if __name__ == '__main__':

    test = Gemeente.create([{"naam": "Mijn gemeete", "cbscode": "GEM001", "plaatsen": ["WPL001", "WPL002"]},
                     {"naam": "Mijn gemeete2", "cbscode": "GAD001", "plaatsen": ["WPL003", "WPL002"]},
                     {"naam": "Tester", "cbscode": "GEM005", "plaatsen": ["WPL043", "WPL202"]}
                     ])
    print('...')
    upd_test = Gemeente.update(test, {"naam": "Tester", "cbscode": "GEM005", "plaatsen": ["WPL993", "WPL202"]})
    print(upd_test)