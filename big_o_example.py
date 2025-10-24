class BigOExamples:
    # O(1)
    def get_first_element(self, arr):
        return arr[0]

    # O(logn)
    def binary_search(self, arr: list[int], target: int) -> int:
        left = 0
        right = len(arr) - 1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1

    # O(n)
    def linear_search(self, arr: list[int], target: int) -> int:
        for i, element in enumerate(arr):
            if element == target:
                return i
        return -1