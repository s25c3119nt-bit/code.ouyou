import random

def bubble_sort_descending(array):
    for i in range(len(array) - 1):
        for j in range(len(array) - 1 - i):
            if array[j] < array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

def binary_search(data, item):
    left = 0
    right = len(data) - 1

    while left <= right:
        mid = (left + right) // 2
        print(f"中間値：{data[mid]}，探索値：{item}")

        if data[mid] == item:
            print(f"{mid + 1}番目に{item}を見つけました!")
            return mid
        elif data[mid] > item:
            print(f"{data[mid]} > {item} なので右側を探索します")
            left = mid + 1
        elif data[mid] < item:
            print(f"{data[mid]} < {item} なので左側を探索します")
            right = mid - 1

    print(f"{item}は見つかりませんでした")
    return -1


def insert_descending(data, item):
    index = 0

    while index < len(data) and data[index] >= item:
        index += 1

    data.insert(index, item)
    print(f"{item}を{index + 1}番目に挿入しました")
    print("挿入後のリスト")
    print(data)


if __name__ == "__main__":
    array = [random.randint(10, 90) for i in range(50)]
    bubble_sort_descending(array)

    print("降順にソートしたリスト")
    print(array)

    while True:
        item = int(input("探索したい整数値（終了は9999）："))

        if item == 9999:
            print("終了します")
            break

        result = binary_search(array, item)

        if result == -1:
            insert_descending(array, item)
