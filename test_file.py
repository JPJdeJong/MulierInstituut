import pandas as pd
import numpy as np

def mult(a: int,b: int):
    return a*b


def update(gemeente: list[dict], lst_nieuwe_gemeente: list[dict]):
    gemeente_new = gemeente.copy()
    update_gem = gemeente_new + lst_nieuwe_gemeente
    return update_gem

print('Hi')

gem1 = [{'GEM001' : 'AA'}]
gem2= [{'GEM001' : 'CCC'}]
inw1 = 100
inw2 = 300
test = mult(inw1, inw2)
lst_gem = update(gem1, gem2)
print(test)
print(lst_gem)