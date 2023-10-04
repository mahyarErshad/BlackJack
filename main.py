import random
from art import logo

print(logo)
print("Welcome to my Casino!")

#Variables
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
state = {
    "user": {
        "cards": [],
        "score": 0,
    },
    "ai": {
        "cards": [],
        "score": 0,
    },
    "game_over": False,
    "winner" : "",
    "loser": ""
}

#Functions
def deal_cards(player):
  if sum(state["ai"]["cards"]) > 17 and player == "ai":
    print("Dealer has passed their cards...")
  elif state["game_over"] == False:
    card = random.choice(cards)
    state[player]["cards"].append(card)
  else:
    return
  
def show_scores(player):
  if player == "ai":
    if state["game_over"] == False:
      name = "Dealer"
      shown_cards = state[player]['cards'][:-1]
    else:
      name = "Dealer's final"
      shown_cards = state[player]['cards']
  else:
      name = "Your"
      shown_cards = state[player]['cards']
  print(
      f"{name} cards are: {shown_cards} with a score of {sum(shown_cards)}")

def calculate_scores():
  for user in state:
    if user in ["user", "ai"]:
      name = state[user]
      cards = name["cards"]
      if sum(cards) > 21 and 11 in cards:
          cards.remove(11)
          cards.append(1)
      show_scores(user)
      name["score"] = sum(cards)
      
def winner_check():
    calculate_scores()
    for user in state:
        if user in ["user", "ai"]:
            if state[user]["score"] == 21:
                state["winner"] = user
                state["game_over"] = True
            elif state[user]["score"] > 21:
                state["loser"] = user
                state["game_over"] = True
    if state["game_over"] == True and state["ai"]["score"] < 21 and state["user"]["score"] < 21:
        if state["ai"]["score"] > state["user"]["score"]:
            state["winner"] = "ai"
        elif state["ai"]["score"] == state["user"]["score"]:
            state["winner"] = "draw"
        elif state["ai"]["score"] < state["user"]["score"]:
            state["winner"] = "user"

  
#Runtime
for _ in range(2):
    deal_cards("user")
    deal_cards("ai")

winner_check()

while state["game_over"] == False:
  should_continue = input("Do you want another card? (y or n)\n").lower()
  if should_continue == "y":
    deal_cards("user")
    deal_cards("ai")
    winner_check()
  elif should_continue == "n":
    while state["ai"]["score"] < 17:
      deal_cards("ai")
      winner_check()
    else:
      state["game_over"] = True

if state["game_over"] == True:
  winner_check()
  if state["winner"] == "user" or state["loser"] == "ai":
    print("You have won the game!")
  elif state["winner"] == "ai" or state["loser"] == "user":
    print("Sorry, You have lost the game!")
  else:
    print("It's a draw")