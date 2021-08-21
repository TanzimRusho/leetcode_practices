class Solution:
    def minTimeToType(self, word: str) -> int:
        moves = 0
        prev = 'a'
        
        for ch in word:
            dif = abs(ord(ch) - ord(prev))
            moves += min(dif, 26-dif) + 1
            prev = ch
        
        return moves 

# Driver Code   
sn = Solution()    
print(sn.minTimeToType("zjpc"))


