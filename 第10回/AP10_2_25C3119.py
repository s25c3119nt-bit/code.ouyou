def bf_search(buff, pattern):
    n = len(buff) - 1  # 探索対象の最終インデックス
    m = len(pattern)  # 探索パターンの文字数
    i = 0  # 探索位置
    count = 0  # 見つかった単語の数

    while i <= n - m + 1:
        j = 0
        while j < m:
            if buff[i + j].lower() != pattern[j].lower():
                break
            j += 1

        if j == m:
            # 単語の前後が英字なら、部分一致なので数えない
            before = i > 0 and buff[i - 1].isalpha()
            after = i + m < len(buff) and buff[i + m].isalpha()
            if not before and not after:
                print(f"{i + 1}文字目で『{pattern}』をみつけました")
                count += 1
        i += 1

    return count


if __name__ == "__main__":
    f = open("/Users/yokoyamatoshiki/Downloads/English.txt", "r", encoding="UTF-8")
    buff = f.read()
    f.close()
    
    while True:
        pattern = input("検索する英単語（終了：QUIT）：").strip()
        if pattern == "QUIT":
            break
        if pattern == "":
            print("英単語を入力してください")
            continue
        count = bf_search(buff, pattern)
        print(f"『{pattern}』は{count}個あります")