import os
import sys
from collections import Counter

test = """
3   4
4   3
2   5
1   3
3   9
3   3"""

data = []

with open('../AdventSecrets/2024/1/1.input.txt', 'r') as fh:
	for line in fh:
		line = line.rstrip().split()
		data.append((int(line[0]), int(line[1])))

test = [(int(x.split()[0]), int(x.split()[1])) for x in test.lstrip().rstrip().split('\n')]

first_list = sorted([x[0] for x in data])
second_list = sorted([x[1] for x in data])

#print(first_list)
#print(second_list)

total = 0
for z, x in enumerate(first_list):
	y = abs(first_list[z] - second_list[z])
	total += y

print('Part 1:', total)

c = Counter(second_list)
total2 = 0
for entry in first_list:
	z = entry * c[entry]
	total2 += z

print('Part 2:', total2)

