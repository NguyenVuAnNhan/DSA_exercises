class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        def count_pairs(nums, n, mid):
            res = 0
            for i in range(n):
                res += bisect.bisect_right(nums, nums[i] + mid) - (i + 1)
            return res

        nums.sort()

        n = len(nums)
        high = nums[-1] - nums[0]

        ls_result = [nums[i+1] - nums[i] for i in range(n - 1)]

        low = min(ls_result)

        print(low)

        while low < high:
            mid = (low + high)//2
            if (count_pairs(nums, n, mid)) < k:
                low = mid + 1
            else:
                high = mid
        
        return low