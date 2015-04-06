#!/usr/bin/env python
# -*- coding: utf-8 -*-

import codecs
import json
import sys

tbl = dict()

def add_from(h):
    for line in h:
        line = line.strip()
        # drop 兒化音
        if line.endswith(u'（兒）'):
            line = line[:-3]
        if len(line) <= 1:
            continue
        key = line[0]
        val = line[1:]
        if key not in tbl:
            tbl[key] = list()
        tbl[key].append(val)

if len(sys.argv) < 2:
    print 'usage:', sys.argv[0], 'FILE1', '[FILE2]', '...'

for i in range(1, len(sys.argv)):
    h = codecs.open(sys.argv[i], 'r', encoding='utf8')
    add_from(h)
    h.close()

h = codecs.open('tbl.json', 'w', encoding='utf8')
json.dump(tbl, h, ensure_ascii=False, sort_keys=True)
h.close()
