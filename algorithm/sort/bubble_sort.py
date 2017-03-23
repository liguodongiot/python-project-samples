#!/usr/bin/env python
# encoding=utf-8


def simple_bubble_sort(lists):
    # 冒泡排序
    count = len(lists)
    for i in range(0, count):
        for j in range(i + 1, count):
            if lists[i] > lists[j]:
                lists[i], lists[j] = lists[j], lists[i]
    return lists

lists = [22, 786, 2.23, 33, 70.2, 199, 101, 77, 56.4]
sortlst = simple_bubble_sort(lists)
print(sortlst)
