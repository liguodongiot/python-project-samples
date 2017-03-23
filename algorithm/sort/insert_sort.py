#!/usr/bin/env python
# encoding=utf-8


def simpel_insert_sort(lists):
    # 插入排序
    count = len(lists)
    for i in range(1, count):
        key = lists[i]
        j = i - 1
        while j >= 0:
            if lists[j] > key:
                lists[j + 1] = lists[j]
                lists[j] = key
            j -= 1
    return lists


lists = [22, 786, 2.23, 33, 70.2]
sortlst = simpel_insert_sort(lists)
print(sortlst)
