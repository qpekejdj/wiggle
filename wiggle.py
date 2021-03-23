import random
import time

#Change visual
back = '.'
wiggle_size = 50
snek = '0'
delay = 0.05
#Change visual

monkey= random.randint(0,wiggle_size)
while True:
    if monkey == wiggle_size+1:
        monkey = 0
    elif monkey == -1:
        monkey = wiggle_size
    print(back*monkey+snek+back*(wiggle_size-monkey))
    time.sleep(delay)
    funky = random.randint(0,4)
    if funky == 1:
        monkey = monkey+1
    elif funky == 2:
        monkey = monkey-1
    elif funky == 3:
        monkey = monkey
        


