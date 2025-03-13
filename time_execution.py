import random
import timeit
from merge_sort import merge_sort
from insertion_sort import insertion_sort
from tim_sort import tim_sort


# Measuring the execution time of a function for sorting a small array and big array 

# Tim Sort
small_array_execution_time = timeit.timeit("tim_sort(random.sample(range(1, 1000), 10))", 
                           globals=globals(), number=2)

big_array_execution_time = timeit.timeit("tim_sort(random.sample(range(1, 20000), 10000))", 
                          globals=globals(), number=2)

print(f"Tim Sort execution time for a small list (10 elements): {small_array_execution_time :.6f} seconds")
print(f"Tim Sort execution time for a large list (10000 elements): {big_array_execution_time:.6f} seconds")


# Merge Sort 
small_array_execution_time = timeit.timeit("merge_sort(random.sample(range(1, 1000), 10))", 
                           globals=globals(), number=2)

big_array_execution_time = timeit.timeit("merge_sort(random.sample(range(1, 20000), 10000))", 
                          globals=globals(), number=2)

print(f"Merge Sort execution time for a small list (10 elements): {small_array_execution_time :.6f} seconds")
print(f"Merge Sort execution time for a large list (10000 elements): {big_array_execution_time:.6f} seconds")


# Insertation Sort
small_array_execution_time = timeit.timeit("insertion_sort(random.sample(range(1, 1000), 10))", 
                           globals=globals(), number=2)

big_array_execution_time = timeit.timeit("insertion_sort(random.sample(range(1, 20000), 10000))", 
                          globals=globals(), number=2)

print(f"Insertion Sort execution time for a small list (10 elements): {small_array_execution_time :.6f} seconds")
print(f"Insertion Sort execution time for a large list (10000 elements): {big_array_execution_time:.6f} seconds")








