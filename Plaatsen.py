import pandas as pd
import numpy as np


# eigenschappen; naam ,cbscode, inwonersaantal, gemeente

# check of cbs code uit 6 tekens betsaat en met WPL begint, en dan 3 cijfers.



def Plaatsen(plaats_data: list [dict]):
    plaats = plaats_data.copy()
    plaatsen = []
    for item in plaats:
        naam = item.get('naam')
        cbscode = item.get('cbscode')
        inwonersaantal = item.get('inwonersaantal')
        gemeente = item.get('gemeente')
        cbs_char = str(cbscode)[:3]
        cbs_num = str(cbscode[3:])
        if inwonersaantal < 0:
            print('negatief aantal inwoners in gemeente, gemeente niet opgenomen')
        if str(cbs_char) == 'WPL':
            if len(cbs_num) > 3:
                print(f'Invalid CBS Code, {cbscode} will not be created')
            num_check = []
            for i in cbs_num:
                    num_check.append(i.isdigit())
            if all(num_check) == True:
                pass  # number is OK.
                plaatsen.append(item)
            else:
                print(f'Invalid CBS Code, number are not all digits. {cbscode} will not be created')

        else:
            print(f'Invalid CBS Code, code is geen plaats {cbscode}, this code will not be created')

        return print(plaatsen)

if __name__ == '__main__':

    test = Plaatsen([{ "naam": "Mijn gemeente", "cbscode": "WPL001", "inwonersaantal": 1000, "gemeente": "Harderwerken"}] )
