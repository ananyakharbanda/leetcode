class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def get_next(num):
            sum_digits = 0
            while num > 0:
                digit = num % 10
                sum_digits += digit ** 2
                num //= 10
            return sum_digits
        
        slow, fast = n, get_next(n)
        
        while fast != 1 and slow != fast:
            slow = get_next(slow)  
            fast = get_next(get_next(fast))  
        
        return fast == 1
