def bubble_sort(num):
    for i in range(0, len(num)-1):
        for j in range(len(num)-1, i, -1):
            if num[j-1] > num[j]:

                num[j-1],num[j] = num[j],num[j-1]
                print(num)
    print(num)

if __name__ == "__main__":
    array = [5, 8, 1, 3, 7, 6, 2, 4, 9, 0]
    bubble_sort(array.copy())