import timeit
#User function Template for python3
class Solution:
    # Function to find values in array equal to their indices
    def valueEqualToIndex(self, arr):
        if not (1 <= len(arr) <= 10**5):
            return []
        for val in arr:
            if not (1 <= val <= 10**6):
                return []
        # solution 1
        # return [i + 1 for i, val in enumerate(arr) if val == i + 1]
        # solution 2
        result = []
        for i in range(len(arr)):
            if arr[i] == i + 1:  # 1-based indexing comparison
                result.append(i + 1)
        return result

arr= [15, 2, 45, 4 , 7]

sol = Solution()

# Time the function call
execution_time = timeit.timeit(lambda: sol.valueEqualToIndex(arr), number=1)
print(f"Execution time over 1 runs: {execution_time:.6f} seconds")