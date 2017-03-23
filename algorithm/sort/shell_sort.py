#!/usr/bin/env python
# encoding=utf-8


def simple_shell_sort(lists):
    # 希尔排序
    count = len(lists)
    step = 2
    group = count // step
    while group > 0:
        for i in range(0, group):
            j = i+group
            while j < count:
                k = j - group
                key = lists[j]
                while k >= 0:
                    if lists[k] > key:
                        lists[k + group]=lists[k]
                        lists[k] = key
                    k -= group
                j += group
        group //= step
    return lists


lists = [22, 786, 2.23, 33, 70.2, 199, 101, 77, 56.4]
sortlst = simple_shell_sort(lists)
print(sortlst)
