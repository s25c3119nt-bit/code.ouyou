import random

def bubble_sort(array):
    for i in range(len(array) - 1):
        for j in range(len(array) - 1 - i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]


def binary_search(data, item):
    left = 0
    right = len(data) - 1

    while left <= right:
        mid = (left + right) // 2

        if data[mid] < item:
            left = mid + 1
        else:
            right = mid - 1

    result = []
    for i in range(right + 1):
        result.append(data[i])
    return result

def linear_search(data, value):
    result = []
    for item in data:
        if item < value:
            result.append(item)
    return result

if __name__ == "__main__":
    array = random.sample(range(10,90), 20)
    print("配列A :")
    print(array)

    sorted_arrey = array.copy()
    bubble_sort(sorted_arrey)
    while True:
        try:
            value = int(input("整数値Nを入力してください："))
        except ValueError:
            print("整数を入力してください")
            continue
        if value < min(array) or value > max(array):
            print("入力値は配列の最小値以上、最大値以下にしてください")
            continue
        break

    print(f"入力値 : {value}")
    print(f"二分探索 : {binary_search(sorted_arrey, value)}") 
    print(f"線形探索 : {linear_search(array, value)}")

        

