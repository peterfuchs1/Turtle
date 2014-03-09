#!/usr/bin/python
"""       turtle-example-suite:

         tdemo_minimal_hanoi.py

The minimal 'Towers of Hanoi' animation
minimally enhanced: User is asked for the
number N of discs (2<=N<=8) (using
numinput()  -- NEW in Python 3.1)

A tower of N discs is transferred from the
left to the right peg.

An imho quite elegant and concise
implementation using a tower class, which
is derived from the built-in type list.

Discs are turtles with shape "square", but
stretched to rectangles by shapesize()
 ---------------------------------------
       To exit press STOP button
 ---------------------------------------
"""
from turtle import *

N = 5

class Disc(Turtle):
    def __init__(self, n):
        Turtle.__init__(self, shape="square", visible=False)
        self.pu()
        self.shapesize(1.5, n*(9./N), 2) # square-->rectangle
        self.fillcolor(n/float(N), 0, 1-n/float(N))
        self.st()

class Tower(list):
    "Hanoi tower, a subclass of built-in type list"
    def __init__(self, x):
        "create an empty tower. x is x-position of peg"
        self.x = x
    def push(self, d):
        d.setx(self.x)
        d.sety(-150+34*len(self))
        self.append(d)
    def pop(self):
        d = list.pop(self)
        d.sety(150)
        return d

def hanoi(n, from_, with_, to_):
    if n > 0:
        hanoi(n-1, from_, to_, with_)
        to_.push(from_.pop())
        hanoi(n-1, with_, from_, to_)

def play():
    onkey(None,"space")
    clear()
    hanoi(N, t1, t2, t3)
    write("press STOP button to exit",
          align="center", font=("Courier", 16, "bold"))

def main():
    global t1, t2, t3, N
    ht(); penup(); goto(0, -225)   # writer turtle
    t1 = Tower(-250)
    t2 = Tower(0)
    t3 = Tower(250)
    # make tower of 6 discs
    N = int(numinput("Number of HANOI Discs",
                     "How many discs (2 - 8)?", 5, 2, 8))
    for i in range(N,0,-1):
        t1.push(Disc(i))
    # prepare spartanic user interface ;-)
    write("press spacebar to start game",
          align="center", font=("Courier", 16, "bold"))
    onkey(play, "space")
    listen()
    return "EVENTLOOP"

if __name__=="__main__":
    msg = main()
    print(msg)
    mainloop()
