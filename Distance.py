"""This class calculates distance between two given poitns and between one point and given cooredinates x and y"""
import math


class Point:
    def __init__(self, x=0.0, y=0.0):
        self.__x = x
        self.__y = y

    def getx(self):
        self.__pointx = self.__x
        return self.__pointx

    def gety(self):
        self.__pointy = self.__y
        return self.__pointy

    def distance_from_xy(self, x, y):
        self.__newx = x
        self.__newy = y
        self.__lenthxy = math.hypot((self.__newx-self.getx()),(self.__newy-self.gety()))
        return self.__lenthxy

    def distance_from_point(self, point):
        self.__distance12 = math.hypot((self.__x-point.getx()),(self.__y-point.gety()))
        return self.__distance12



point1 = Point(0, 0)
point2 = Point(1, 1)
print(point1.distance_from_point(point2))
print(point2.distance_from_xy(2, 0))
