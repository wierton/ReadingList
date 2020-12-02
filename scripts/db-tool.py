#!/usr/bin/env python3
#coding: utf-8

import sys
import urllib.parse
import urllib.request
import time
import sys
import re
import os

def parse_dbfile(fname):
    entries=[]
    with open(fname) as fp:
        entry=[]
        for line in fp.readlines():
            if line[0] == '\n':
                entries.append(entry)
                entry=[]
                continue
            attr, value = line.split(':', 1)
            entry.append([attr, value[:-1]])
    return entries

def print_entries(entries):
    for e in entries:
        for k, v in e:
            print("{}:{}".format(k, v), end='\n')
        print('', end='\n')

def manipulate(entries):
    def pairsGetValue(e, key):
        for k, v in e:
            if k == key:
                return v
        return ''
    def pairsRenameKey(e, oldKey, newKey):
        for i in range(len(e)):
            if e[i][0] == oldKey:
                e[i][0] = newKey
    for e in entries:
        pairsRenameKey(e, "score", "tags")
    for e in entries:
        e.append(("state", " assigning labels"))
    entries = sorted(entries, key=lambda e: pairsGetValue(e, "domain"))
    return entries

if __name__ == '__main__':
    db_fname = 'papers.db'
    if not os.access(db_fname, os.F_OK):
        print('db file {} cannot be found'.format(db_fname))
        os.exit(0)

    entries = parse_dbfile(db_fname)
    entries = manipulate(entries)
    print_entries(entries)
