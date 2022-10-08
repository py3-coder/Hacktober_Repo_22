MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
end_of_task=True
while end_of_task:
  def update_resources(cofee):
    if (cofee == 'espresso'):
      resources["water"]-=50
      resources["coffee"]-=18
    elif (cofee == 'latte'):
      resources["water"]-=200
      resources["milk"]-=150
      resources["coffee"]-=24 
    elif (cofee == 'cappuccino'):
      resources["water"]-=250
      resources["milk"]-=100
      resources["coffee"]-=24 
  
  def check_resources(cofee):
    if cofee == 'espresso':
      if resources["water"]<50:
        print("Insufficient water")
        return 0
      elif resources["coffee"]<18:
        print("Insufficient coffee")
        return 0
    elif cofee == 'latte':
      if resources['water']<200:
        print("Insufficient water")
        return 0
      elif resources["milk"]<150:
        print("Insufficient milk")
        return 0  
      elif resources["coffee"]<24:
        print("Insufficient coffee")
        return 0
    elif cofee == 'cappuccino':
      if resources["water"]<250:
        print("Insufficient water")
        return 0
      elif resources["milk"]<100:
        print("Insufficient milk")
        return 0  
      elif resources["coffee"]<24:
        print("Insufficient coffee")
        return 0
  def report():
    for key in resources:
      print(f"{key}: {resources[key]}ml")
    print(f"Money: ${profit}")
    choice=input("What would you like? (espresso/latte/cappuccino): ")
    coffee(choice)
  
  def coin():
    print("please insert coins.")
    quarter=int(input("how many quarters?: "))
    dimes=int(input("how many dimes?: "))
    nickles=int(input("how many nickles?: "))
    pennies=int(input("how many pennies?: "))
    coin=0.25*quarter+0.10*dimes+0.05*nickles+0.01*pennies
    return coin
  
  def coffee(choice):
    global profit
    # choice=input("What would you like? (espresso/latte/cappuccino): ")
    if choice == 'report':
      report()
    else :
      if (choice == 'espresso'):
        check=check_resources(choice)
        if check == 0:
          end_of_task=False
        if check!=0:
          value=coin()
          change=round(value-1.5,2)
          profit+=1.5
          print(f"Here is ${change} in change")
          print("Here is your espresso. Enjoy!")
          update_resources(choice)
      elif (choice == 'latte'):
        check=check_resources(choice)
        if check == 0:
          end_of_task=False
        if check!=0:
          value=coin()
          change=round(value-2.5,2)
          profit+=2.5
          print(f"Here is ${change} in change")
          print("Here is your latte. Enjoy!")
          update_resources(choice)
      elif (choice == 'cappuccino'):
        check=check_resources(choice)
        if check == 0:
          end_of_task=False
        if check!=0:
          value=coin()
          change=round(value-3.0,2)
          profit+=3.0
          print(f"Here is ${change} in change")
          print("Here is your cappuccino. Enjoy!")
          update_resources(choice)
  
  choose=input("What would you like? (espresso/latte/cappuccino): ")
  coffee(choose)
