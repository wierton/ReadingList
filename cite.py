#!/usr/bin/python
#coding=utf-8

# import urllib
import urllib.parse
import urllib.request
import time
import sys
import re
from scholarly import scholarly

if __name__ == "__main__":
    wfname=sys.argv[1]+'.new'
    wfcontents=''.join(open(wfname, 'r').readlines())

    need_skip=True
    wfp=open(sys.argv[1]+'.new', 'a+')
    with open(sys.argv[1]) as fp:
        lines=fp.readlines()
        for line in lines:
            if line[0] != '*':
                if not need_skip: wfp.write(line)
                continue
            info=line.replace('* ', '')
            info=info.replace('\n', '')
            conference, title=info.split(' ', 1)
            if title in wfcontents:
                print('skip {}'.format(title))
                continue
            else:
                print('process {}'.format(title))

            need_skip=False
            search_query=scholarly.search_pubs(title)
            cites=next(search_query).fill().bib['cites']
            wfp.write('* {}:{} {}\n'.format(conference, cites, title))
            wfp.flush()
