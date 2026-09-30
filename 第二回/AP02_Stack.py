def test_stack():
    lifo = [1, 2, 3, 4, 5]
    print(lifo)

    lifo.append(6)
    print(lifo)

    a = lifo.pop()
    print(a)
    print(lifo)

    a = lifo.pop()
    print(a)
    print(lifo)

if __name__ == "__main__":
    test_stack()