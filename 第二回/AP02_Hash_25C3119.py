def AP02_EX_Hash():
    mydict = {}
    # 教授名と研究室名のハッシュテーブル
    mydict.update({"安藤昌也": "エクスペリエンスデザイン研究室"})
    mydict.update({"飯田一博": "空間音響研究室"})
    mydict.update({"小早川真衣子": "情報と社会のデザイン研究室"})
    mydict.update({"今野将": "応用知能システム研究室"})
    mydict.update({"竹本浩典": "音声生成研究室"})
    mydict.update({"田邉里奈": "コミュニケーションデザイン研究室"})
    mydict.update({"苣木禎史": "マルチモーダル研究室"})
    mydict.update({"中本和宏": "インタラクションデザイン研究室"})
    mydict.update({"細田真道": "行動認識・フィードバック研究室"})
    mydict.update({"宮田高道": "多次元情報処理研究室"})
    mydict.update({"森信一郎": "知的情報工学研究室"})

    print(mydict)

    key = input("検索する教授名：")

    if key in mydict:
        print(mydict.get(key))
    else:
        print("該当する教授が見つかりません")


if __name__ == "__main__":
    AP02_EX_Hash()
