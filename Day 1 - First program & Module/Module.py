import pyjokes
import random

#Get a random joke
joke = pyjokes.get_joke()
print(joke)
print()

#Get a random choice
print(random.choice(['stone', 'paper', 'scissors']))