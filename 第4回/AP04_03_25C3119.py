def mergeSort(num):
    if len(num) < 2:
        return num

    c = round(len(num) / 2)
    return merge(mergeSort(num[:c]), mergeSort(num[c:]))


def merge(low, high):
    if len(low) < 1:
        return high
    if len(high) < 1:
        return low

    if low[0] > high[0]:
        return [low[0]] + merge(low[1:], high)
    else:
        return [high[0]] + merge(low, high[1:])


def input_data():
    while True:
        array = [int(i) for i in input(
            "リストを入力してください（カンマ区切り、-99999で終了）："
        ).split(",")]
        if array[0] == -99999:
            break
        sort = mergeSort(array.copy())
        print(sort)


if __name__ == "__main__":
    input_data()