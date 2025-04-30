"""This code finds perimeter of triangle by given coordinates of its vertices """


import math


class Point:
    def __init__(self,x,y):
        self.__x = x
        self.__y = y

    def getx(self):
        self.__newx = self.__x
        return self.__newx

    def gety(self):
        self.__newy = self.__y
        return self.__newy


class Triangle:
    def __init__(self, vertice1, vertice2, vertice3):
        self.__vertices = [vertice1,vertice2,vertice3]


    def perimeter(self):
        self.__perim = 0
        for leg in range (3):
            if leg < 2:
                self.__leg = math.hypot((Point.getx(self.__vertices[leg]) - Point.getx(self.__vertices[leg+1])),(Point.gety(self.__vertices[leg]) - Point.gety(self.__vertices[leg+1])))
            else:
                self.__leg = math.hypot((Point.getx(self.__vertices[leg]) - Point.getx(self.__vertices[0])),(Point.gety(self.__vertices[leg]) - Point.gety(self.__vertices[0])))

            self.__perim +=self.__leg

        return self.__perim


triangle = Triangle(Point(0, 0), Point(1, 0), Point(0, 1))
print(triangle.perimeter())
