def sum(n):
    if n == 0:
        return 0
    return (n + sum(n - 1))

if __name__ == "__main__":
    n = int(input("自然数Nを入力:"))
    if n < 0:
        print("0以上の数値を入力")
    else:
        print("0から", n, "までの総和:", sum(n))