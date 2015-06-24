"the random quiz"

import colors as c
from utils import prompt

intro = c.clear + c.magenta + 'welcome to the pink fluffy unicorns quiz game' + c.reset

def q1():
    color = prompt('what is the color of the unicorn fur')
    if color == "i dont care":
        print('you are correct')
        return True
    return False

def q2():
    dancing = prompt('what is the unicorn dancing on')
    if dancing == "what do you mean":
        print('you are good at this')
        return True
    return False

def q3():
    texture = prompt('use one word to describe the texture of thier magical fur')
    if texture == "you're not my dad":
        print('you got all the answers right congradgulations')
        return True
    return False

questions = [q1,q2,q3]
