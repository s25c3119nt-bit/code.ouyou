def bubble_sort(num):
    for i in range(0, len(num)-1):
        for j in range(len(num)-1, i, -1):
            if num[j-1] > num[j]:

                num[j-1],num[j] = num[j],num[j-1]
                print(num)
    print(num)

def input_data():
    while True:
        array = [int(i) for i in input(
            "リストを入力（-99999で終了）："
        ).split(",")]

        if array[0] == -99999:
            break
        bubble_sort(array.copy())

if __name__ == "__main__":
    input_data()
