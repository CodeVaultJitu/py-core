students = [["Rahul", 85], ["Anita", 92], ["Sam", 78]]

#accessing data
print(students[0]) #first student
print(students[1][0]) #seconds student's name
print(students[2][1]) #thrds student's marks

# Loop through nested list
for student in students:
    name = student[0]
    marks = student[1]
    print(f"{name} scored {marks}")

#in the loop student is a reusable variable , can be created then and there