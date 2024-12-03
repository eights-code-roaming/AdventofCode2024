import os
import sys
from collections import Counter

test="""
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
"""

test = test.rstrip().lstrip().split('\n')
test = [list(map(int, x.split())) for x in test]

#print(test)

data = []
with open('../AdventSecrets/2024/2/2.input.txt', 'r') as fh:
	for line in fh:
		line = line.rstrip().split()
		line = [int(x) for x in line]
		data.append(line)

safe_reactor = []
for x in data:
	d = [x[y] - x[y + 1] for y in range(0, len(x) - 1)]
	if 0 in d:
		safe_reactor.append(False)
		continue

	safe_bool = []
	if d[0] < 0:
		# Decreasing list.
		for z in d:
			if abs(z) > 3:
				safe_bool.append(False)
				continue
			elif z > 0:
				safe_bool.append(False)
				continue
	else:
		# Increasing list.
		for z in d:
			if z > 3:
				safe_bool.append(False)
				continue
			elif z < 0:
				safe_bool.append(False)
				continue

	if False in safe_bool:
		safe_reactor.append(False)
	else:
		safe_reactor.append(True)

	#print(x)
	#print(d)
	#print(safe_reactor[-1])

c = Counter(safe_reactor)

print('Part 1', c[True])

def determine_safe(x):
	d = [x[y] - x[y + 1] for y in range(0, len(x) - 1)]
	safe_bool = []

	if d[0] < 0:
		# increasing list.
		for z in d:
			if abs(z) > 3:
				safe_bool.append(False)
				continue
			elif z > 0:
				safe_bool.append(False)
				continue
			elif z == 0:
				safe_bool.append(False)
				continue
			else:
				safe_bool.append(True)
	else:
		# decreasing list.
		for z in d:
			if z > 3:
				safe_bool.append(False)
				continue
			elif z < 0:
				safe_bool.append(False)
				continue
			elif z == 0:
				safe_bool.append(False)
				continue
			else:
				safe_bool.append(True)

	#print(x)
	#print(d)
	#print(safe_bool)
	return(safe_bool)

safe_reactor2 = []

for z, x in enumerate(data):
	#print('---Report', z)
	bool_results = determine_safe(x)
	#print(bool_results)
	
	if False in bool_results:
		pos = bool_results.index(False)
		#print(pos)

		y = x.copy()
		z = x.copy()
		w = x.copy()
		y.pop(pos)
		z.pop(pos + 1)
		w.pop(pos - 1)

		#print('2')
		bool_results2 = determine_safe(y)
		#print('3')
		bool_results3 = determine_safe(z)
		#print('4')
		bool_results4 = determine_safe(w)

		fix = False
		if False not in bool_results2:
			fix = True
		elif False not in bool_results3:
			fix = True
		elif False not in bool_results4:
			fix = True

		#print('Fix', fix)
		if fix:
			safe_reactor2.append(True)
			#print('Safe')
		else:
			safe_reactor2.append(False)
			#print('Fail')
	else:
		safe_reactor2.append(True)
		#print('Safe')

c2 = Counter(safe_reactor2)
print('Part 2', c2[True])
