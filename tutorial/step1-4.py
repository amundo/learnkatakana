#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Step 1: Get a bunch of text in the alphabet in question. In reality you'll need waaay more text than this.
text = u"""
Τις διατροφικές συνήθειες των αρχαίων Ελλήνων χαρακτήριζε η λιτότητα, κάτι που αντικατοπτρίζει τις δύσκολες συνθήκες υπό τις οποίες διεξάγεται η ελληνική γεωργική δραστηριότητα. Θεμέλιό τους ήταν η λεγόμενη «μεσογειακή τριάδα»:[α] σιτάρι, λάδι και κρασί.
Στη βάση της διατροφής των αρχαίων Ελλήνων συναντούμε τα δημητριακά, κυρίως σιτάρι σκληρό, όλυρα και κριθάρι. Το σιτάρι έφτανε στο τραπέζι ως πλιγούρι, ως συστατικό του χυλού και φυσικά ως αλεύρι, από το οποίο παρασκευαζόταν ο άρτος και οι γαλέττες. Τα δημητριακά συνοδεύονταν συνήθως από οπωροκηπευτικά (λάχανα, κρεμμύδια, φακές, κουκιά και ρεβύθια). Η κατανάλωση κρέατος και θαλασσινών σχετιζόταν με την οικονομική κατάσταση της οικογένειας, αλλά και με το αν κατοικούσε στην πόλη, στην ύπαιθρο ή κοντά στη θάλασσα. Οι Έλληνες κατανάλωναν ιδιαιτέρως τα γαλακτοκομικά και κυρίως το τυρί. Το βούτυρο ήταν γνωστό, αλλά έχανε σε προτιμήσεις σε σχέση με το ελαιόλαδο. Το φαγητό συνόδευε κρασί (κόκκινο, λευκό ή ροζέ) αναμεμειγμένο με νερό.
Πληροφορίες για τις διατροφικές συνήθειες των αρχαίων Ελλήνων παρέχουν τόσο οι γραπτές μαρτυρίες όσο και διάφορες καλλιτεχνικές απεικονίσεις: οι κωμωδίες του Αριστοφάνη και το έργο του γραμματικού Αθήναιου από τη μία πλευρά, τα κεραμικά αγγεία και τα αγαλματίδια από ψημένο πηλό από την άλλη.
""" # Some Greek from <a href=http://el.wikipedia.org/wiki/Διατροφή_στην_αρχαία_Ελλάδα>http://el.wikipedia.org/wiki/Διατροφή_στην_αρχαία_Ελλάδα</a>. I have no idea what this is going on about.

text = text.replace('\n',' ')

# Step 2a: letters...
letters = list(text)

# Step 2b: words...
words = text.split(' ')
# This is the crudest possible tokenizer.

# Step 4, okay we need a bit of code here.

def make_tally(letters):
  tally = {}
  for letter in letters:
    if letter not in tally:
      tally[letter] = 0 # initialize
    tally[letter] += 1 
  return tally

tally = make_tally(letters)

def sort_by_tally(tally):
  sorted_tally = sorted([(score, letter) for letter, score in tally.items()])
  sorted_tally = list(reversed(sorted_tally)) # we want most common first.
  return [letter for score, letter in sorted_tally]

letters_by_tally = sort_by_tally(tally)

