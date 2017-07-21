import sys

#test case:
#1000000003->0
#1534236469->0
#-34982->-28943
#345421->124543

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        print(sys.maxint) 	# defalut max value of integer of Python

        if x > 0:			# 1. positive integer
			RX = str(x)[::-1]
			reverseInt = int(RX)
			# check reversed integer is 32-bit signed integer
			if isOverflow(reverseInt):
				reverseInt = 0
        elif x < 0:			# 2. negivate integer
        	reverse = int(str(x)[1:][::-1])
        	if isOverflow(reverse):
        		reverseInt = 0
        	else:
        		reverseInt = reverse*(-1)
        	# print(reverseInt)
        elif x == 0:		# 3. input is 0
        	reverseInt = 0

        return reverseInt

def isOverflow(x):
	# check wether x is 32-bit signed integer 
	# minValue: -2147483647 = 2^32-1
	# maxValue: 2147483647 = -(2^32 -1)
	isOverflow = False
	if not (x >= -2147483647) & (x <= 2147483647):
		isOverflow = True
	return isOverflow

result = Solution.reverse(Solution(), -34982)
print(result)
