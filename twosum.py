class Solution():
    def twoSum(self,nums,target):
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return (i, j)
        return []
def main():
    n = int(input("Enter the number of elements:"))
    nums = list(map(int,input("Enter the nums:").split()))
    target = int(input("Enter Target Element:"))
    obj = Solution()
    result = obj.twoSum(nums,target)
    print(result)
if __name__ == "__main__":
    main()