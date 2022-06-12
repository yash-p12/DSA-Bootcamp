from functools import lru_cache

class Solution:
    
    #Function to find length of longest increasing subsequence.
    def longestSubsequence(self,arr,n):
        
        @lru_cache(None)
        def solve(ele,n):
            if(n==0):
                return 0
                
            if(arr[n-1]<ele):
                return max(1+solve(arr[n-1],n-1),solve(ele,n-1))
            else:
                return solve(ele,n-1)
        
        return solve(float('inf'),n)