"""
Problem A. Round 3 2017 CodeJam Challenge

This module will process strings and determine if they are googlements.
Details on googlements can be found in README.md in current directory.


It will contain the following funcs:
	- decay()
	- handleEdgeCases()

"""


def decay(num_str, num_len):
	"""This function will decay the string, and count the number of possible
	numbers that the value could have degraded from

	Input:
		num_str(string): str representing a number
		len(int): int representing the length of the number (str)

	Output:
		count (int): number of possible googlements that str could have been
	"""

	# handle the edge case and initialize count value
	count = handleEdgeCases(num_str, num_len)
	if count == 1:
		return int(num_str)
	decay_flag = True
	decay_dict = dict(old=[c for c in num_str], new=[c for c in num_str])
	# chars = []
	# tmp = []
	# for c in num_str:
	# 	chars.append(c)
	# 	tmp.append(c)
	print('DECAYING {} NOW'.format(num_str))
	print('-'*80)
	print('VALUES')
	print(decay_dict['old'])
	print('-' * 80)


	while decay_flag:
		print('CHARS')
		print(decay_dict)
		if all([str(i) == decay_dict['new'][i-1] for i in range(1, num_len+1)]):
			decay_flag = False
		else:
			print('decaying...')
			for i in range(1, num_len+1):
				print('-'*80)
				print('old {}'.format(decay_dict['old']))
				print('-'*80)
				print('Index: {} has {} occurrences'.format(i, decay_dict['old'].count(str(i))))
				# count how many occurrences of i, and set that to idx val of str
				decay_dict['new'][i-1] = decay_dict['old'].count(str(i))

				print('-' * 80)
				print('new {}'.format(decay_dict['new']))
				print('-' * 80)
			count += 1
			decay_dict['old'] = decay_dict['new']

	return count


def handleEdgeCases(num_str, num_len):
	"""This function will handle edge cases for googlements

	Cases:
		- len(str) == 1 --> len(str)

	Args:
		str(string): str representing the number (possible googlement)
		num_len(int): length of number
	Returns:
		bool: bool representing whether it is edge case or not"""

	if num_len == 1:
		return True
	else:
		return False


if __name__ == '__main__':
	num_cases = int(input())
	counts_list = []

	for case in range(0, num_cases):
		print('Working on case {}'.format(case+1))
		num_str = input()
		num_str = num_str.lstrip('0')
		num_len = int(len(num_str))

		# print(num_str, num_len)
		if num_len == 1:
			# print(int(num_str))
			counts_list.append(int(num_str))
		else:
			# is_edgecase = handleEdgeCases(num_cases, num_len)
			# if is_edgecase:
			# 	counts_list.append(int(num_str.replace('0', '')))
			print('num str/len {} - {}'.format(num_str, num_len))
			cnt = decay(num_str, num_len)
			counts_list.append(cnt)
	print(counts_list, num_cases)
	print(len(counts_list) == num_cases)
	print('\n'.join(['Case #{}: {}'.format(i, counts_list[i-1]) for i in range(1, num_cases+1)]))
