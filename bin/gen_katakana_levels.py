#!/usr/bin/env python
# -*- coding: utf-8 -*-
import fileinput
import sys, codecs
sys.stdout = codecs.getwriter('utf-8')(sys.stdout)
import re
from levels import *
from unicodedata import *

#katakanaRE = re.compile('^[ァ-ンー]+$')
def is_katakana(word):
  letters = u'ァアィイゥウェエォオカガキギクグケゲコゴサザシジスズセゼソゾタダチヂッツヅテデトドナニヌネノハバパヒビピフブプヘベペホボポマミムメモャヤュユョヨラリルレロヮワヰヱヲンヴヵヶヷヸヹヺーヽヾㇰㇱㇲㇳㇴㇵㇶㇷㇸㇹㇺㇻㇼㇽㇾㇿ・'
  katakanaRE = re.compile('^[' + letters + ']+$')
  return  katakanaRE.match(word)

content = ''.join([line.decode('utf-8') for line in fileinput.input()]).replace('\n','')

words = tokenize(content)

katakana_words = [word for word in words if is_katakana(word)]

levels = sort_into_levels(list(' '.join(katakana_words))) 

ladder = []
[ladder.append([]) for i in range(len(levels))]

for word in set(katakana_words):
   rung = rank_word(word, levels)
   ladder[rung].append( word )

ladder = list(reversed(ladder))

for rung in ladder:
  print u'\u3010' + ''.join(sorted(set(''.join(rung))))  + u'\u3011'
  print len(rung)
  print 

storable = {}


for rung in ladder:
  storable[''.join(sorted(rung))]

exit()
for i, rung in enumerate(ladder):
  print  
  if len(rung)>0:
    print u'\u3010' + ''.join(sorted(set(''.join(rung))))  + u'\u3011'
  print '\n'.join(rung)

