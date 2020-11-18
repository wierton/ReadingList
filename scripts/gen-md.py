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


class Renderer:
    def __init__(self):
        pass
    def google_scholar_query_url(self, query):
        google_scholar_query_prefix = 'https://scholar.google.com/scholar?q='
        words = re.split('\s+', query.strip())
        return google_scholar_query_prefix + \
                '+'.join([urllib.parse.quote(w) for w in words])

    def render_title(self, title):
        return '[{}]({})'.format(title, self.google_scholar_query_url(title))
    def quote_label(self, label):
        return re.sub('\s+', '-', label)
    def render_label(self, label):
        return '[{0}](labels/{0}.md)'.format(self.quote_label(label))
    def render_conference(self, conf_year):
        urlpfx = 'https://dblp.org/db/conf/'
        configs = {
          "ICSE": [ urlpfx + 'icse/icse%y.html', [ 2015, 2010 ] ],
          "FSE": [ urlpfx + 'sigsoft/fse%y.html', [ ] ]
        }

        conf, year = conf_year.split("'")
        if int(year) < 50: year = '20' + year
        else: year = '19' + year

        info = configs[conf]
        if int(year) in info[1]:
            volume_1 = info[0].replace('%y', year + '-1')
            volume_2 = info[0].replace('%y', year + '-2')
            return '{}([1]({}), [2]({}))'.format(
                conf_year, volume_1, volume_2)
        else:
            url = info[0].replace('%y', year)
            return '[{}]({})'.format(conf_year, url)

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
    return sorted(papers, key=lambda p: p.cites, reverse=True)

def generate_readinglist_md(papers):
    os.system('mkdir -p docs')
    fp = open('docs/ReadingList.md', 'w+')
    fp.write('# total list\n')
    fp.write('\n')
    fp.write('|pub|labels|cites|score|title|\n')
    fp.write('|---|------|-----|-----|-----|\n')
    renderer = Renderer()
    for paper in papers:
        pub = renderer.render_conference(paper.pub)
        labels = []
        for label in paper.labels:
            labels.append(renderer.render_label(label))
        labels = ', '.join(labels)
        cites = paper.cites
        score = paper.score
        title = renderer.render_title(paper.title)
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
    renderer = Renderer()
    for label in label2paper.keys():
        fp = open('docs/labels/{}.md'.format(
            renderer.quote_label(label)), 'w+')
        fp.write('# {}\n'.format(label))
        fp.write('\n')
        for paper in label2paper[label]:
            fp.write('* {} {}\n'.format(
                paper.pub, renderer.render_title(paper.title)))
        fp.close()

if __name__ == '__main__':
    db_fname = 'papers.db'
    if not os.access(db_fname, os.F_OK):
        print('db file {} cannot be found'.format(db_fname))
        os.exit(0)
    papers = parse_dbfile(db_fname)
    generate_readinglist_md(papers)
    generate_md_by_labels(papers)
