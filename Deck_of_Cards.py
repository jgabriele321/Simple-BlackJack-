import random,copy

class Card:
  def __init__(self, suit, face, value):
        self.suit = suit
        self.face = face
        self.value = value

class Deck:
  def __init__(self, amt):
    self.amt = amt
    self.card = []

    suit_options = ["SP","CL","DM","HRT"]
    face_options = [2,3,4,5,6,7,8,9,10,"J","Q","K","A"]
    value_options = [2,3,4,5,6,7,8,9,10,10,10,10,11]
    
    for s in range(0,4):
      for f in range(0,13):
        self.card.append(Card(suit_options[s],face_options[f],value_options[f]))

    self.card = self.card * self.amt
  
  def shuffle (self):
    shuffled_deck = random.shuffle(self.card)
    return shuffled_deck
    
  def queue_up (self, int):
    queue = []
    for i in range(0,int):
      queue.append(the_deck.card[int])
    
    return queue