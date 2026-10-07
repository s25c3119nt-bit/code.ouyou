import numpy as np

def test_arrey():
    a = np.array([10,20,30])
    print(a)
    print('*********************')

    a = np.insert(a, 2, 25)
    print(a)
    print('*********************')

    a = np.append(a, 100)
    print(a)
    print('*********************')

    for i in range(a.size):
        print('a[{}] = {}' .format(i, a[i]))
if __name__ == "__main__":
    test_arrey()