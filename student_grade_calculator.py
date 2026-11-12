name=input("Name: ")
bn=int(input("Bangla marks: "))
en=int(input("English marks: "))
m=int(input("Math marks: "))
total=bn +en + m
average=float(total/3)
print(f"Student Name: {name}")
print(f"Total Marks: {total}")
print(f"Average: {average:.2f}")
if average>79:
    print("Grade: A+")
elif average>69:
    print("Grade: A")
elif average>59:
    print("Grade: B")
elif average>49:
    print("Grade: C")
else:
    print("Grade: F")