"""
File: boggle.py
Name:
----------------------------------------
TODO:
"""

import time

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'


def main():
	"""
	TODO:
	"""

	first_word = {}
	first_row = input('1 row of letters: ')
	if check(first_row, first_word):
		second_row = input('2 row of letters: ')
		if check1(second_row, first_word):
			third_row = input('3 row of letters: ')
			if check2(third_row, first_word):
				fourth_row = input('4 row of letters: ')
				if check3(fourth_row, first_word):
					start = time.time()
					read_dictionary(first_word)
					end = time.time()
					print('----------------------------------')
					print(f'The speed of your boggle algorithm: {end - start} seconds.')


def check(first_row, first_word):
	for i in range(len(first_row)):
		if i % 2 == 0:
			first_word[i+11] = first_row[i]
	if len(first_row) != 7:
		print('Illegal input')
		return False
	else:
		a = first_row.split()
		if len(a) != 4:
			print('Illegal input')
			return False
	return True


def check1(second_row, first_word):
	for i in range(len(second_row)):
		if i % 2 == 0:
			first_word[i+21] = second_row[i]
	if len(second_row) != 7:
		print('Illegal input')
		return False
	else:
		a = second_row.split()
		if len(a) != 4:
			print('Illegal input')
			return False
	return True


def check2(third_row, first_word):
	for i in range(len(third_row)):
		if i % 2 == 0:
			first_word[i+31] = third_row[i]
	if len(third_row) != 7:
		print('Illegal input')
		return False
	else:
		a = third_row.split()
		if len(a) != 4:
			print('Illegal input')
			return False
	return True

def check3(fourth_row, first_word):
	for i in range(len(fourth_row)):
		if i % 2 == 0:
			first_word[i+41] = fourth_row[i]
	if len(fourth_row) != 7:
		print('Illegal input')
		return False
	else:
		a = fourth_row.split()
		if len(a) != 4:
			print('Illegal input')
			return False
	return True


def read_dictionary(first_word):
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	with open(FILE,'r') as f:
		word_d = []
		for line in f:
			line = line.strip()
			num = len(line)
			if 7 > num >= 4:
				word_d.append(line)
	word_s = []
	ans = ''
	ans_list = []
	for i in range(len(word_d)):
		check_word = word_d[i]
		for num, letter in first_word.items():
			if check_word[0] in letter:
				word_s.append(check_word)
	word = {}
	for num, letter in first_word.items():
		word[num] = letter
	for num, letter in first_word.items():
		check_letter(letter,num,first_word,word,word_s,ans,ans_list)
	print(f"There are: {len(ans_list)} words in total.")


def check_letter(letter,num,first_word,word,word_s,ans,ans_list):
	sub_s = ''
	num_s = []
	ans += letter
	if ans in word_s and ans not in ans_list:
		ans_list.append(ans)
		print(f'Found: "{ans}"')
	else:
		# 上
		if num > 20:
			sub_s += word[num-10]
			num_s.append(num-10)
		# 下
		if num < 40:
			sub_s += word[num + 10]
			num_s.append(num + 10)
		# 左
		if num % 10 != 1:
			sub_s += word[num - 2]
			num_s.append(num - 2)
		# 右
		if num % 10 != 7:
			sub_s += word[num + 2]
			num_s.append(num + 2)
		#左上
		if num % 10 != 1 and num > 20:
			sub_s += word[num - 12]
			num_s.append(num - 12)
		#右上
		if num % 10 != 7 and num > 20:
			sub_s += word[num - 8]
			num_s.append(num - 8)
		#左下
		if num % 10 != 1 and num < 40:
			sub_s += word[num + 8]
			num_s.append(num + 8)
		#右下
		if num % 10 != 7 and num < 40:
			sub_s += word[num + 12]
			num_s.append(num + 12)
		word_list = []
		cur = ans
		for i in range(len(sub_s)):
			ch = sub_s[i]
			cur += ch
			a = num_s[i]
			for wor in word_s:
				if wor.startswith(cur):
					word_list.append(wor)
					word[num] = '0'
					check_letter(ch, a, first_word,word, word_list, ans,ans_list)
					word[num] = first_word[num]
			cur = ans




def has_prefix(ans, sub_s, word_s):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	cur = ans
	word_list = []
	for i in range(len(sub_s)):
		ch = sub_s[i]
		cur += sub_s[i]
		for word in word_s:
			if word.startswith(cur):
				word_list.append(word)
	print(word_list)
	return word_list







if __name__ == '__main__':
	main()
