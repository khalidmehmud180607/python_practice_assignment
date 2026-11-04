name=input("Enter student name: ")
print()
m=int(input("Enter Math marks: "))
e=int(input("Enter English marks: "))
p=int(input("Enter Python marks: "))
print(f"\nStudent name: {name}")
average=round((m+e+p)/3,2)
print(f"Average Marks: {average}")
if average>=80 :
    print("Final Grade: A+")
elif average>=70 :
    print("Final Grade: A-")
elif average>=60 :
    print("Final Grade: A+")
elif average>=50 :
    print("Final Grade: B")
elif average>=40 :
    print("Final Grade: C")
else:
    print("Final Grade: F")

