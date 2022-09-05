rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random as rn
lists=[rock,paper,scissors]
choice=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))
comp_choice=rn.randint(0,2)
print(lists[choice])
print(f"Computer chose: {lists[comp_choice]}\n")
flag=True #False if computer wins
if comp_choice==choice:
  print("Woah its a draw")
elif comp_choice==0 and choice==2:
  flag=False
elif comp_choice==2 and choice==1:
  flag=False
elif comp_choice==1 and choice==0:
  flag=False

if(flag):
  print("You Win!")
else:
  print("You lose :(")
  