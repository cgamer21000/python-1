"""This is my utils library with awesome stuff."""

import colors as c

def prompt(question):
    print(c.red + question + c.reset)
    answer = input("> " + c.base3).lower().strip()
    print(c.reset)
    return answer

if __name__ == '__main__':
    testanswer = prompt("Whatever")
    print(testanswer)
