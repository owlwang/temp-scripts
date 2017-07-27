#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author = owlwang

from __future__ import print_function
import requests
from bs4 import BeautifulSoup


def get_page_content():
    r = requests.get('https://free-proxy-list.net/')
    if r.status_code != 200 or r.content != '':
        return r.text
    return None


def main():
    html = get_page_content()
    soup = BeautifulSoup(html, 'lxml')
    table = soup.find('table', id='proxylisttable')
    rows = table.find_all('tr')[1:-1]  # remove first and last row
    s = ('ip', 'port', 'code', 'contry', 'anonymity', 'google', 'https', 'lastchecked')
    for tr in rows:
        td = tr.find_all('td')
        yield {key: td[i].string for i, key in enumerate(s)}


if __name__ == '__main__':
    print(list(main()))
