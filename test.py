totalcourses = 6
courseentered = 0
denn = 0  #this represents
Unitcum = 0


while (courseentered < totalcourses):
    score = int(input("Enter your score: "))
    Units = int(input("Enter the course units: "))  # type: int
    if (score > 70):
        point = 5
    elif (score > 60 and score < 70):
        point = 4
    elif (score > 50 and score < 60):
        point = 3
    elif (score > 43 and score < 50):
        point = 1
    elif (score > 40 and score < 44):
        point = 0
    else:
        point = 0


    numerator = point * Units  # type: int
    print("the denom is ", numerator)
    print(Units)
    Unitcum += Units
    denn += numerator
    print("cumulated denom is ", denn)
    courseentered +=1
    print("course entered ", courseentered , "times. ")


cgpa =  denn/Unitcum
print("your CGPA is ", cgpa)


