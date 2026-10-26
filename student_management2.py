students=[]
def load_students():
    try:
        with open("students.txt","r")as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                data=line.split(",")
                if len(data) != 4:
                    continue
                roll, name, age, branch = data
                if any(student["roll"] == roll for student in students):
                    print("Duplicate roll number:", roll)
                    continue
                if not roll.isdigit():
                    print("Invalid roll number:", roll)
                    continue
                if not name.replace(" ", "").isalpha():
                    print("Invalid student name:", name)
                    continue
                if not age.isdigit() or not (1 <= int(age) <= 100):
                    print("Invalid age:", age)
                    continue
                if not branch.replace(" ", "").isalpha():
                    print("Invalid branch:", branch)
                    continue
                student={
                     "roll": roll,
                    "name": name,
                    "age": age,
                    "branch": branch
                }
                students.append(student)
    except FileNotFoundError:
        print("students.txt file not found!")
load_students()
def add_student():
    roll=input("enter Roll Number:").strip()
    if not roll.isdigit():
        print("Please enter a valid Roll Number!")
        return
    for student in students:
        if student["roll"]==roll:
            print("Roll Number already exists!")
            return
    name=input("Enter Name:").strip()
    if not name.replace(" ", "").isalpha():
        print("Please enter a valid name!")
        return
    if not name:
        print("please enter a valid name!")
        return
    try:
        age=int(input("enter age:"))
    except ValueError:
        print("please enter a valid age!")
        return
    if age<1 or age>100:
        print("please enter a valid age!")
        return
    branch=input("Enter Branch:").strip()
    if not branch.replace(" ", "").isalpha():
        print("Please enter a valid branch!")
        return
    if not branch:
        print("please enter a valid branch!")
        return
    student={
        "roll":roll,
        "name":name,
        "age":age,
        "branch":branch
    }
    students.append(student)
    with open("students.txt","a")as file:
        file.write(
            student["roll"]+","+
            student["name"]+","+
            str(student["age"])+","+
            student["branch"]+"\n"
        )   
    print("Student Added Successfully!")
def view_students():
    if not students:
        print("No students found!")
        return
    else:
        branch_count={}
        total_age=0
        oldest_age=0
        youngest_age = 101
        print("Total students:",len(students))
        students.sort(key=lambda student: int(student["roll"]))
        for i, student in enumerate(students, start=1):
            total_age=total_age+int(student["age"])
            if int(student["age"]) > oldest_age:
                oldest_age = int(student["age"])
            if int(student["age"]) < youngest_age:
                youngest_age = int(student["age"])
            branch = student["branch"].lower()
            branch_count[branch] = branch_count.get(branch, 0) + 1
            print("Student",i)
            print("--------------------")
            print("Roll Number:", student["roll"])
            print("Name:", student["name"])
            print("Age:", student["age"])
            print("Branch:", student["branch"])
            print("--------------------")
    average_age = total_age / len(students)
    print("Average Age:", round(average_age,2))
    print("Oldest Student Age:", oldest_age)
    print("Youngest Student Age:", youngest_age)
    print("Branch-wise Student Count:")
    for branch, count in sorted(branch_count.items()):
        print(branch.upper(), ":", count)
