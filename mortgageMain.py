#!/usr/bin/env python3
from subclasses import *
from mortgage import *
import pandas as pd
import numpy as np
	

intro = input('Is this your first time using this script? ')
if intro in ['yes', 'YES', 'Yes', 'Yep', 'Y', 'YEs', 'yES', 'yeS', 'y']:
	print("This script was written as a submission to Codecademy's Final project for CS101 and as such it is not intended as financial advise nor a repository of real estate information. It is, put simply, a thought experiment for those who wish to explore what finding a loan to purchase a home might look like.")
	print("If you would like to use this script to provide meaningful information there are a few pieces of information I would suggest you gather before we begin... namely your: \n credit score \n student loan debt* (per month payment) \n credit card debt (per month payment) \n car payments \n other financial obligations (per month payment) \n *if you are in deferment you will be asked to input the total loan amount, the per month payment will be calculated at 6.5'%' interest with a 10 year repayment plan")

print('Now I will ask you to input some common information banks use to decide whether you qualify for a mortgage loan. Please note I will assume you have good credit (above 660). In future iterations of this script I will attempt to include loans for lower credit scores')

preliminary = False

while preliminary not in ['yes', 'YES', 'Yes', 'Yep', 'Y', 'YEs', 'yES', 'yeS', 'y']:
	credit_score = int(input('What is your credit score? (If you are married and including your spouse on the loan, include the lowest average FICO score between you and your spouse. ex: your three credit scores are 740, 720, and 700, and your spouse has three scores of 780, 760 and 740, you would enter 720 (740 + 720 +700)/3. HOWEVER, if you do put your spouse on the loan each time I ask for what you pay monthly for each category of debt, you must enter the total monthly you AND your spouse pay.'))
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
	preliminary = input(f'Your credit score is {credit_score} and you are able to put {down_payment} down for a house in {county}. Is this correct? ')
	
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
else:
	max_loan = int(dict_county_to_loan1[county])
	
limit = (max_loan + down_payment) * 0.93

print(f'The maximum loan in your area for the type of house you want to purchase is {max_loan}. With the ${down_payment} you have for a down payment, the priciest home that you can buy in this area is approximately {limit} when accounting for taxes and fees.')	

homeprice = int(input('What is the value of the home that you want to purchase? '))
while homeprice >= limit or homeprice in ['quit', 'Quit', 'QUIT']:
	print(f'That home is more than you can afford with your current downpayment. Banks will lend ${max_loan} for that zip code. Your down payment is {down_payment}, which means you can purchase a home under {limit} when you account for taxes and closing costs. Please note this is an estimate. You should also know, this does not take into account your credit score or your debt obligations which banks use to decide whether they will issue a loan. We will do that calculation in a bit.')
	homeprice = int(input('For now let\'s get a smaller home value... what is the value of the home that you want to purchase? (type quit to stop'))


usr_ltv = loan_to_value(homeprice, down_payment)
Int = findinterestRate(credit_score)
if usr_ltv <= .8500000:
	mortI = MI(homeprice, down_payment, credit_score) + .0008
elif usr_ltv <= .90000000:
	mortI = MI(homeprice, down_payment, credit_score) + .0016
elif usr_ltv <= .95000000:
	mortI = MI(homeprice, down_payment, credit_score) + .0024
else:
	mortI = MI(homeprice, down_payment, credit_score) + .004
	
loan = homeprice * 1.07

if mortI == None:
	payment = findPayment(loan, Int, 30)
else:
	payment = findPayment(loan, Int, 30) + (mortI * loan)/12
	
print('Now let\'s run some numbers... Here\'s where I ask you about your debt obligations in order to see what you qualify for.')

