
def bubble_sort(array):
    compare_count = 0
    swap_count = 0

    for i in range(0, len(array) - 1):
        for j in range(0, len(array) - 1 - i):
            compare_count += 1
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                swap_count += 1
            print(array)

    print("バブルソートの計算時間は{}回（比較処理{}回，交換処理{}回）".format(
        compare_count + swap_count, compare_count, swap_count))
    print(array)


def selection_sort(array):
    compare_count = 0
    swap_count = 0

    for i in range(0, len(array) - 1):
        min_index = i
        for j in range(i + 1, len(array)):
            compare_count += 1
            if array[j] < array[min_index]:
                min_index = j

        if min_index != i:
            array[i], array[min_index] = array[min_index], array[i]
            swap_count += 1

    print("選択ソートの計算時間は{}回（比較処理{}回，交換処理{}回）".format(
        compare_count + swap_count, compare_count, swap_count))
    print(array)


def insertion_sort(array):
    compare_count = 0
    shift_count = 0
    insert_count = 0

    for i in range(1, len(array)):
        key = array[i]
        j = i - 1

        while j >= 0:
            compare_count += 1
            if array[j] > key:
                array[j + 1] = array[j]
                shift_count += 1
                j -= 1
            else:
                break

        array[j + 1] = key
        insert_count += 1

    total = compare_count + shift_count + insert_count
    print("挿入ソートの計算時間は{}回（比較処理{}回，シフト処理{}回），挿入処理{}回）".format(
        total, compare_count, shift_count, insert_count))
    print(array)


if __name__ == "__main__":
    while True:
        num = [int(i) for i in input(
            '並び替える数値をカンマ区切りで入力してください：'
        ).split(',')]

        if num[0] == -999:
            break

        print("入力配列")
        print(num)

        bubble_sort(num.copy())
        print("*" * 39)
        selection_sort(num.copy())
        print("*" * 39)
        insertion_sort(num.copy())

