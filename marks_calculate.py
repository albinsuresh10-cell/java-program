# Program to calculate total, average, and grade
# Get marks for three subjects
subject1 = float(input("Enter marks for Subject 1: "))
subject2 = float(input("Enter marks for Subject 2: "))
subject3 = float(input("Enter marks for Subject 3: "))

# Calculate total and average
total = subject1 + subject2 + subject3
average = total / 3

# Calculate grade
if average >= 90:
    grade = "A"
elif average >= 80:
    grade = "B"
elif average >= 70:
    grade = "C"
elif average >= 60:
    grade = "D"
elif average >= 40:
    grade = "E"
else:
print("\n--- Student Mark Report ---")    grade = "F"
  print("Total Marks =", total)
print("Average Marks =", round(average, 2))
print("Grade =", grade)
