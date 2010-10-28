#!/usr/bin/env python
# coding: utf-8
import codecs, sys, unicodedata, re
sys.stdout = codecs.getwriter('utf-8')(sys.stdout)
from collections import defaultdict
from operator import itemgetter
from fileinput import input
from unicodedata import name

def read_unicode_input_stream():
  content = []
  for line in input(): content.append(line)
  content = ''.join(content)
  return content.strip().decode('utf-8')

def freq(seq):
  fq = defaultdict(int)
  for e in seq: 
    try: 
      n = name(e)
      if 'KATAKANA' in n: fq[e] += 1
    except: 
      continue
  return fq
 
if __name__ == "__main__":
  text = read_unicode_input_stream()
  letters = list(text)
  letterfq = freq(letters)
  
  for letter, fq in sorted(letterfq.items(), key=itemgetter(1)):
    print fq, letter, name(letter)



