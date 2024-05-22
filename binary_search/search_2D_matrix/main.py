from typing import List
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binarySearch(arr: List[int]) -> bool:
            l = 0
            r = len(arr) -1
            while l <= r:
                mid = (l + r) // 2
                if arr[mid] == target:
                    return True
                elif arr[mid] < target:
                    l = mid + 1
                else: 
                    r = mid - 1
            return False
            
        n = len(matrix[0]) - 1 # highest value of the left arr
        m = len(matrix) - 1 # lowest value of the right arr
        
        l_arr_counter = 0
        l = matrix[l_arr_counter][n]
        r_arr_counter = m
        r = matrix[r_arr_counter][0]
        print(l, r)
        if l_arr_counter == r_arr_counter:
            return binarySearch(matrix[0])
        while l <= r:
            if target <= l:
                print(matrix[l_arr_counter])
                return binarySearch(matrix[l_arr_counter])
            elif l < target < r:
                # incrase l arr count by 1
                # decrease r arr coutn by 1
                l_arr_counter += 1
                r_arr_counter -= 1
                if l_arr_counter == r_arr_counter:
                    print(l_arr_counter, r_arr_counter)
                    print(matrix[l_arr_counter])
                    return binarySearch(matrix[l_arr_counter])
                l = matrix[l_arr_counter][n]
                r = matrix[r_arr_counter][0]
                print(l, r)
            else: 
                print(matrix[r_arr_counter])
                return binarySearch(matrix[r_arr_counter]) 

x = Solution()
print(
    x.searchMatrix(
    [[1,3,5], [10,11,16], [23, 30, 60]], -1)
    )
print(
    x.searchMatrix(
    [[1,3,5], [10,11,16], [23, 30, 60]], 3)
    )
print(
    x.searchMatrix([[1]], 1)
)
print(
    x.searchMatrix([[1,3]], 1)
)
print(
    x.searchMatrix([[1], [3]], 1)
)