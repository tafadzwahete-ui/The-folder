import random
pc_choices=("rock","paper","scizors")
CPU=random.choice(pc_choices)

me=input("lets play rock, paper,scizors what do you choose")

print("pc_choices",CPU)

if CPU==me:
      print('draw')
elif me==me and CPU:
      print("won")
elif CPU =="paper" and me=="rock":
      print("you lost")
elif CPU=="scizors" and me=="rock":
      print("u won")
elif CPU=="paper" and me=="scizors":
      print("wow")
elif CPU=="paper" and me=="rock":
      print("you lost")
else:
      print("lost")     
