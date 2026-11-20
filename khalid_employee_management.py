import sys
#function to add new employee information into the list and then store in .txt file
def add_employee():
    while(True):
        try:
            employee_name=input("Enter employee name: ").strip().title()
            if(employee_name==""):
                raise ValueError ("Error! Name cant be empty!")
            words_list=employee_name.split()
            if not all (word.isalpha() for word in words_list):
                raise TypeError("Error ! Cant enter a number or special sign in name !")
        except ValueError as e:
            print(e)
            print("Enter the name again...\n")
        except TypeError as e:
            print(e)
            print("Enter the name again...\n")
        except EOFError as e:
            print(e)
            print("Enter the name again...\n")
        except Exception as e:
            print(e)
            print("Enter the name again...\n")
        else:
            print("Name entered successfully\n")
            break
    while(True):
        try:
            employee_Id=input("Enter employee id : ").strip().title()
            if(employee_Id==""):
                raise ValueError ("Error! Id cant be empty!")
        except ValueError as e:
            print(e)
            print("Enter the Id again...\n")
        except EOFError as e:
            print(e)
            print("Enter the Id again...\n")
        except Exception as e:
            print(e)
            print("Enter the Id again...\n")
        else :
            print("Id entered successfully\n")
            break
    while(True):
        try:
            salary=int(input("Enter salary : ").strip())
            if (salary<0):
                raise TypeError("Salary cant be negative")
        except EOFError as e:
            print(e)
            print ("Plz enter salary again...\n")
        except TypeError as e:
            print (e)
            print ("Plz enter salary again...\n")
        except ValueError:
            print ("Invalid value")
            print ("Plz enter salary again...\n")
        except Exception as e:
            print (e)
            print ("Plz enter salary again...\n")
        else:
            print("Salary entered successfully\n")
            break
    data=f"Employee info\nEmployee name: {employee_name}\nEmployee Id : {employee_Id}\nEmployee salary : {salary}\n\n"
    with open("employees.txt",'a') as f:
        f.write(data)
    input("Tap enter to continue : ")
#function to view information of all the employee
def view_employee():
    with open("employees.txt",'r',encoding='utf-8') as f:
        print(f.read())
    input("Tap anywhere to continue : ")
#programme start from here the upper part is for function
print("-----Welcome to the app-----")
while(True):
    print("Option 1)Add employee\nOption 2)View employee information\nOption 3)Quit")
    while(True):
        try:
            option=int(input("Choose a option : ").strip())
            if(option != 1 and option != 2 and option != 3):
                raise LookupError ("Error ! Only 1 ,2 ,3 are allowed!")
        except EOFError as e:
            print(e)
            print("Plz choose option again...\n")
        except LookupError as e:
            print (e)
            print ("Plz choose option again...\n")
        except ValueError:
            print ("Invalid value")
            print("Plz choose option again...\n")
        except Exception as e:
            print (e)
            print ("Plz choose again...\n")
        else :
            print("Successfully option selected\n")
            break
    if(option==1):
        add_employee()
    elif(option==2):
        view_employee()
    elif(option==3):
        sys.exit()