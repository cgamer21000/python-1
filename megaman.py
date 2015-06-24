"the megaman quiz"

import colors as c
from utils import prompt

intro = c.clear + c.blue + 'welcome to the megaman quiz game' + c.reset

def q1():
    villian = prompt('who is the main villian of the megaman series')
    if villian == "dr.wily":
        print('you are correct')
        return True
    return False

def q2():
    person = prompt('who was the person who created megaman')
    if person == "dr.light":
        print('you are correct')
        return True
    return False

def q3():
    name = prompt('what is megaman's real name')
    if name == "rock":
        print('you got all the questions right you are the megaman master')
        return True
    return False

questions = [q1,q2,q3]
