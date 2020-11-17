import re
import sys

with open('ReadingList.md') as fp:
    tag=''
    for line in fp.readlines():
        if line[0] == '#':
            tag = line.replace('#', '').strip()
        elif line[0] == '*':
            info = line.replace('*', '').strip()
            pub_cites, title = info.split(' ', 1)
            pub, cites = pub_cites.split(':')
            print('title: {}'.format(title), end='\n')
            print('pub: {}'.format(pub), end='\n')
            print('target: {}'.format(tag), end='\n')
            print('labels: {}'.format(tag), end='\n')
            print('cites: {}'.format(cites), end='\n')
            print('score: {}'.format(0), end='\n')
            print('', end='\n')
