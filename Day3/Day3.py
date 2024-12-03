import os
import sys
import re
from functools import reduce
from collections import deque

with open('../AdventSecrets/2024/3/3.input.txt', 'r') as fh:
	data = fh.read()

	test = 'xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))'

	def compute(x):
		res = re.findall(r'(mul\(\d+,\d+\))', x)

		sums = []
		if res:
			for entry in res:
				res2 = re.findall(r'\d+', entry)


				if res2:
					val = [int(x) for x in res2]
					prod = reduce(lambda x,y: x*y, val, 1)
					sums.append(prod)

		return(sum(sums))
	print('Part 1', compute(data))

	test2 = '''xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))'''

	input_string = data

	donts = [m.end() for m in re.finditer('''don't\(\)''', input_string)]
	dos = [m.start() for m in re.finditer('''do\(\)''', input_string)]
	dos = [0] + dos

	#print(donts)
	#print(dos)

	donts = deque(donts)
	dos = deque(dos)
	end = -1
	filt = ''

	while len(dos) > 0:
		start = dos.popleft()

		if len(donts) > 0 and start > end:
			while end < start:
				try:
					end = donts.popleft()
				except IndexError:
					end = len(input_string)
			#print(start, end)
		elif start < end:
			# dos appear multiply before a dont
			continue
		
		#elif len(donts) == 0 and start > end:
		#	end = len(input_string)

		filt += input_string[start:end]

		#print(input_string[start:end])

	#print(filt)
	print('Part 2:', compute(filt))
