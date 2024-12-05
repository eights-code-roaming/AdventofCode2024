import os
import sys
from collections import defaultdict
import math

rules = []
order = []
with open('../AdventSecrets/2024/5/5.input.txt', 'r') as fh:
	rules, orders = fh.read().split('\n\n')

test='''47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47'''

#rules, orders = test.split('\n\n')

rule_dict = defaultdict(list)
orders = [x.split(',') for x in orders.split('\n')]

for r in rules.split('\n'):
	first, second = r.split('|')
	rule_dict[first].append(second)


#for r in rule_dict:
#	print(r, rule_dict[r])

middles = []
incorrect = []
for o in orders:
	correct = True
	#print('Order', o)
	for z, e in enumerate(o):
		if e in rule_dict:
			r = rule_dict[e]
			#print(e, '-', r)

			right = o[z + 1:]
			left = o[:z]

			for r2 in r:
				#print(r2, left, r2 in left)
				if r2 in left:
					correct = False
					if o not in incorrect:
						incorrect.append(o)
					break


	#print(','.join(o), correct)
	if correct:
		midpoint = math.floor(len(o) / 2.0)
		midpoint = int(midpoint)
		middles.append(int(o[midpoint]))

print('Part 1:', sum(middles))

middles2 = []

def corrected(x, rules):
	correct = True
	for z, e in enumerate(x):
		if e in rules:
			r = rules[e]

			right = x[z + 1:]
			left = x[:z]

			for r2 in r:
				if r2 in left:
					correct = False
					break

	return correct

for i in incorrect:

	i2 = i.copy()
	fix = True

	while fix:
		#print('I2', i2)
		for z, e in enumerate(i2):
			r = rule_dict[e]

			right = i2[z + 1:]
			left = i2[:z]
			left_swap = None

			for r2 in r:
				if r2 in left:
					left_swap = i2.index(r2)
					break
			#print(e, r, r2, left, right, r2 in left)
			if left_swap is not None:
				swap = i2[left_swap]

				i2[z] = swap
				i2[left_swap] = e
			else:
				cor = corrected(i2, rule_dict)
				#print(cor)
				if cor:
					fix = False

	#print('Final', i2)
	midpoint = math.floor(len(i2) / 2.0)
	midpoint = int(midpoint)
	middles2.append(int(i2[midpoint]))

print('Part 2:', sum(middles2))