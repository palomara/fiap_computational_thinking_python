# weight 2
lab_project = float(input("Insert lab's poject grade: "))
# weight 3
semiannual_grade = float(input("Insert  semiannual grade: "))
#weight 5
final_exam = float(input("Insert final exam: "))

weighted_arithmetic_mean = (lab_project * 2 + semiannual_grade * 3 + final_exam * 5)/ (2 + 3 + 5)

print("Mean: ", weighted_arithmetic_mean)

if 8 <= weighted_arithmetic_mean <= 10:
    print("Conceito A")
elif 7 <= weighted_arithmetic_mean <= 7.9:
    print("Conceito B")
elif 6 <= weighted_arithmetic_mean <= 6.9:
    print("Conceito C")
elif 5 <= weighted_arithmetic_mean <= 5.9:
    print("Conceito D")
else:
    print("Conceito E")
