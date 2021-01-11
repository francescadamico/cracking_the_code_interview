'''
You are building a diving board by placing a bunch of planks of wood end-to-end. There are two types of planks, one of length 'shorter' and one of length 'longer'. You must use exactly k planks of wood. Write a method to generate all possible length for the diving board.
'''

def board_lengths(s, l, k):

	lengths = [i * s + (k - i) * l for i in range(k + 1)]

	return lengths

s = 10
l = 30

k = 100

print(board_lengths(s, l, k))

# 120, 100, 80, 60, 40