def search_student():
    print("1. Search by Roll Number")
    print("2. Search by name")
    print("3. Search by Branch")
    choice=input("enter your choice:")
    if choice!="1" and choice!="2" and choice!="3":
        print("Invalid choice!")
        return
    if choice=="1":
        roll=input("enter Roll Number:").strip()
        if not roll:
           print("Please enter a roll number!")
           return
        if not roll.isdigit():
            print("Please enter a valid roll number!")
            return
        found=False
        count=0
        for student in students:
            if student["roll"]==roll:
                print("Student found!")
                print("Roll Number:",student["roll"])
                print("Name:",student["name"])
                print("Age:",student["age"])
                print("Branch:",student["branch"])
                found=True
                count+=1
        if found:
            print("Students Found:",count) 
        if not found:
            print("Student not Found!")
    if choice=="2":
        name=input("enter name:").strip()
        if not name:
            print("Please enter a name!")
            return
        if not name.replace(" ", "").isalpha():
            print("Please enter a valid name!")
            return
        found=False
        count=0
        for student in students:
            if name.lower() in student["name"].lower():
                print("Student found!")
                print("Roll Number:",student["roll"])
                print("Name:",student["name"])
                print("Age:",student["age"])
                print("Branch:",student["branch"])
                found=True
                count+=1
        if found:
            print("Students Found:",count)
        if not found:
            print("Student not Found!")
    if choice == "3":
        branch = input("Enter Branch:").strip()
        if not branch:
           print("Please enter a branch!")
           return
        if not branch.replace(" ", "").isalpha():
            print("Please enter a valid branch!")
            return
        found = False
        count = 0
        for student in students:
            if student["branch"].lower() == branch.lower():
                print("Student found!")
                print("Roll Number:", student["roll"])
                print("Name:", student["name"])
                print("Age:", student["age"])
                print("Branch:", student["branch"])
                found = True
                count += 1
        if found:
            print("Students Found:", count)
        if not found:
            print("Student not Found!")        
def update_student():
    roll=input("enter Roll Number:").strip()
    if not roll:
        print("Please enter a roll number!")
        return
    if not roll.isdigit():
        print("Please enter a valid Roll Number!")
        return
    found=False
    for student in students:
        if student["roll"]==roll:
            confirm=(input("Are you sure you want to update? (yes/no):").strip().lower())
            if confirm == "no":
                print("Update cancelled!")
                found = True
                break
            elif confirm!="yes":
                print("Please enter yes or no!")
                found=True
                break
            print("Student found!")
            name=input("enter New name:").strip()
            if not name:
                print("please enter a valid name!")
                return
            if not name.replace(" ", "").isalpha():
                print("Please enter a valid name!")
                return
            try:
                age=int(input("enter age:"))
            except ValueError:
                print("please enter a valid age!")
                return
            if age<1 or age>100:
                print("please enter a valid age!")
                return
            student["age"]=age
            branch=input("enter New branch:").strip()
            if not branch or not branch.replace(" ", "").isalpha():
                print("please enter a valid branch!")
                return
            student["name"] = name
            student["age"] = age
            student["branch"]=branch
            found=True
            print("Student updated successfully!")
            with open("students.txt","w")as file:
                for student in students:
                    file.write(
                        student["roll"]+","+
                        student["name"]+","+
                        str(student["age"])+","+
                        student["branch"]+"\n"
                    )     
    if not found:
        print("Student not found!")
def delete_student():
    roll=input("enter Roll Number:").strip()
    if not roll:
        print("Please enter a roll number!")
        return
    if not roll.isdigit():
        print("Please enter a valid Roll Number!")
        return
    found=False
    for student in students:
        if student["roll"]==roll:
            confirm=input("Are you sure you want to delete? (yes/no):").strip().lower()
            if confirm=="yes":
                students.remove(student)
                found=True
                print("Student deleted successfully!")
            elif confirm=="no":
                print("Deleted cancelled!")
                found=True
                break
            else:
                print("Please enter yes or no!")
                found=True
                break
    if found:
        with open("students.txt", "w")as file:
            for student in students:
                file.write(
                        student["roll"] + "," +
                        student["name"] + "," +
                        student["age"] + "," +
                        student["branch"] + "\n"
                )
    if not found:
        print("Student not found!")
while True:
    print("==============================")
    print("STUDENT MANAGEMENT SYSTEM")
    print("==============================")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")
    choice=input("enter your choice:")
    if choice=="1":
        add_student()
    elif choice=="2":
        view_students()
    elif choice=="3":
        search_student()
    elif choice=="4":
        update_student()
    elif choice=="5":
        delete_student()
    elif choice=="6":
        print("Thank you!")
        break
    else:
        print("Invalid choice!")