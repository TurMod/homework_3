from datetime import datetime
from multiprocessing import Process, Queue


def factorize(*numbers):
    queue = Queue()
    processes = []
    for number in numbers:
        pr = Process(target=factorize_number, args=(number, queue))
        pr.start()
        processes.append(pr)

    [el.join() for el in processes]

    results = []
    while not queue.empty():
        result = queue.get()
        results.append(result)

    return results


def factorize_number(number, q):
    result = []
    divisor = 1

    while divisor <= number:
        if number % divisor == 0:
            result.append(divisor)
        divisor += 1
    q.put(result)


if __name__ == '__main__':
    start = datetime.now()
    a, b, c, d = factorize(128, 255, 99999, 10651060)

    assert a == [1, 2, 4, 8, 16, 32, 64, 128]
    assert b == [1, 3, 5, 15, 17, 51, 85, 255]
    assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
    assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106, 1521580, 2130212, 2662765, 5325530, 10651060]
    finish = datetime.now()

    print(f'Time -> {finish - start}')
