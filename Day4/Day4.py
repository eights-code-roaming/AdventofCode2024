import os
import sys
import numpy as np

data = []
with open('../AdventSecrets/2024/4/4.input.txt', 'r') as fh:

	for line in fh:
		line = line.rstrip()
		line = list(line)
		data.append(line)

test = '''MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX'''

test2 = [list(x) for x in test.split('\n')]

words = np.matrix(data)

def check(y, x, matrix):
	# y, x coordinates to add to for check
	direct = {'N': [[-1, 0], [-2, 0], [-3, 0]],
			  'NE': [[-1, 1], [-2, 2], [-3, 3]],
			  'E': [[0, 1], [0, 2], [0, 3]],
			  'SE': [[1, 1], [2, 2], [3, 3]],
			  'S': [[1, 0], [2, 0], [3, 0]],
			  'SW': [[1, -1], [2, -2], [3, -3]],
			  'W': [[0, -1], [0, -2], [0, -3]],
			  'NW': [[-1, -1], [-2, -2], [-3, -3]]}

	counter = 0
	max_y, max_x = matrix.shape

	for d in direct:

		char_list = []

		for char in direct[d]:
			bounds = False
			y1 = char[0]
			x1 = char[1]

			new_y = y + y1
			new_x = x + x1

			if (new_y < 0) or (new_y > max_y - 1) or (new_x < 0) or (new_x > max_x - 1) :
				bounds = True

			if bounds:
				char_list.append('F')
			else:
				char_list.append(matrix[new_y, new_x])

		#print(y, x, char_list)
		if 'F' in char_list:
			continue
		elif ''.join(char_list) == 'MAS':
			counter += 1

	return counter

ymax, xmax = words.shape

total_xmax = 0

for y in range(0, ymax):
	for x in range(0, xmax):
		if words[y, x] == 'X':
			xmax_count = check(y, x, words)
			total_xmax += xmax_count
			#print(y, x, xmax_count)

print('Part 1:', total_xmax)

def check2(y, x, matrix):
	direct = {'NE': [-1, 1],
			  'SE': [1, 1],
			  'SW': [1, -1],		  
			  'NW': [-1, -1]}

	max_y, max_x = matrix.shape
	char_list = []
	
	for d in direct:
		char = direct[d]

		bounds = False
		y1 = char[0]
		x1 = char[1]

		new_y = y + y1
		new_x = x + x1

		if (new_y < 0) or (new_y > max_y - 1) or (new_x < 0) or (new_x > max_x - 1) :
			bounds = True

		if bounds:
			char_list.append('F')
		else:
			char_list.append(matrix[new_y, new_x])

	if 'F' in char_list:
		return 0

	valid = ['MMSS', 'SSMM', 'MSSM', 'SMMS']
	if ''.join(char_list) in valid:
		return 1
	else:
		return 0

total_xmax2 = 0

for y in range(0, ymax):
	for x in range(0, xmax):
		if words[y, x] == 'A':
			xmax_count = check2(y, x, words)
			total_xmax2 += xmax_count
			#print(y, x, xmax_count)

print('Part 2:', total_xmax2)



