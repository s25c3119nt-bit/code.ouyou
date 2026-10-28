def oddsum(x):
    if x == 0:
        return 0
    return (2 * x - 1) + oddsum(x - 1)

def evsum(y):
    if y == 0:
        return 0
    return (2 * y) + evsum(y - 1)

def expo(x, y):
    if y == 0:
        return 1
    return x * expo(x, y - 1)

def input_data():
    while True:
        ix, iy = ((int)(i) for i in input().split())

        if ix == 99 and iy == 99:
            break

        print(f"{ix}個目までの奇数の和は{oddsum(ix)}")
        print(f"{iy}個目までの偶数の和は{evsum(iy)}")
        print(f"{ix}の{iy}乗は{expo(ix, iy)}")
        print("*" * 43)

if __name__ == "__main__":
    input_data()