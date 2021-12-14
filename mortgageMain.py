#!/usr/bin/env python3
from subclasses import *
from mortgage import *
#initialization phase
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
	down_payment = int(input('How much money do you have saved for a downpayment? '))
	check = input('Are you receiving any money to help with the downpayment? (must include a letter stating the giver does not expect repayment. ')
	if check in ['yes', 'YES', 'Yes', 'Yep', 'Y', 'YEs', 'yES', 'yeS', 'y']:
		down_payment += int(input('How much will you receive?' ))
	preliminary = input(f'Your credit score is {credit_score} and you are able to put {down_payment} down for a house. Is this correct?')

#proccessing phase

#termination phase

		