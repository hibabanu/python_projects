sum=0
total=0
attendance = [18, 20, 19, 15, 21]

for x in attendance:
    if (x>=20):
        print(f"{x}:attendence is full")
        sum = sum + 1
       

    else:
        print(f"{x}:attendence is not full")
    total=total+x    

print(f"days the class was full:{sum}")
print(f"The total attendance for all 5 days:{total}")