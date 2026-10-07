from collections import deque

def test_queue():
    fifo = deque([1, 2, 3, 4, 5])
    print(fifo)

    fifo.append(6)
    print(fifo)

    b = fifo.popleft()
    print(b)
    print(fifo)

if __name__ == "__main__":
    test_queue()