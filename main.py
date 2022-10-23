import random

def guess(x):
  random_number = random.randint(1, x)
  guess = 0
  while guess != random_number:
    guess = int(input(f'Guess a number between 1 and {x}: '))
    if guess < random_number:
      print('Sorry, guess again. Too low.')
    elif guess > random_number:
      print('Sorry, guess again. Too high.')
  
  print(f'Yay, congrats! You have guessed the number {random_number} correctly.')
    
def computer_guess(x):
  low = 1
  high = x
  feedback = ''
  while feedback != 'c':

    if low != 'c':
      guess = random.randint(low,high)
    else:
      guess = low #could also be high bc low = high

    feedback = input(f'Is {guess} too high(H), too low (L), or correct (C)? ').lower()
    if feedback == 'h':
      high = guess - 1
    elif feedback == 'l':
      low = guess + 1

    if low > high:
      print(f'Heey, you told me something wrong... You said is bigger than {low} and lower than {high}!?')
      quit()

  print(f'Yay! The computer guessed your number {guess}, correctly!')


def main():
  x = 1000 #define your range here.
  game = int(input(f'What game do you want to play? \n \
  1 - Try to guess a number set by the computer; \n \
  2 - The computer try to guess your number (between 1 and {x}). \n Answer: '))
  
  if game == 1:
    guess(x)
  elif game == 2:
    computer_guess(x)
  else:
    print(f'Sorry, I don\'t understand your game.')
    exit()

main()