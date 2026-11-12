name=input(("Name: "))
print('\n')
a=range(3)
d={}
for i in a:
    namee=input("Product Name: ")
    price=int(input("Product Price: "))
    print("\n")
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
print(f"Subtotal: {total}")
print(f"Discount: {discount}")
print(f"Final total: {total - discount}")