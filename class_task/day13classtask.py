
import os
item= input("Enter the item: ")

if os.path.exists("items.txt"):
    f= open("items.txt","a")
    f.write(f"{item}\n")

else:
    f= open("items.txt","w")
    f.write(f"{item}\n")

f.close()
f= open("items.txt","r")
print(f.read())