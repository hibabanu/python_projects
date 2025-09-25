

import os
number= int(input("Enter the number of students: "))

if os.path.exists("students.txt"):
    f= open("students.txt","a")
    for i in range(number):
        names= input(f"Enter the name of the student {i+1}: ")
        f.write(names + "\n")
    f.close()

else:
    
    f= open("students.txt","w")
    for i in range(int(number)):
        names= input(f"Enter the name of the student{i+1}: ")
        f.write(names + "\n")
    f.close()

print("updated list of students:")
f = open("students.txt", "r")
all_names = f.readlines()
f.close()

for name in all_names:
    print(name.strip())