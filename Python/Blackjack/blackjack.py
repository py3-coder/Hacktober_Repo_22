import random
from os import system
from sys import platform
from art import logo

def clear():
  if platform == "win32":
    _ = system("cls")
  else:
    _ = system("clear")

cards = [11,1,2,4,5,6,7,8,9,10,10,10,10,]
def deal_card():
  """Returns a random card from the deck"""
  card = random.choice(cards)
  return card

def calculate_score(cards):
  """ Returns the sum of cards"""
  if sum(cards) == 21 and len(cards) == 2:
    return 0
    
  if 11 in cards and sum(cards)>21:
    cards.remove(11)
    cards.append(1)
  
  return sum(cards)

def compare(user_score,computer_score):
  if user_score == computer_score:
    return "Draw"
  elif computer_score == 0:
    return "Computer has a blackjack, you lose."
  elif user_score == 0:
    return "You have a blackjack, you win."
  elif user_score > 21:
    return "You went over, you lose."
  elif computer_score >21:
    return "Computer went over, you win."
  elif user_score > computer_score:
    return "You win."
  else:
    return "You lose."
def blackjack():
  clear()
  print(logo)
  user_cards = []
  computer_cards = []
  for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
  is_game_over = False
  while not is_game_over:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print("Your cards: {}, current score: {}".format(user_cards,user_score))
    print("Computer's first card: {}".format(computer_cards[0]))

    if user_score == 0 or computer_score == 0 or user_score > 21:
      is_game_over = True
    else:
      user_should_deal = input("Type 'y' to deal another card, or type 'n' to pass: ")
      if user_should_deal == 'y':
        user_cards.append(deal_card())
      else:
        is_game_over = True

  while computer_score != 0 and computer_score<17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)

  print("Your final hand: {}, your final score {}.".format(user_cards,user_score))
  print("Computer's final hand: {}, computer's final score {}.".format(computer_cards,computer_score))
  print(compare(user_score,computer_score))

def main():
  should_continue = True
  while should_continue:
    user_input = input("Type 'y' to play 'BlackJack', type 'n' to end: ")
    if user_input == 'y':
      blackjack()
    else:
      should_continue = False
    
if __name__ == '__main__':
  main()
