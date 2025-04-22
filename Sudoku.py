#! /user/bin/env python
""" This code checks if the provided 9x9 matrix is a valid Sudoku"""

def enter_rows(row_number):
    # accepts values entered by user for rows
    print("Enter 9 digits for row #", row_number + 1," :")
    row_data = input()
    while len(row_data) != 9 or row_data.isdigit() == False or "0" in row_data:
        row_data = input("The entered string is not valid. Enter a 9 digit string:")
    return str(row_data)

def enter_sudoku():
    #forms 9x9 sudoku table
    sudoku =[]
    for row in range (9):
        sudoku.append(enter_rows(row))
    return sudoku

def check_column(sudoku):
    # checks if figures in columns repeat or not
    for col in range(9):
        column = []
        for ro in sudoku:
            column.append(ro[col])
        for dig in column:
            if column.count(dig)>1:
                return "No"
    return "Yes"

def check_quadr(sudoku):
    # checks if figures in 3x3 quadrants repeat or not
    quadr = []
    rows = [0,3,6]
    cols = [0,3,6]
    for ro in rows:
        for co in cols:
            row = 0 + ro
            while row < (3+ro) :
                col = 0 + co
                while col < (3+co):
                    quadr.append(sudoku[row][col])
                    col +=1
                row +=1


            for q in quadr:
                if quadr.count(q) > 1:
                    return "No"
            else:
                quadr = []
    return "Yes"


def sudoku_function(sudoku):
    # check if all entered values form sudoku
    for rows in sudoku:
        for dig in rows:
            if rows.count(dig) > 1:
                return "No"

        if check_column(sudoku) == "No":
                return "No"
        if check_quadr(sudoku) == "No":
            return "No"
    return "Yes"

# test1

row1 = "295743861"
row2 = "431865927"
row3 = "876192543"
row4 = "387459216"
row5 = "612387495"
row6 = "549216738"
row7 = "763524189"
row8 = "928671354"
row9 = "154938672"

sudoku1 =[row1,row2,row3,row4,row5,row6,row7,row8,row9]

print(sudoku_function(sudoku1)=="Yes")

# test2

row11 = "195743862"
row22 = "431865927"
row33 = "876192543"
row44 = "387459216"
row55 = "612387495"
row66 = "549216738"
row77 = "763524189"
row88 = "928671354"
row99 = "254938671"

sudoku2 = [row11,row22,row33,row44,row55,row66,row77,row88,row99]

print(sudoku_function(sudoku2)=="No")

print(sudoku_function(enter_sudoku()))

