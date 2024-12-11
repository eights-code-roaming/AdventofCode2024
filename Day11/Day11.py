import os
import sys
from collections import deque

data = '''3028 78 973951 5146801 5 0 23533 857'''

test = '''0 1 10 99 999'''

test2 = '''125 17'''

memoize = dict()

class stones:
	def __init__(self, stone_str):
		self.stones = [int(x) for x in stone_str.split(' ')]
		self.stones = deque(self.stones)

	def print(self):
		print(self.stones)

	def update(self):
		new_stones = deque()

		for s in self.stones:
			if s == 0:
				new_stones.append(1)
			elif len(str(s)) % 2 == 0:
				s2 = str(s)
				first = s2[:int(len(s2) / 2)]
				second = s2[int(len(s2) / 2):]

				new_stones.append(int(first))
				new_stones.append(int(second))
			else:
				new_stones.append(s * 2024)

		self.stones = new_stones

s = stones(data)

for k in range(0, 75):
	#print(k)
	#s.print()
	s.update()

print('Part 1:', len(s.stones))

