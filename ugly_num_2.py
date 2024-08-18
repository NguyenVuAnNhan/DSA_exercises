class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ugly_numbers = [1] * n
      
        index_2, index_3, index_5 = 0, 0, 0
      
        for i in range(1, n):
            next_2 = ugly_numbers[index_2] * 2
            next_3 = ugly_numbers[index_3] * 3
            next_5 = ugly_numbers[index_5] * 5
          
            ugly_numbers[i] = min(next_2, next_3, next_5)
          
            if ugly_numbers[i] == next_2:
                index_2 += 1
            if ugly_numbers[i] == next_3:
                index_3 += 1
            if ugly_numbers[i] == next_5:
                index_5 += 1
      
        return ugly_numbers[n - 1]