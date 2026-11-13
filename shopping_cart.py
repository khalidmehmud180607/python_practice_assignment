name=input(("Coustomer Name: "))
a=range(3)
d={}
for i in a:
    namee=input("Product Name: ")
    price=int(input("Product Price: "))
    d.update({namee : price})
total=0
for i in d.values():
    total=total + i
if total > 4999:
    discount =total*20/100
elif total >2999:
    discount=total*10/100
else:
    discount=0
    print("----shopping summary----")
print(f"Coustomer Name: {name}\n")
i=1
for P,p in d.items():
    print(f"Product {i}: {P}\nPrice: {p:.2f}\n")
    i=i+1
print(f"Subtotal: {total:.2f}")
print(f"Discount: {discount:.2f}")
print(f"Final total: {total - discount:.2f}")