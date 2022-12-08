import timeit

prime_numbers_squares = [2,3,5,7,11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
fibonacci_numbers_squares = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025]


def pythonic_way(list_1, list_2):
    return tuple(map(sum,list(zip(list_1,list_2))))


def readable_way(list_1, list_2):
    result_list = []
    for element in range(len(list_1)):
        result_list.append(list_1[element] + list_2[element])
    return result_list 


print(f"Pythonic way took: {timeit.timeit(lambda: pythonic_way(prime_numbers_squares,fibonacci_numbers_squares),number=1)}s")
print(f"Readable way took: {timeit.timeit(lambda: readable_way(prime_numbers_squares,fibonacci_numbers_squares), number=1)}s")