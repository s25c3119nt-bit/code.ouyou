def test_list():
    a = [10,20,30]
    print(a)
    print('**********************')

    a.insert(2, 25)
    print(a)
    print('**********************')

    a.insert(2, '99')
    print(a)
    print('**********************')

    a.append(100)
    print(a)
    print(a.index(100))

if __name__ == "__main__":
    test_list()