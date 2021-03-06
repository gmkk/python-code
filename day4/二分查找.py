#!/usr/bin/env python
# -*- conding-utf8 -*-

def binary_search(data_source, find_n):
    mid = int(len(data_source)/2)
    if mid >= 1:
        if data_source[mid] > find_n: # data in left
            print("data in left of [%s]" % data_source[mid])
            print(data_source[:mid])
            binary_search(data_source[:mid], find_n)
        elif data_source[mid] < find_n: # data in right
            print("data in right of [%s]" % data_source[mid])
            print(data_source[mid:])
            binary_search(data_source[mid:], find_n)
        elif data_source[mid] == find_n:
            print("found %s" % data_source[mid])
    elif data_source[mid] == find_n:
        print("found %s" % data_source[mid])
    else:
        print("not found")


if __name__ == '__main__':
    data = list(range(1,100,3))
    ret = input("请输入猜测的数字：")
    binary_search(data, int(ret))
