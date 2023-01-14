def makeHand(list,hideBool):
  
  if (hideBool):
    output ="[ X ] "
    for x in range(len(list)):
      if x > 0:
        temp = "[" + str(list[x].face) + " " + list[x].suit + "]"
        output += temp 
      
    return output
  else:
    output =""
    for x in list:
      temp = "[" + str(x.face) + " " + x.suit + "]"
      output += temp 
    return output

def getBestScore(list):
  number = 0
  temp = 0

  for x in range(len(list)):
    number += list[x].value
    
  if (number <= 21):
    return number
  else:
    number = 0
    for x in range(len(list)):
      temp = list[x].value
      if (temp != 11):
        number += temp
      else:
        number += 1

    return number

def print_table(dealer, player, show):
  
  print("")
  print("The dealer shows:")
  print(makeHand(dealer,show))
  print("You have:")
  print(makeHand(player,0))
  print("")
  