#!/usr/bin/env python3
import os
"""
given an integer N, return the smallest integer greater than N, sum of whose digists is twice as big as the sum of digits of N,
Examples:
1.Given N = 14, the function should return 19, The sum of digits of 19(1 + 9 = 10) is twice as big as sum of digits of 14(1 + 4 = 5).
2.Given N = 99, the function should return 9999.
...
codility challenge
"""
def biggest_sum(num:int):
	""" This returns the biggest sum """
	*str_num, = str(num)
	sum_num = sum(map(int, str_num)) #sum the input value
	twi_num  = 2 * sum_num
	total_str = '0'
	find_str = '1'
	res = 0
	done = False
	while not done:
		for i in range(10):
			nd_num = sum(map(int,[*str(total_str)])) #sum the total value
			find_num = nd_num + int(find_str)
			if find_num + i == twi_num:
				if (int(find_str) == 1 and i == 8) or (int(find_str) == 8 and i == 1): # check if the two match an entry for 9 at end case(such as 18 or 81)
					res = total_str + '9' ## then add 9 instead of 18 or 81 ex:(99918 becomes 9999)
				else:
					res = total_str + find_str + str(i)
				res = int(res)
				if res < num: ## checks if the result is greater than the number
					continue
				found = True
				done = True
				
			if i == 9 and int(find_str) < 10:
				find_str = str(int(find_str) + 1)
				
			if i == 9 and find_str == '9':
				total_str += "9"
				find_str = '1'

	return res
	
if __name__ =="__main__":

	val = int(input("enter value, 0 or -1 to cancle: "))
	if val != 0 or val != -1:
		print(biggest_sum(val))
	else:
		os.exit()
	
