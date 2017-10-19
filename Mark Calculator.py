import statistics
score_list = []
name_student = input("Enter the name of the student: ")
print("Please enter the 5 exam results fro the student")
for i in range(0, 5):
    x = 0
    while x == 0:
        try:
            score = int(input("Enter the score: "))
            while score > 100 or score < 0:
                score = int(input("Please enter a score that is between 0 and 100: "))
            x = 1
        except ValueError:
            print("Please enter a integer score")
    score_list.append(score)
print("The final result for " + name_student + " is " + str(statistics.mean(score_list)))
