"""Implement a merge sort algorithm implementation."""


def merge_sort(lis):
    merge_sort2(lis, 0, len(lis) - 1)


def merge_sort2(lis, first, last):
    if first < last:
        middle = (first + last) // 2
        merge_sort2(lis, first, middle)
        merge_sort2(lis, middle + 1, last)
        merge(lis, first, middle, last)


def merge(lis, first, middle, last):
    left_lis = lis[first: middle + 1] + [9999999]
    right_lis = lis[middle + 1: last + 1] + [9999999]  # include last
    i = j = 0

    for k in range(first, last + 1):
        if left_lis[i] <= right_lis[j]:
            lis[k] = left_lis[i]
            i += 1
        else:
            lis[k] = right_lis[j]
            j += 1


if __name__ == "__main__":
    items = [9, 8, 6, -8, -3]
    print(items)
    merge_sort(items)
    print(items)