#!/usr/bin/env python
from collections import defaultdict
from unicodedata import category

def depunctuate(content):
  depuncked = []
  
  for c in content:
    if c != u'\u30FB' and category(c)[0] in ('S', 'P') :  # symbol or punctuation
      depuncked.append(' ')
    else:
      depuncked.append(c)
  return ''.join(depuncked)

def tokenize(text):
  text = text.replace('\n',' ').replace('\t', ' ')
  text = depunctuate(text)
  words = []
  word = ''
  for c in text:
    if c == ' ' or category(c).startswith('P') and c != u'\u30FB':
      words.append(word)
      word = ''
    else:
      word += c
  return words

def split_into_letters(text):
  return list(text)

def frequency(sequence):
  count = {}
  for element in sequence:
    if element not in count: count[element] = 0
    count[element] += 1
  return count

def sorted_by_frequency(letters):
  count = frequency(letters)
  sortable = sorted([(count[letter], letter) for letter in count.keys()], reverse=True)
  return [letter for score, letter in sortable]

def sort_into_levels(content):
  letters = split_into_letters(content)
  commonest_letters = sorted_by_frequency(letters) # commonest first
  return [set(commonest_letters[:i]) for i in range(1, len(commonest_letters)+1)]

def rank_word(word, levels):
  for i, level in enumerate(levels):
    if set(word).issubset(level):
      return i
      break

if __name__ == "__main__":
  import fileinput
  content = ''.join([line.decode('utf-8') for line in fileinput.input()]).replace('\n','')
  levels = sort_into_levels(content)
  words = tokenize(content)
  for word in set(words):
    print rank_word(word, levels), word.encode('utf-8')
