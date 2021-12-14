#!/usr/bin/env python3
from decimal import Decimal, getcontext

def findPayment(loan, interest_rate, years_of_loan):
	""" takes a loan, interest rate r and m total months of the payment"""
	r = (interest_rate / 100) / 12
	m = years_of_loan * 12
	return (r * loan * ((1 + r)**m) / ((1 + r)** m - 1))

getcontext().prec = 5

def loan_to_value(home_value, down_payment):
	return Decimal((home_value - down_payment) / home_value)
	

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
	
class findInterestRate(object):
	def __init__(self, home_value, down_payment, credit_score):
		self.cs = credit_score
		self.ltv = loan_to_value(home_value, down_payment)
		self.dp = down_payment
		self.hv = home_value
		
	def preQualify_premrate(self):
		if self.hv - self.dp > 914000:
			return False
		elif self.ltv >= .91:
			return False
		elif self.cs < 680:
			return False
		
class calcDebt(object):
	def __init__(self, student_loans_monthly = 0, student_loans_total = 0, car_payment = 0, in_deffer = False, credit_card = 0, other = 0, gross_pay = 50000):
		self.slm = student_loans_monthly
		self.slt = student_loans_total
		self.cp = car_payment
		self.dfer = in_deffer
		self.cc = credit_card
		self.oth = other
		self.gp = gross_pay
	
	def debttoincome(self):
		if self.dfer == False:
			return (self.slm + self.cp + self.cc + self.oth)/(self.gp / 12)
		elif self.dfer == True:
			return (findPayment(self.slt, 6.5, 10) + self.cp + self.cc + self.oth)/(self.gp / 12)
		
	
		
		
