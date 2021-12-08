#!/usr/bin/env python3
from mortgage import *

class Fixed(Mortgage):
	def __init__(self, loan, r, years):
		Mortgage.__init__(self, loan, r, years)
		self.legend = 'Fixed, ' + str(r) + '%'

class FixedWithPts(Mortgage):
	def __init__(self, loan, r, years, pts):
		Mortgage.__init__(self, loan, r, years)
		self.pts = pts
		self.paid = [loan * (pts/100)]
		self.legend = (f'Fixed, {r} %, {pts} points')
		
class 