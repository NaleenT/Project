
#Use each of these operators: +, *, /, =, %
#and, or, not
#if, elif, else
#while loop
#for loop
#Create a list and iterate through that list using a for loop to print each item out on a new line.
#Create a tuple and iterate through it using a for loop to print each item out on a new line.
#
#Define a function that returns a string variable.
#Call the function you defined above and print the result to the shell.


#Assign an integer to a variable.
#Assign a string to a variable.
#Assign a float to a variable.
Student_list = {"Emily": [3.7, "Math", 20], "Nate": [4.0, "English", 34], "Mary": [2.0, "English", 15], "Josh": [1.7, "Math", 40]}

#Use the print() function to print out the variable you assigned.
print(Student_list)

names = list(Student_list.keys())
gpas = [data[0] for data in Student_list.values()]
classes = [data[1] for data in Student_list.values()]
attendance = [data[2] for data in Student_list.values()]

total_gpa = 0
index = 0
while index < len(gpas):
    total_gpa += gpas[index]
    index += 1

curve = total_gpa / len(gpas)
print("The average GPA is " + str(round(curve, 1)))

total_days = 0
index_2 = 0
while index_2 < len(attendance):
    total_days += attendance[index_2]
    index_2 += 1

avg_attendance = total_days / len(attendance)
print("The average attendance is " + str(avg_attendance))

average_attendance_year = (total_days * 4)/len(attendance)

print("This is only the first quater. Attandance for the year should average " + str(average_attendance_year) + " days")




def check_pass_fail(student_data):
    if student_data[0] >= 2.8 and student_data[2] >= 20:
        return "Pass"
    elif student_data[0] <= 2.8 and student_data[2] <= 20:
        return "Fail"
    else:
        return "Not enough data"


def start():
    Name = input("Please search for a student: ")

    try:
        Student_data = Student_list[Name]
        print(f"GPA: {Student_data[0]}, Class: {Student_data[1]}, Attendance: {Student_data[2]}")
        more()
    
        Pass_Fail = check_pass_fail(Student_data)
        print(f"This student is on track to {Pass_Fail}")
        more()

    except KeyError:
        print("Try a different name")
        more()

def more():
    More = input("Would you like to search for another name?")
    if More == "No":
        quit()
    if More == "Yes":
        start()
    else:
        print("Please enter Yes or No.")
        more()    


start()




