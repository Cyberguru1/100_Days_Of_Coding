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
	find_str = '1'
	res = 0
	done = False
	while not done:
			find_str = str(int(find_str) + 1)
			find_num = sum(map(int,[*str(find_str)])) #sum the total value
			if find_num  == twi_num:
				res = int(find_str)
				if res < num: ## checks if the result is greater than the number
					continue
				done = True
	return res
	
if __name__ =="__main__":

	val = int(input("enter value, 0 or -1 to cancel: "))
	if val != 0 or val != -1:
		print(biggest_sum(val))
	else:
		os.exit()
	
