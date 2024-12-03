# 法一
import random

# 初始化陣列
def inputarr(data, size):
    for i in range(size):
        data[i] = random.randint(1, 100)

# 顯示陣列
def showdata(data, size):
    for i in range(size):
        print('%3d' % data[i], end=' ')
    print()

# 快速排序
def quick(d, size, left, right):
    if left < right:
        key = left  # 基準值索引

        # 左指標
        l_idx = left + 1
        while l_idx < size and d[l_idx] < d[key]: # 防止指標超出陣列範圍 & 要若小於key值
            l_idx += 1  # 若沒有比key大，也沒有超出array範圍，繼續往右移動

        # 右指標
        r_idx = right
        while r_idx > left and d[r_idx] > d[key]:
            r_idx -= 1  # 若沒有比key小，繼續往左移動

        # 指標未交錯時，交換數值
        while l_idx < r_idx:
            d[l_idx], d[r_idx] = d[r_idx], d[l_idx]   # 交換左右兩邊的值(前面的while已跑完，若尚未交錯，代表有找到符合 > or < key規則的值，就進行交換)
            l_idx += 1 # 交換完後，左邊指標往右移動
            while l_idx < size and d[l_idx] < d[key]:
                l_idx += 1
            r_idx -= 1
            while r_idx > left and d[r_idx] > d[key]:
                r_idx -= 1

        # 將基準值放到正確位置
        d[key], d[r_idx] = d[r_idx], d[key]

        # 顯示排序過程
        showdata(d, size)

        # 遞迴排序左側和右側子陣列
        quick(d, size, left, r_idx - 1)
        quick(d, size, r_idx + 1, right)

# 主程式
def main():
    data = [0] * 100
    size = int(input('請輸入陣列大小: '))
    inputarr(data, size)
    print('原始資料為:')
    showdata(data, size)
    print('排序過程:')
    quick(data, size, 0, size - 1)
    print('排序結果:')
    showdata(data, size)

main()
