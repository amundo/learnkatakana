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
  limit = len(commonest_letters)
  for i in range(limit):
    prefix = commonest_letters[:i+1]
    level = { 
      'new_letter' :  commonest_letters[i],
      'romaji' :  kana2romaji(commonest_letters[i]),
      'sofar' :  commonest_letters[:i],
      'regex' :  regexify(prefix),
      'number' :  "%.2d" % i,
      'next' :  "%.2d" % (i+1) if (i < limit) else "%.2d" % 0 ,
      'next_letter' :  commonest_letters[(i+1) % limit],
      'prev_letter' :  commonest_letters[(i-1)] if i > 1 else commonest_letters[0],
      'wordlist' : []
      'prev' :  "%.2d" % (i-1) if (i > 0) else "%.2d" % 0,
    }
    levels.append( level )
  return levels

def level_words(words):
  levels = make_levels(words)
  for word in words:
    for level in levels:
      if level['regex'].match(word):
        if len(word) < 12 and len(level['wordlist']) < 50: level['wordlist'].append(word) 
        break 
  return levels

def read_romaji2katakana(jsonfile='katakana.json'):
  rules = json.loads(open(jsonfile).read().decode('utf-8'))
  return dict(rules)

def romaji2kana(romaji):
  ruledict = read_romaji2katakana()
  return ruledict[romaji]

def invert_dict(d):
  return dict([(v,k) for k,v in d.items()])

def kana2romaji(romaji):
  return invert_dict(read_romaji2katakana())

if __name__ == "__main__":

  from string import Template 
  text = sys.stdin.read().decode('utf-8').replace('\n', ' ')

  page_template = Template(open('page.template').read().decode('utf-8'))
  word_template = Template(open('word.template').read().decode('utf-8'))

  words = text.split()
  levels = level_words(words)

  for level in levels:  
    level['page_title'] = 'Learn Katakana: ' + level['new_letter']
    level['wordlist'] = '\n'.join([word_template.substitute(word=w) for w in level['wordlist']])
    page = page_template.safe_substitute(level) 

    outfile = "levels/%s.html" % level['number']
    out = open(outfile, 'w')
    out.write(page.encode('utf-8'))
    out.close()
