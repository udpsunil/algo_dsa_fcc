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
    

    def merge_sort(self, arr: list[int], left: int, right: int):
        if left < right:
            mid = (left + right) // 2
            self.merge_sort(arr, left, mid)
            self.merge_sort(arr, mid+1, right)
            merge(arr, left, mid, right)

    def print_pairs(self, arr: list[int]):
        for element in arr:
            for another in arr:
                print(element, ", ", another)


def merge(arr:list[int], left: int, mid: int, right:int):
    n1 = mid - left + 1
    n2 = right - mid
    L = [0] * n1
    R = [0] * n2

    for i in range(n1):
        L[i] = arr[left + i]
    for j in range(n2):
        R[j] = arr[mid + 1 + j]

    i = j = 0
    k = left
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

