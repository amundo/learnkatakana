#!/usr/bin/env python
# -*- coding: utf-8 -*-
import fileinput
import sys, codecs
sys.stdout = codecs.getwriter('utf-8')(sys.stdout)
import re
from unicodedata import *

def is_kana_and_latin(line):
  letters = u' \ta-zA-Zァアィイゥウェエォオカガキギクグケゲコゴサザシジスズセゼソゾタダチヂッツヅテデトドナニヌネノハバパヒビピフブプヘベペホボポマミムメモャヤュユョヨラリルレロヮワヰヱヲンヴヵヶヷヸヹヺーヽヾㇰㇱㇲㇳㇴㇵㇶㇷㇸㇹㇺㇻㇼㇽㇾㇿ・'
  pattern = u'^[' + letters + u']+$'
  katakanaRE = re.compile(pattern)
  return  katakanaRE.match(line)

#content = ''.join([line.decode('utf-8') for line in fileinput.input()]).replace('\n','')

for line in fileinput.input():
  line = line.strip()
  try: 
    line = line.decode('utf-8')
    if is_kana_and_latin(line): print line
  except:
    continue

