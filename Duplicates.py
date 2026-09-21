class Solution():
 def duplicates(self,nums):
   seen = set()

   for ch in nums:
     if ch in seen:
      return True

     seen.add(ch)
   return False
def main():
  arr = list(map(int,input().split()))
  solution = Solution()
  result = solution.duplicates(arr)
  print(result)
if __name__ =="__main__":
  main()
