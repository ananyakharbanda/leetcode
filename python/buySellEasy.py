class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy = 0
        sold = 0
        first = True

        for i in prices:
            if first:
                buy = i
                first = False
            elif i < buy:
                buy = i
            elif i - buy > sold:
                sold = i - buy
        return sold