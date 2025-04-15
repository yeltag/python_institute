""" transfers integer numbers into seven-segment display view"""

def sev_seg_display(number):
    error = False
    for figure in number:
        if figure in "1234567890":
            error = False
        else:
            error = True
            break
    if not error:
        n = print(line_one(number), line_two(number), line_three(number), line_four(number), line_five(number), sep="\n")
        return n
    else:
        sev_seg_display(str(input("You have entered wrong value. Enter an integer number:")))
def line_one(number):
    line1 = ""
    for figure in number:
        if figure == "1":
            add_line = "  #"
        elif figure == "4":
            add_line = "# #"
        else:
            add_line = "###"
        line1 = line1 + "  " + add_line
    return line1

def line_two(number):
    line2 = ""
    for figure in number:
        if figure in "1237":
            add_line = "  #"
        elif figure in "56":
            add_line = "#  "
        else:
            add_line = "# #"
        line2 = line2 + "  " + add_line
    return line2

def line_three(number):
    line3 = ""
    for figure in number:
        if figure in "17":
            add_line = "  #"
        elif figure in "0":
            add_line = "# #"
        else:
            add_line = "###"
        line3 = line3 + "  " + add_line
    return line3

def line_four(number):
    line4 = ""
    for figure in number:
        if figure in "134579":
            add_line = "  #"
        elif figure in "2":
            add_line = "#  "
        else:
            add_line = "# #"
        line4 = line4 + "  " + add_line
    return line4

def line_five(number):
    line5 = ""
    for figure in number:
        if figure in "147":
            add_line = "  #"
        else:
            add_line = "###"
        line5 = line5 + "  " + add_line
    return line5

sev_seg_display(str(input("Enter an integer number:")))
