#User function Template for python3

class Solution:
    def multiply(self, arr):
        n = len(arr)
        mid = n // 2
        left_sum, right_sum = 0, 0
        for i in range(n):
            if i < mid:
                left_sum += arr[i]
            else:
                right_sum += arr[i]
        return left_sum * right_sum
