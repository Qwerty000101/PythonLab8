#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


if __name__ == '__main__':
    A = tuple(map(int, input("Введите 24 числа\n").split()))
    while len(A) != 24:
        print("Должно быть введено 24 числа", file=sys.stderr)
        exit(1)

    s = A.count(5)

    print(s)