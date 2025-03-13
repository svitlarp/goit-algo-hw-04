## Analyse of execution time od three algorythmes

- Insertation Sort;
- Merge Sort;
- Tim Sort which is default python sorting algorytme;

A Python module <a href="https://docs.python.org/3.13/library/timeit.html">'timeit'</a> is used to analyze execution time.

```bash
Tim Sort execution time for a small list (10 elements): 0.000067 seconds
Tim Sort execution time for a large list (10000 elements): 0.049145 seconds

Merge Sort execution time for a small list (10 elements): 0.000060 seconds
Merge Sort execution time for a large list (10000 elements): 0.072793 seconds

Insertion Sort execution time for a small list (10 elements): 0.000046 seconds
Insertion Sort execution time for a large list (10000 elements): 4.488904 seconds
```

By comparing the performance of the same algorithms on input arrays of different sizes, we can observe a significant difference in Insertion Sort's efficiency on small versus large arrays. This indicates that Insertion Sort's execution time increases considerably with larger datasets. However, Merge Sort performs much better than Insertion Sort on large arrays, though it still does not match the efficiency of Tim Sort.
In contrast, Tim Sort exhibits nearly consistent execution times regardless of whether it is applied to a small or large array.
