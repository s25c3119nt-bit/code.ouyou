def bf_search(buff, pattern):
    n = len(buff)
    m = len(pattern)
    count = 0
    i = 0
    while i <= n - m:
        j = 0
        while j < m:
            if buff[i + j] != pattern[j]:
                break
            j += 1
        if j == m:
            count += 1
            print(f"{i + 1}文字目で『{pattern}』を見つけました")
        i += 1
    return count


if __name__ == "__main__":
    with open('/Users/yokoyamatoshiki/Downloads/AP10当日配布用コード/AP10_String.txt', "r", encoding="utf-8") as f:
        buff = f.read()

    while True:
        pattern = input("検索する文字列（終了：QUIT）：")
        if pattern == "QUIT":
            break
        if pattern == "":
            print("空文字列は検索できません")
            continue
        count = bf_search(buff, pattern)
        print(f"『{pattern}』は{count}個あります")