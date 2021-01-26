'''
Given a list of people with birth and death years in it, implement a method to compute the year with the most number of people alive. You may assume that all people were born between 1900 and 2000 included. If a person was alive during any portion of that year, they should be included in that year's count. For example, Person(birth = 1908, death = 1909) should be included for both 1908 and 1909.
'''
from collections import defaultdict


class Person:
	def __init__(self, b, d):
		self.birth = b
		self.death = d


def most_populated(P):
	
	d = defaultdict(int)
	most_pop = (1900, 0)
	
	"""
	Split responsabilities and make it more pythonic:
	for p in P:
	    for y in range(p.birth, p.death + 1):
                d[y] += 1
	return max(d, key=d.get)
	"""
	
	for p in P:
		for y in range(p.birth, p.death + 1):		
			d[y] += 1
			if d[y] > most_pop[1]:
				most_pop = (y, d[y])
	
	return most_pop



p1 = Person(1900, 2000)
p2 = Person(1901, 1999)
p3 = Person(1902, 1902)
p4 = Person(1903, 1903)


P = [p1, p2, p3, p4]

print(most_populated(P))
