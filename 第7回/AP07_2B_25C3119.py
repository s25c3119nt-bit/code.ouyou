TREE = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F", "G"],
    "D": ["H", "J"],
    "E": ["K"],
    "F": ["L", "M"],
    "G": ["N"],
    "H": ["O"],
    "J": ["P", "Q"],
    "K": ["R", "S"],
    "L": [],
    "M": ["T", "U"],
    "N": ["V"],
    "O": [],
    "P": [],
    "Q": [],
    "R": [],
    "S": [],
    "T": [],
    "U": [],
    "V": []
}

def breadth_first_search(start, target):
    queue = [start]

    while queue:
        node = queue.pop(0)
        print("->" + node, end="")

        if node == target:
            print("\n{}を発見したため、探索を終了します".format(target))
            return

        for child in TREE[node]:
            queue.append(child)

    print("\n{}は見つかりませんでした".format(target))


if __name__ == "__main__":
    target = input("探索対象のノードを入力してください：").upper()
    if target not in TREE:
        print("存在するノードを入力してください")
    else:
        print("幅優先探索：", end="")
        breadth_first_search("A", target)
