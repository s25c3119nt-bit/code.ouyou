def quickSort(num):
    if len(num) < 2:
        return num

    pivot = num[0]
    left, right = divide(pivot, num[1:])
    return quickSort(left) + [pivot] + quickSort(right)


def divide(pivot, dnum):
    if len(dnum) < 1:
        return ([], [])

    left, right = divide(pivot, dnum[1:])
    tmp = dnum[0]

    if tmp > pivot:
        return ([tmp] + left, right)
    else:
        return (left, [tmp] + right)


def input_data():
    while True:
        array = [int(i) for i in input(
            "リストを入力してください（カンマ区切り、-99999で終了）："
        ).split(",")]
        if array[0] == -99999:
            break
        sort = quickSort(array.copy())
        print(sort)


if __name__ == "__main__":
    input_data()