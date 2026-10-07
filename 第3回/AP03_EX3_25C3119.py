def input_data():
    global phonebook

    while True:
        n, p = input().split()

        phonebook.update({n: p})

        if n == "end":
            break


def print_data():
    print(phonebook)
    for k, v in phonebook.items():
        if k == "end":
            break
        print("名前：", k, "\t電話番号：", v)


def search_data():
    while True:
        key = input()

        if key == "end":
            break

        if key in phonebook:
            print("名前：", key, "\t電話番号：", phonebook[key])
        else:
            print("名前が見つかりません")

    print("検索終了")


if __name__ == "__main__":
    phonebook = {}

    input_data()
    print_data()
    print("********検索処理にはいる********")
    search_data()
