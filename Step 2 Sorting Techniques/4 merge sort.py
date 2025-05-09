''' 

Merge Sort Algorithm 11/4/25

https://takeuforward.org/data-structure/merge-sort-algorithm/

Dry run in notes

TC O(NLogn), SC O(N)

'''

arr = [13,46,24,52,20,9]
n = len(arr)

def merge(arr, low, mid, high):
    temp = []
    left = low
    right = mid+1

    while left <= mid and right <= high:
        if arr[left] <= arr[right]:
            temp.append(arr[left])
            left += 1
        else:
            temp.append(arr[right])
            right += 1
    while left <= mid:
        temp.append(arr[left])
        left += 1
    while right <= high:
        temp.append(arr[right])
        right += 1
    for i in range(low, high+1):
        arr[i] = temp[i-low]


def merge_sort(arr, low, high):
    if low == high:
        return
    mid = (low + high) // 2
    
    merge_sort(arr, low, mid)
    merge_sort(arr, mid+1, high)
    merge(arr, low, mid, high)

merge_sort(arr, 0, n-1)
print(arr)
