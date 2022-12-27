from art import logo, vs
from game_data import data
from replit import clear
import random

score = 0
def validate(guess, compare, against):
  global score
  if guess == 'A':
    if compare['follower_count'] > against['follower_count']:
      score += 1
      print(f"You're right! Current score: {score}")
    else:
      print(f"Sorry, that's wrong. Final score: {score}")
      return False
  else:
    if against['follower_count'] > compare['follower_count']:
      score += 1
      print(f"You're right! Current score: {score}")
    else:
      print(f"Sorry, that's wrong. Final score: {score}")
      return False
  return True

def high_low():
  compare = random.choice(data)
  against = random.choice(data)
  answer = True
  while answer:
    # Check that A and B are not the same
    if against == compare:
      against = random.choice(data)
    
    print(f"Compare A: {compare['name']}, a {compare['description']}, from {compare['country']}.")
    print(vs)
    print(f"Against B: {against['name']}, a {against['description']}, from {against['country']}.")
    guess = input("Who has more followers? Type 'A' or 'B': ").upper()
    clear()
    print(logo)
    answer = validate(guess, compare, against)
    if answer:
      compare = against

print(logo)
high_low()