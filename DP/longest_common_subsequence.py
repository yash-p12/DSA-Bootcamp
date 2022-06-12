from functools import lru_cache

class Solution:
    #Function to find the length of longest common subsequence in two strings.
    def lcs(self,x,y,s1,s2):
        
        @lru_cache(None)
        def solve(x,y):
            if(x==0 or y==0):
                return 0
                
            if(s1[x-1]==s2[y-1]):
                return max(1+solve(x-1,y-1),solve(x-1,y-1))
            
            else:
                return max(solve(x,y-1),solve(x-1,y))
        
        return solve(x,y)