#!/usr/bin/env python3
#coding: utf-8

import sys
import urllib.parse
import urllib.request
import time
import sys
import re
import os

class Paper:
    title=''
    pub=''
    domain=''
    year=''
    conference=''
    labels=[]
    cites=0
    score=0

    def __init__(self):
        pass

def google_scholar_query_url(query):
    google_scholar_query_prefix = 'https://scholar.google.com/scholar?q='
    words = re.split('\s+', query.strip())
    return google_scholar_query_prefix + \
            '+'.join([urllib.parse.quote(w) for w in words])

def parse_dbfile(fname):
    papers=[]
    with open(fname) as fp:
        paper=Paper()
        for line in fp.readlines():
            if line[0] == '\n':
                papers.append(paper)
                paper=Paper()
                continue
            attr, value = line.split(':', 1)
            value = value.strip()
            if attr == 'title':
                paper.title = value
            elif attr == 'publication':
                paper.pub = value
                paper.conference = value.split("'")[0]
                paper.year = value.split("'")[1]
            elif attr == 'domain':
                paper.domain = value
            elif attr == 'labels':
                paper.labels = [i.strip() for i in value.split(',')]
            elif attr == 'cites':
                paper.cites = int(value)
            elif attr == 'score':
                paper.score = int(value)
    return papers

def generate_readinglist_md(papers):
    fp = open('ReadingList.md', 'w+')
    fp.write('# total list\n')
    fp.write('\n')
    fp.write('|pub|labels|cites|score|title|\n')
    fp.write('|---|------|-----|-----|-----|\n')
    for paper in papers:
        pub = paper.pub
        labels = []
        for label in paper.labels:
            labels.append('[{0}](docs/labels/{0}.md)'.format(
                label))
        labels = ', '.join(labels)
        cites = paper.cites
        score = paper.score
        title = '[{}]({})'.format(paper.title, google_scholar_query_url(paper.title))
        fp.write('|{}|{}|{}|{}|{}|\n'.format(
            pub, labels, cites, score, title))
    fp.close()

def generate_md_by_labels(papers):
    label2paper = {}
    for paper in papers:
        for label in paper.labels:
            label2paper.setdefault(label, [])
            label2paper[label].append(paper)
    os.system('mkdir -p docs/labels')
    for label in label2paper.keys():
        fp = open('docs/labels/{}.md'.format(label), 'w+')
        fp.write('# {}\n'.format(label))
        fp.write('\n')
        for paper in label2paper[label]:
            fp.write('* {} [{}]({})\n'.format(
                paper.pub, paper.title,
                google_scholar_query_url(paper.title)))
        fp.close()

if __name__ == '__main__':
    db_fname = 'papers.db'
    if not os.access(db_fname, os.F_OK):
        print('db file {} cannot be found'.format(db_fname))
        os.exit(0)
    papers = parse_dbfile(db_fname)
    generate_readinglist_md(papers)
    generate_md_by_labels(papers)