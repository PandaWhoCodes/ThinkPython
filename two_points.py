"""
Write a function called distance_between_points
that takes two Points as arguments
and returns the distance between them.
"""
import math


def distance_between_points(x1, y1, x2, y2):
    return math.sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))


if __name__ == '__main__':
    z1 = int(input("Enter the First Point#1:"))
    z2 = int(input("Enter the Second Point#1:"))
    z11 = int(input("Enter the First Point#2:"))
    z22 = int(input("Enter the Second Point#2:"))
    print(distance_between_points(z1, z2,z11,z22))
