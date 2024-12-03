def partition(arr, low, high):
    pivot = arr[low]  # 選擇第一個元素作為基準值
    left = low + 1
    right = high

    while True:
        while left <= right and arr[left] < pivot:  # 找到大於等於 pivot 的左側值
            left += 1
        while left <= right and arr[right] > pivot:  # 找到小於等於 pivot 的右側值
            right -= 1

        if left > right:  # 當左右指標交錯時
            arr[low], arr[right] = arr[right], arr[low]  # 將基準值移到正確位置
            return right  # 返回基準值位置
        else:  # 未交錯時，交換左右值
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

def QuickSort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)
        QuickSort(arr, low, pivot_index - 1)
        QuickSort(arr, pivot_index + 1, high)

# 測試數據
arr = [47, 47, 96, 17, 12, 55, 99, 47, 92, 22]
QuickSort(arr, 0, len(arr) - 1)
print("排序結果:", arr)
