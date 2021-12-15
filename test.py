#!/usr/bin/env python3

from subclasses import *
from mortgage import *
import pandas as pd
import numpy as np
#initialization phase

dict_zip_to_county = pd.read_csv('zip_to_county.csv', header=1, index_col=0, squeeze=True).to_dict()

dict_county_to_loan1 = pd.read_csv('county_1_2_3_4_unitloanlimits.csv', usecols=[0,1], index_col=0, header=1, squeeze=True).to_dict()

for i in dict_county_to_loan1.keys():
	dict_county_to_loan1[i] = dict_county_to_loan1[i].replace('$', '').replace(' ','').replace(',','')
	
print(dict_zip_to_county[95120].upper())
print(dict_county_to_loan1[dict_zip_to_county[95120].upper()])

