# This also must be a completed solution to your problem.
class Solution(object):
    def numberOfMatches(n):
        """
        :type n: int
        :rtype: int
        """
        return n-1
        # current = n
        # played = 0
        # while current > 1:
        #     if current % 2 == 0:
        #         played += current/2
        #         current = current/2
        #     elif current % 2 == 1:
        #         played += (current -1)/2
        #         current = (current -1)/(2+1)
        # return played
    n = input("Enter number of teams: ")
    print numberOfMatches(n)