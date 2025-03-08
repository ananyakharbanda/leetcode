class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        output = []
        minNum = 0
        for x in range(len(ratings)):
            output.append(1)
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i-1]:
                output[i] = output[i-1] + 1
        
        for j in range(len(ratings)-2, -1, -1):
            if ratings[j] > ratings[j+1]:
                output[j] = max(output[j+1] + 1, output[j])
        for y in output:
            minNum += y
        return minNum