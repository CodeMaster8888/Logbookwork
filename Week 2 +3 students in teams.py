# Test table
#   No.Students         No.Teams            No.studentsleft
#   100                 20`                 0
#   76                  15                  1
#   28                  5                   3
x = 0
while x == 0:
    try:
        students_at_school = int(input("Enter the number of students at the school: "))
        while students_at_school < 0:
            students_at_school = int(input("You can't have negative students so please enter a postive value: "))
        x = 1
    except ValueError:
        print("Please enter the number of students at your school which is an integer.")
if students_at_school == 0:
    print("Sorry you don't have any students so you won't be able to have any teams. ")
    exit()
x = 0
while x == 0:
    try:
        team_size = int(input("Enter the size of the team you would like: "))
        while team_size <= 0:
            if team_size == 0:
                team_size = int(input("Sorry you need to enter a positive value which is greater than zero: "))
            else:
                team_size = int(input("You can't have a negative size team so please enter a positive value: "))
        x = 1
    except ValueError:
        print("Please enter the size of your team which is an integer.")
number_of_teams = students_at_school // team_size
students_leftover = students_at_school - (number_of_teams * team_size)
print("The amount of teams the can have is " + str(number_of_teams))
print("The number of students who won't be able to play are " + str(students_leftover))
