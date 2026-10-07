def input_data():
    global name, phone

    while True:
        n, p = input().split()

        name.append(n)
        phone.append(p)

        if n == "end":
            break


def print_data():
    print(name)
    print(phone)
    for (n, p) in zip(name, phone):
        if n == "end":
            break
        print("名前：", n, "\t電話番号：", p)


def search_data():
    while True:
        key = input()

        if key == "end":
            break

        for na in name:
            if na == key:
                i = name.index(na)
                print("名前：", na, "\t電話番号：", phone[i])
                break
            elif na == "end":
                print("名前が見つかりません")
                break

    print("検索終了")


if __name__ == "__main__":
    name = []
    phone = []

    input_data()
    print_data()
    print("********検索処理にはいる********")
    search_data()