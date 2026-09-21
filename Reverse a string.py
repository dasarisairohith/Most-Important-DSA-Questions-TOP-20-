class Solution():
    def reverse(self,s):
        n = len(s)
        return s[::-1]
def  main():
    s = input()
    solution = Solution()
    result = solution.reverse(s)
    print(result)
if __name__ == "__main__":
    main()
