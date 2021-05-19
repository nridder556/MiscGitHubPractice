
from Lifter import Lifter
import math


def main():
    first = 'Nick'
    last = 'Ridder'; weight=200;height=65;bench=335;squat=502.5;deadlift=615
    lifter_a = Lifter(first,last,weight,height,bench,squat,deadlift)
    txt = '{} {} has a total of {}'
    print(txt.format(first, last, lifter_a.getTotal()))
    print(lifter_a.getBMI())

main()





