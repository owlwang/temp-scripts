#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/10 下午5:05
# @Author  : owlwang
# @Site    : 
# @File    : findsuffixfile.py
# @Software: PyCharm

from __future__ import print_function
import os
import sys


def main(path, suffix):
    with open('output.txt', 'a') as f:
        for dirpath, dirnames, filenames in os.walk(path):
            for filename in filenames:
                names = os.path.join(dirpath, filename)
                if names.endswith('.' + suffix):
                    f.write(names + '\n')


if __name__ == '__main__':
    if len(sys.argv) <= 2:
        print('[-] Usage: script.py targetpath suffix')
        sys.exit()
    else:
        path = sys.argv[1]
        suffix = sys.argv[2]
        main(path, suffix)
