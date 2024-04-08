from art import logo, vs
from game_data import data
import random

print(logo)

game_on = True
score = 0

option_a = random.choice(data)
option_b = random.choice(data)

while(game_on):
  if option_a == option_b:
    option_b = random.choice(data)

  
  print(f"Compare A: {option_a['name']} , {option_a['description']}, {option_a['country']}")
  print(vs)
  print(f"Against B: {option_b['name']}, {option_b['description']}, {option_b['country']}")

  answer = input("Who has more followers? Type 'A' or 'B': ").upper()

  if answer == 'A' or answer == 'B':
    if answer == 'A':
      if option_a['follower_count'] > option_b['follower_count']:
        score += 1
        
        option_a = option_b
        B = random.randint(0, len(data)-1)
        option_b = data[B]
        
        print(f"You're right! Current score: {score} \n")
      else:
        print(f"You are wrong, game over! Your final score: { score }")
        game_on = False
        
    if answer == 'B':
      if option_b['follower_count'] > option_a['follower_count']:
        score += 1
        
        option_a = option_b
  
        B = random.randint(0, len(data)-1)
        option_b = data[B]
        
        print(f"You're right! Current score: {score} \n")
      else:
        print(f"You are wrong, game over! Your final score: { score }")
        game_on = False
        
  else:
    print("\n Invalid input. Please type 'A' or 'B'")
    continue