import random
import time

user_name = input("Hello, what's your name?")
print("Hello,", user_name)
print("Ready for a new band name...?")
#number = input("To generate a band name pick an umber between 0 and 10")

names = ["Dirty Socks", "Rotten Hearts", "Unstable Atoms", "Hackers", "The Dead", "Amoebas"]
time.sleep(5)
print(random.choice(names))
