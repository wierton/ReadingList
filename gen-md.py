#coding: utf-8

import sys
import os

class Paper:
    title=''
    pub=''
    domain=''
    labels=[]
    cites=0
    score=0

    def __init__(self):
        pass

def parse_dbfile(fname):
    papers=[]
    with open(fname) as fp:
        paper=Paper()
        for line in fp.readlines():
            if line[0] == '\n':
                paper=Paper()
                continue
            attr, value = line.split(':', 1)
            value = value.strip()
            if attr == 'title':
                paper.title = value
            elif attr == 'publication':
                paper.pub = value
            elif attr == 'domain':
                paper.domain = value
            elif attr == 'labels':
                paper.labels = [i.strip() for i in value.split(',')]
            elif attr == cites:
                paper.cites = int(value)
            elif attr == score:
                paper.cites = int(value)

def generate_
