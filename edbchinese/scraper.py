#!/usr/bin/env python

from bs4 import BeautifulSoup
import codecs

# Main list: KS1 & KS2
# It contains Cantonese pronunciations
ks12 = set()
# There are six supplementary lists
# I:   Four-Character Expressions
# II:  Idiomatic Phrases
# III: Words Used in Classical Chinese
# IV:  Terms and Proper Noun
# V:   Transliterated Loan Words
# VI:  Characters Used in Names
slst = [set() for i in range(6)]

def handle(data):
    soup = BeautifulSoup(data, 'lxml')
    ci = soup.find(id='tblCi')
    if ci is not None:
        elems = ci.find_all('td', class_='ci')
        elems = filter(lambda e:e.find('table') is None, elems)
        words = map(lambda e:e.get_text().strip(), elems)
        ks12.update(words)
    for i in range(1, 7):
        fb = soup.find(id='fb0%d' % i)
        if fb is None:
            continue
        elems = fb.find_next('table').find_all('td', class_='ci')
        elems = filter(lambda e:e.find('table') is None, elems)
        words = map(lambda e:e.get_text().strip(), elems)
        words = filter(lambda e:len(e)>0, words)
        slst[i-1].update(words)

def savelst(fn, lst):
    h = codecs.open(fn, 'w', encoding='utf8')
    lst = list(lst)
    lst.sort()
    h.write('\n'.join(lst))
    h.close()

N = 4762
for i in range(1, N+1):
    _id = '%04d' % i
    h = codecs.open('data/%s.html' % _id, 'r', encoding='utf8')
    handle(h.read())
    h.close()

savelst('ks12.txt', ks12)
for i in range(1, 7):
    savelst('fb%02d.txt' % i, slst[i - 1])
