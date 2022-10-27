import os


print('''


                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\
                         `'-------'`
                       .-------------.
                      /_______________\


''')
bids={}
bidding_finished=False
while not bidding_finished:
  name=input("What is your name? ")
  price=int(input("What is your bid? $"))
  bids[name] = price
  d=input("Are there any other biddders? Type 'yes' or 'no' .\n")
  if d== "yes":
    os.system('clear')
  else :
    bidding_finished=True
    os.system('clear')
bid=0
for key in bids:
  if bids[key] > bid:
    bid=bids[key]
    winner=key
print(f"the winner is {winner} with a bid 0f ${bid}")    
