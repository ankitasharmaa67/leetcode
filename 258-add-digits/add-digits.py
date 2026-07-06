class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        
        while num>=10:
            result = 0
            while num > 0:
                result += num % 10
                num //=10
            
            num = result

        return num
                 