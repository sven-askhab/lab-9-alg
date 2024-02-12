

import timeit
import bisect
import random


def binary_search(arr, target):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


def generate_sorted_array(size):
    return list(range(1, size + 1))


def measure_time(func, *args):
    return timeit.timeit(lambda: func(*args), number=1000)


def main():
    sizes = list(range(100, 1100, 100))
    
    print("Size\tWorst Case\tAverage Case\tPy Worst Case\tPy Average Case")
    
    for size in sizes:
        sorted_array = generate_sorted_array(size)
        r_elem = random.choice(sorted_array)

        wst_time = measure_time(binary_search, sorted_array, size + 1)
        avg_time = measure_time(binary_search, sorted_array, r_elem)
        py_wst_time = measure_time(bisect.bisect_left, sorted_array, size + 1)
        py_avg_time = measure_time(bisect.bisect_left, sorted_array, r_elem)
        
        print(f"{size}\t{wst_time:.6f}\t{avg_time:.6f}\t" \
              f"{py_wst_time:.6f}\t{py_avg_time:.6f}")


if __name__ == "__main__":
    main()