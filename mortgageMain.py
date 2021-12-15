#!/usr/bin/env python3
from subclasses import *
from mortgage import *
import pandas as pd
import numpy as np
#initialization phase

dict_zip_to_county = pd.read_csv('zip_to_county.csv', header=1, index_col=0, squeeze=True).to_dict()

dict_county_to_loan1 = pd.read_csv('county_1_2_3_4_unitloanlimits.csv', usecols=[0,1], index_col=0, header=1, squeeze=True).to_dict()
dict_county_to_loan2 = pd.read_csv('county_1_2_3_4_unitloanlimits.csv', usecols=[0,2], index_col=0, header=1, squeeze=True).to_dict()
dict_county_to_loan3 = pd.read_csv('county_1_2_3_4_unitloanlimits.csv', usecols=[0,3], index_col=0, header=1, squeeze=True).to_dict()
dict_county_to_loan4 = pd.read_csv('county_1_2_3_4_unitloanlimits.csv', usecols=[0,4], index_col=0, header=1, squeeze=True).to_dict()

for i in dict_county_to_loan1.keys():
	dict_county_to_loan1[i] = dict_county_to_loan1[i].replace('$', '').replace(' ','').replace(',','')
for i in dict_county_to_loan2.keys():
	dict_county_to_loan2[i] = dict_county_to_loan2[i].replace('$', '').replace(' ','').replace(',','')
for i in dict_county_to_loan3.keys():
	dict_county_to_loan3[i] = dict_county_to_loan3[i].replace('$', '').replace(' ','').replace(',','')
for i in dict_county_to_loan4.keys():
	dict_county_to_loan4[i] = dict_county_to_loan4[i].replace('$', '').replace(' ','').replace(',','')
	
print(int(dict_county_to_loan1['CALHOUN COUNTY']))

intro = input('Is this your first time using this script? ')
if intro in ['yes', 'YES', 'Yes', 'Yep', 'Y', 'YEs', 'yES', 'yeS', 'y']:
	print("This script was written as a submission to Codecademy's Final project for CS101 and as such it is not intended as financial advise nor a repository of real estate information. It is, put simply, a thought experiment for those who wish to explore what finding a loan to purchase a home might look like.")
	print("If you would like to use this script to provide meaningful information there are a few pieces of information I would suggest you gather before we begin... namely your: \n credit score \n student loan debt* (per month payment) \n credit card debt (per month payment) \n car payments \n other financial obligations (per month payment) \n *if you are in deferment you will be asked to input the total loan amount, the per month payment will be calculated at 6.5'%' interest with a 10 year repayment plan")

print('Now I will ask you to input some common information banks use to decide whether you qualify for a mortgage loan. Please note I will assume you have good credit (above 660). In future iterations of this script I will attempt to include loans for lower credit scores')

preliminary = False

while preliminary not in ['yes', 'YES', 'Yes', 'Yep', 'Y', 'YEs', 'yES', 'yeS', 'y']:
	credit_score = int(input('What is your credit score? '))
	while credit_score <= 660:
		print('Please enter a credit score that is higher than 660, you may want to raise your credit before seeking a mortgage.')
		credit_score = int(input('What is your credit score? '))
	try:
		down_payment = int(input('How much money do you have saved for a downpayment? '))
	except ValueError:
		print('You must enter a numerical value without a comma ex. 20000')
		down_payment = int(input('How much money do you have saved for a downpayment? '))
	check = input('Are you receiving any money to help with the downpayment? (must include a letter stating the giver does not expect repayment. ')
	if check in ['yes', 'YES', 'Yes', 'Yep', 'Y', 'YEs', 'yES', 'yeS', 'y']:
		try:
			down_payment += int(input('How much will you receive?' ))
		except ValueError:
			print("You must enter a numerical value without a comma ex. 20000")
			down_payment += int(input('How much will you receive?' ))
	try:
		zip_code = int(input('Enter the zip code where you want to purchase a house. '))
	except ValueError:
		print("You must enter a numerical value.")
		zip_code = int(input('Enter the zip code where you want to purchase a house. '))
	county = dict_zip_to_county[zip_code].upper()
	preliminary = input(f'Your credit score is {credit_score} and you are able to put {down_payment} down for a house in {county}. Is this correct?')
try:
	unit = int(input('How many units are in the home you want to purchase? '))
except ValueError:
	print('Enter a numerical value please. ex. 2')
	unit = int(input('How many units are in the home you want to purchase? '))
	
if unit == 1:
	max_loan = int(dict_county_to_loan1[county])
elif unit == 2:
	max_loan = int(dict_county_to_loan2[county])
elif unit == 3:
	max_loan = int(dict_county_to_loan3[county])
elif unit == 4:
	max_loan = int(dict_county_to_loan4[county])

limit = (max_loan + down_payment) * 0.93

print(f'The maximum loan in your area for the type of house you want to purchase is {max_loan}. With the ${down_payment} you have for a down payment, the priciest home that you can buy in this area is approximately {limit} when accounting for taxes and fees.')
	
print('Now let\'s run some numbers... Here\'s where I ask you about your debt obligations in order to see what you qualify for.')

check = False
check = input(print('Do you have student loans? (answer yes even if they are in deferment.)'))
if check in ['yes', 'YES', 'Yes', 'Yep', 'Y', 'YEs', 'yES', 'yeS', 'y']:
	in_defer = input(print('Are your loans in deferment? (you are not actively making payments on them.'))
	if in_defer in ['yes', 'YES', 'Yes', 'Yep', 'Y', 'YEs', 'yES', 'yeS', 'y']:
		in_defer = True
	elif in_defer in ['No', 'NO', 'n', 'N', 'idk', 'nO', '0', 'nah', 'na', 'no']:
		in_defer = False


#proccessing phase

#termination phase

		