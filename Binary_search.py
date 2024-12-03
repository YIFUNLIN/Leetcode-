import random

def binary_search(data,goal):   
    low = 0
    high = 49
    while low <= high and goal != -1:
        mid = int((low + high) // 2)
        if goal < mid:
            high = mid - 1
        elif goal > mid:
            low = mid + 1
        else:
            return mid
    return -1  # 若沒找到，則回傳 -1


val = 1
data = [0]  * 50
for i in range(50):
    data[i] = val
    val += random.randint(1,5)

while True:
    num = 0
    goal = int(input("輸入想搜尋的值(1-150),輸入-1結束:"))
    if goal == -1:
        break
    num = binary_search(data, goal)
    if num == -1:
        print('找不到[%3d]'%goal)
    else:
        print('在 %2d 位置找到 [%3d]'%(num+1,data[num]))

print('資料內容')
for i in range(5):
    for j in range(10):
        print('%3d-%-3d'%(i*10+j+1,data[i*10+j]),end='')
    print()


