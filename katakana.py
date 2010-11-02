import re
import sys
from collections import defaultdict

def uptos(seq):
 return [''.join(seq[:i]) for i in range(1,len(seq)+1)]

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

def regexify(pattern):
  return re.compile('^[' + pattern + ']+$')

def make_ranking(words):
  levels = []
  commonest_letters = sorted_by_freq(''.join(words))
  for key in uptos(commonest_letters):
    key = ''.join(sorted(key))
    levels.append( (key, regexify(key), [])  )
  return levels

def rank_words(words, levels):
  ranking = defaultdict(list)
  for word in words:
    for key, matcher, matched in levels:
      if matcher.match(word): 
        matched.append(word) 
        break
  return levels

def list_to_html(li):
  html = []
  for e in li: html.append('<li><a target=_blank href=http://ja.wikipedia.org/wiki/' + e.replace(' ', '_') + '>' + e + '</a></li>')
  return '\n'.join(html)

if __name__ == "__main__":
  text = sys.stdin.read().decode('utf-8').replace('\n', ' ')
  levels = make_ranking(text)
  words = text.split()
  levels = rank_words(words, levels)
  current = set(levels[0][0])

  for i, (key, regex, words)  in enumerate(levels):
    wrapper = open('page.template').read().decode('utf-8')
    wrapper = wrapper.replace('<body>', '<body>%s')

    previous = current
    current = set(key)
    new_letters = ' '.join(current - previous)

    prev = "%.2d" % (int(i)-1)
    next = "%.2d" % (int(i)+1)

    sofar = "<a id=sofar>" + ''.join(previous) + "</a>"

    nav = "<nav><a id=home href=..>home</a> <a class=prev href=" + prev + ".html>%s</a> <strong>Level %d</strong> <a  class=next href=" + next + ".html>%s</a> " + sofar + "</nav>" 
    nav = nav % (prev, i, next)
   
    
    page = nav + u"<h1>Level %d: <span class=new_letter>%s</span></h1>\n<ol id=level>%s</ol>"
    
    wordlist = list_to_html(words)
    page = page % (i, new_letters, wordlist)
  
    out = open("levels/%.2d.html" % i, 'w')
    page = wrapper % page 
    out.write(page.encode('utf-8'))
    out.close()
  