check = False
check = input('Do you have student loans? (answer yes even if they are in deferment.) (if including your spouse on the loan you must include his/her info)')
if check in ['yes', 'YES', 'Yes', 'Yep', 'Y', 'YEs', 'yES', 'yeS', 'y']:
	in_defer = input('Are your loans in deferment? (you are not actively making payments on them) ')
	if in_defer in ['yes', 'YES', 'Yes', 'Yep', 'Y', 'YEs', 'yES', 'yeS', 'y']:
		in_defer = True
		student_loans_total = input('How much do you owe? (if including your spouse on the loan you must include his/her info)')
	else:
		in_defer = False
		try:
			student_loans_monthly = input('How much do you pay each month? (if including your spouse on the loan you must include his/her info)')
		except ValueError:
			print('Please enter a number with just numbers. no commas')
			student_loans_monthly = input('How much do you pay each month? (if including your spouse on the loan you must include his/her info)')
	check = False
else:
	student_loans_monthly = 0
	in_defer = False
	check = False
	
check = input('Do you have car payments? (if including your spouse on the loan you must include his/her info)')
if check in ['yes', 'YES', 'Yes', 'Yep', 'Y', 'YEs', 'yES', 'yeS', 'y']:
	car_payment = input('What do you pay per month for your auto loans? (if including your spouse on the loan you must include his/her info)')
	check = False
else:
	car_payment = 0
	
check = input('Do you have credit card debt? (if including your spouse on the loan you must include his/her info)')
if check in ['yes', 'YES', 'Yes', 'Yep', 'Y', 'YEs', 'yES', 'yeS', 'y']:
	credit_card = input('How much do you owe?')
	credit_percent = float(input('What is the average percent of interest on your credit debt? (if including your spouse on the loan you must include his/her info)'))
	if credit_percent >= 0 and credit_percent <= 0.5:
		credit_percent *= 100
	elif credit_percent < 0 or credit_percent > 50:
		credit_percent = float(input('Please enter either a decimal between .01 and .50 OR a number between 1 and 50. What is the average percent interest on your credit debt? (if including your spouse on the loan you must include his/her info)'))
	check = False
else:
	credit_card = 1
	credit_percent = 7.5
	
check = input('Do you have any other debt obligations? (if including your spouse on the loan you must include his/her info)')
if check in ['yes', 'YES', 'Yes', 'Yep', 'Y', 'YEs', 'yES', 'yeS', 'y']:
	other = input('How much do you pay per month for these obligations? (if including your spouse on the loan you must include his/her info)')
else:
	other = 0
	
gross_pay = input('What is your annual salary before taxes? (if including your spouse on the loan you must include his/her info)')

if in_defer == True:
	usr_CD = calcDebt_defer(student_loans_total, car_payment, credit_card, other, gross_pay, credit_percent, payment = 0)
	debtratio = usr_CD.debttoincome()
	usr_CDwM = calcDebt_defer(student_loans_total, car_payment, credit_card, other, gross_pay, credit_percent, payment = 0)
	debtratiowM = usr_CDwM.debttoincome() 
else:
	usr_CD = calcDebt(student_loans_monthly, car_payment, credit_card, other, gross_pay, credit_percent, payment = 0)
	debtratio = usr_CD.debttoincome()
	usr_CDwM = calcDebt(student_loans_monthly, car_payment, credit_card, other, gross_pay, credit_percent, payment)
	debtratiowM = usr_CDwM.debttoincome()



print(f'Banks will take the total debt obligations you have each month and use that value as part of their decision making. They will use this information to determine how much money they will lend you. Your debt to income is {debtratio} before your loan is added. If you put less than 20 percent down, banks want to see your total debt to income ratio, including your mortgage, be under 45 percent. If you put 20 percent or more down that ratio increases to 50 percent.')

if debtratiowM <= 45:
	print(f'Now that you want to add a mortgage payment your debt ratio is {debtratiowM}. Which means the bank will usually give you the loan. Your payment is {payment} with an insurance rate of {Int} and mortgage insurance of {mortI}')
elif debtratiowM <= 50 and usr_ltv <= .80:
	print(f'Now that you want to add a mortgage payment your debt ratio is {debtratiowM}. Which means the bank will usually give you the loan. Your payment is {payment} with an insurance rate of {Int} and mortgage insurance of {mortI}')
else:
	print(f'It looks like you do not qualify for this loan as your debt to income ratio ({debtratiowM}) is too high. You need to save a larger down payment or look for a cheaper house.')


		