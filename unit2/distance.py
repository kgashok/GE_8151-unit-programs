#!/usr/bin/env python3

from math import sqrt


def distance_between(pointA, pointB):
    '''returns the distance between two cartesian points

    @author kgashok
    @param pointA tuple containing x and y coordinates
    @param pointB tuple containing x and y coordinates

    @return float value representing distance'''

    x1, y1 = pointA
    x2, y2 = pointB

    distx = x1 - x2
    disty = y1 - y2

    return sqrt(distx**2 + disty**2)


# main program
# tuple packing allows for assigning
# multiple inputs in one statement
pointA = int(input("Enter x_cordinate for PointA ")), \
    int(input("Enter y_cordinate for PointA "))

pointB = int(input("Enter x_cordinate for PointB ")), \
    int(input("Enter y_cordinate for PointB "))

print("distance between points", distance_between(pointA, pointB))
