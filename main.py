from Deck_of_Cards import *
from Helper import *
import random

number_of_decks = 6
the_deck = Deck(number_of_decks)
the_deck.shuffle()
counter = 0
gameCounter = 0
red_card = random.randint((len(the_deck.card)/2),len(the_deck.card)-2)
player_score = 0
dealer_score = 0
player_stack = 100
min_bet = 2
current_bet = 0 

def hit (person):
  global counter
  global the_deck
  person.append(the_deck.card[counter])
  counter +=1

def dealer_plays():
  global dealer
  
  while (getBestScore(dealer) < 17):
    hit(dealer)

  if (getBestScore(dealer) > 21):
    return "BUST"
  else:
    return getBestScore(dealer)

print("----- Welcome To BlackJack -----")

while True: 
  if (red_card < (counter - 10)):
    counter = 0
    red_card = random.randint((len(the_deck.card)/2),len(the_deck.card)-2)

  gameCounter += 1

  try:
    current_bet = int(input("How much would you like to bet? \n"))
  except:
    print("you need to bet an whole number")
    break

  if (current_bet > player_stack):
    print("get out of here you broke boi")
    break

  #Start the game by dealing out 4 cards
  print("Game: "+ str(gameCounter) + " Stack: " + str(player_stack) + " Your Bet: " + str(current_bet))
  dealer = [the_deck.card[counter], the_deck.card[counter + 1]]
  counter += 2
  player = [the_deck.card[counter], the_deck.card[counter + 1]]
  counter += 2

  print_table(dealer, player, 1)
  print("Your current score: " + str(getBestScore(player)))
  player_score = getBestScore(player)
  
  answer = input("Would you like to hit or stay? Spacebar + Enter to hit \n")
  while (answer == " "):
    hit(player)
    print_table(dealer, player, 1)
    print("Your current score: " + str(getBestScore(player)))
    player_score = getBestScore(player)
    if(getBestScore(player) > 21):
      player_score = "BUST"
      print("")
      print("oh you busted :(")
      print("")
      break
    answer = input("Would you like to hit or stay? Spacebar + Enter to hit \n")
  
  dealer_score = dealer_plays()
  print_table(dealer, player, 0)
  print("Your Score: " + str(player_score))
  print("Dealer Score: " + str(dealer_score))

  if (player_score == "BUST"):
    print("")
    print("you busted so you lost")
    player_stack -= current_bet
  elif (dealer_score == "BUST"):
    print("")
    print("the dealer busted so you won!")
    player_stack += current_bet
  elif (dealer_score == player_score):
    print("")
    print("it's a tie!")
  elif (player_score > dealer_score):
    print("")
    print("you win!")
    player_stack += current_bet
  else:
    print("")
    print("you lost")
    player_stack -= current_bet

  print("Your Stack = " + str(player_stack))
  print("")
  answer = input("another game? spece + enter to play again \n")
  if (answer != " "):
    break
    
    

print("-- Game Over --")
print("You Played " + str(gameCounter) + " Games")
print("Your Stack: " + str(player_stack))