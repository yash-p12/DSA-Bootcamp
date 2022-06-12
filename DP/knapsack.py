from functools import lru_cache

class Solution:
    
    #Function to return max value that can be put in knapsack of capacity W.
    def knapSack(self,W, wt, val, n):
        @lru_cache(maxsize=None)
        def solve(W,n):
            if(n==0 or W==0):
                return 0
            
            if(wt[n-1]<=W):
                return max(val[n-1]+solve(W-wt[n-1],n-1),
                solve(W,n-1))
            if (wt[n-1]>W):
                return solve(W,n-1)
        # code here
        return solve(W,n)