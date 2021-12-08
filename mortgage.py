#!/usr/bin/env python3

def findPayment(loan, interest_rate, years_of_loan):
	""" takes a loan, interest rate r and m total months of the payment"""
	r = (interest_rate / 100) / 12
	m = years_of_loan * 12
	return (r * loan * ((1 + r)**m) / ((1 + r)** m - 1))

print(findPayment(200000, 6.5, 30))

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
	

		<#code#>