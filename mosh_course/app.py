# from utils import find_max
# from ecommerce import shipping

# first_student = find_max([45,45,64,64,46,7,45,7,49,78])
# print (first_student)

# shipping.calc_shipping()

# import random

# for i in range(30):
#     random_number = int(random.random()*100)
#     print(random_number)
# members = ["Clement", "Olives", "John", "Stephen", "Haggith"]

# leader = random.choice(members)
# print(leader)

# from utils import Dice

# dice = Dice
# roll_dice = dice.roll()
# print(roll_dice)

#PATH

from pathlib import Path

path = Path("emails")
if not path.exists():
    path.mkdir()
print(path.exists())
path_directory = Path()
for file in path_directory.glob("*"):
    print(file)
