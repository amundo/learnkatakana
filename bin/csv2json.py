import json
import sys
import csv

#csv_file = sys.argv[1]		
csv_file = 'katakana.csv'	

reader = csv.reader(open(csv_file))

lines = [line for line in reader]

def unicodeize(codepoint):
  return unichr(int(codepoint, 16))

rules = [(v, unicodeize(k)) for k, v in lines]

rules = [(name, letter) for name, letter in rules if 'HALFWIDTH' not in name]

print json.dumps(rules)

