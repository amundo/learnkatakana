#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import sys
import json
from collections import defaultdict


def freq(seq):
 fq = {}
 for e in seq:
  if e not in fq: fq[e] = 0
  fq[e] += 1
 return fq

def sorted_by_freq(seq):
 byfq = [(v,k) for k,v in freq(seq).items()]
 commonest =  ''.join([k for v,k in sorted(byfq, reverse=True)])
 return commonest 

def regexify(prefix):
  return re.compile('^[' + prefix + ']+$')

def make_levels(words):
  levels = []
  commonest_letters = sorted_by_freq(''.join(words))
  for i in range(1, len(commonest_letters)+1):
    prefix = commonest_letters[:i]
    regex =  regexify(prefix)
    level = { 
      'new_letter' :  prefix[-1],
      'sofar' :  prefix,
      'number' :  "%.2d" % i,
      'next' :  "%.2d" % (i+1),
      'prev' :  "%.2d" % (i-1),
      'wordlist' :  [word for word in words if len(word) < 10 and regex.match(word)][:40]
    }
    levels.append( level )
  for level in levels: print len(level['wordlist'])
  return levels

def read_romaji2katakana(jsonfile='katakana.json'):
  rules = json.loads(open(jsonfile).read().decode('utf-8'))
  return dict(rules)

def convert_to_kana(romaji):
  return ruledict[romaji]


if __name__ == "__main__":

  from string import Template 
  text = sys.stdin.read().decode('utf-8').replace('\n', ' ')

  page_template = Template(open('page.template').read().decode('utf-8'))
  word_template = Template(open('word.template').read().decode('utf-8'))

  words = text.split()
  levels = make_levels(words)

  for level in levels:  
    level['page_title'] = 'Learn Katakana: ' + level['new_letter']
    level['wordlist'] = '\n'.join([word_template.substitute(word=w) for w in level['wordlist']])
    page = page_template.safe_substitute(level) 

    outfile = "levels/%s.html" % level['number']
    out = open(outfile, 'w')
    out.write(page.encode('utf-8'))
    out.close()
