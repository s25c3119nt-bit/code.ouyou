import numpy as np


def input_data():
    #グローバル変数は関数内で値の変更をする場合はglobal宣言をしないといけない
    global name, phone
    for i in range(len(name)):
        n, p = input().split()
        #名前にendが入力されたら入力処理は終了
        name[i] = n
        phone[i] = p
        if n == "end":
            break


def print_data():
    print(name)
    print(phone)
    for i in range(len(name)):
        if name[i] == "end":
            break
        print("名前：", name[i], "\t電話番号：", phone[i])


def search_data():
    #検索用の繰り返し処理
    while True:
        key = input()
        #keyに代入された値がendなら検索処理そのものを終了
        if key == "end":
            break

        for i in range(len(name)):
            #名前の配列の要素にkeyの値と同じものがあったら
            if name[i] == key:
                #名前と同じインデックスの電話番号の要素を出力
                print("名前：", name[i], "\t電話番号：", phone[i])
                break
            #名前の配列の要素がendになったら（電話帳としてのデータの最後ということ）
            elif name[i] == "end":
                #keyの値が見つからなかったということになるので、その旨を通知して終了
                print("名前が見つかりません")
                break

    print("検索終了")


if __name__ == "__main__":
    name = np.empty(10, dtype=object)
    phone = np.empty(10, dtype=object)
    input_data()
    print_data()
    print("********検索処理にはいる********")
    search_data()