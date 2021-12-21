#!/usr/bin/env python3
from decimal import Decimal, getcontext
import pandas as pd
import numpy as np

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

def findPayment(loan, interest_rate, years_of_loan):
	""" takes a loan, interest rate r and m total months of the payment"""
	r = (interest_rate / 100) / 12
	m = years_of_loan * 12
	return (r * loan * ((1 + r)**m) / (((1 + r)** m) - 1))

getcontext().prec = 5

def loan_to_value(home_value, down_payment):
	return Decimal((home_value - down_payment) / home_value)

def findinterestRate(credit_score):
	if credit_score >= 760:
		return .0333
	if credit_score >= 740:
		return .033
	if credit_score >= 720:
		return .03405
	if credit_score >= 700:
		return .03616
	if credit_score >= 680:
		return .03625
	if credit_score >= 660:
		return .03625
	
def MI(home_value, down_payment, credit_score):
	ltv = loan_to_value(home_value, down_payment)
	if ltv <= .8000000000:
		return None
	else:
		if credit_score >= 760:
			return .0017
		if credit_score >= 740:
			return .0022
		if credit_score >= 720:
			return .0029
		if credit_score >= 700:
			return .0036
		if credit_score >= 680:
			return .0049
		if credit_score >= 660:
			return .0072

class Mortgage(object):
	def __init__(self, loan, annRate, years):
		self.loan = loan
		self.rate = annRate
		self.years = years
		self.paid = [0.0]
		self.outstanding = [loan]
		self.payment = findPayment(loan, annRate, years)
		self.legend = None
	
	def makePayment(self):
		self.paid.append(self.payment)
		reduction = self.payment - self.outstanding[-1] * self.rate
		self.outstanding.append(self.oustanding[-1] - reduction)
	
	def getTotalPaid(self):
		return sum(self.paid)
	
	def __str__(self):
		return self.legend
	
		
class calcDebt_defer(object):
	def __init__(self, student_loans_total = 0, car_payment = 0, credit_card = 1, other = 0, gross_pay = 50000, credit_percent = 7.5, payment = 0):
		self.slt = float(student_loans_total)
		self.cp = float(car_payment)
		self.cc = float(credit_card)
		self.credp = float(credit_percent)
		self.oth = float(other)
		self.gp = float(gross_pay)
		self.p = float(payment)
		
	def debttoincomedefer(self):
		return (max((findPayment(self.slt, 6.5, 10) + self.cp + findPayment(self.cc, self.credp, .83333) + self.oth + self.p), 1)/(self.gp / 12)) * 100
		
class calcDebt(object):
	def __init__(self, student_loans_monthly = 0, car_payment = 0, credit_card = 1, other = 0, gross_pay = 50000, credit_percent = 7.5, payment = 0):
		self.slm = float(student_loans_monthly)
		self.cp = float(car_payment)
		self.cc = float(credit_card)
		self.credp = float(credit_percent)
		self.oth = float(other)
		self.gp = float(gross_pay)
		self.p = float(payment)
		
	def debttoincome(self):
		return (max((self.slm + self.cp + findPayment(self.cc, self.credp, .83333) + self.oth + self.p), 1)/(self.gp / 12)) * 100