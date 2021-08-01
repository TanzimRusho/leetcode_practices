class Solution:
    def minimumPerimeter(self, neededApples: int) -> int:
        for i in range(10000001):
            sum = 2 * i  * (i + 1) * (2 * i + 1)
            if sum >= neededApples:
                return 8*i
                
def main():
    solve = Solution()
    
    neededApples = int(input())
    
    ans = solve.minimumPerimeter(neededApples)
    
    print(ans)
    
if __name__ == "__main__":
    main()
