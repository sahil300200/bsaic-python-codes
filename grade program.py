marks=float(input("Enter marks;"))
if marks>=90:
    grade='A'
elif marks>=80:
    grade='B'
elif marks>=70:
    grade='C'
elif marks>=60:
    grade='D'
else:
   grade='F'
print("For marks",marks,"the grade is",grade)
