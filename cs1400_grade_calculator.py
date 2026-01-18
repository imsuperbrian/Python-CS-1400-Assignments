name = input("Enter your first name: ")
programming_assignments = float(input("enter your Program Assignments percentage: "))
quizzes = float(input("enter your Quizzes percentage: "))
labs = float(input("enter your Labs percentage: "))

print()

for i in range(6):
    midterm = i * 20

    results = (10 * programming_assignments + 25 * quizzes + 10 * labs + 55 * midterm) / 100
    print(name, "if your average midterm exam score is", midterm,
          "your course percentage for CS 1400 will be", str(results) + ".")
