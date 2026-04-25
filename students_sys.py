import mysql.connector

con = mysql.connector.connect(
    host ="localhost",
    user="root",
    password="Malar1420@",
    database="student_mgmt_system"
)
print("sql-python connection successful")
cursor = con.cursor()
while True:
    #add students
    print("1 - for add students")
    print("\n 2 - for view students")
    print("\n 3 - for delete studets")
    print("\n 4 - for update students")
    print("\n 5 - for search students")
    print("\n 6 - for exit student system")


    sub_choice = input("Enter your choice: ")
    if sub_choice == "1":

        id = int(input("Enter student id: "))
        name = input("Enter student name: ")
        marks=int(input("Enter student marks: "))

        query ="insert into student_info (id,name,marks) values (%s,%s,%s)"
        values = (id,name,marks)

        cursor.execute(query,values)
        con.commit()

        print("\nstudents addded succesfully")
    elif sub_choice == "2":
        #view students
        cursor.execute("select * from student_info")
        for row in cursor.fetchall():
            print(row)
        print("\nstudents data viewed succesfully")
    elif sub_choice == "3":
        del_id=int(input("Enter student id you want to delete: "))
        cursor.execute("select * from student_info where id=%s",(del_id,))
        if  not  cursor.fetchone():
            print("student id doesn't exist")
            continue

        query = "delete from student_info where id=%s"
        values=(del_id,)
        cursor.execute(query,values)
        con.commit()
        print("\nstudents data deleted succesfully for that id")
    elif sub_choice == "4":
        id=int(input("Enter student id you want to update: "))
        cursor.execute("select * from student_info where id=%s",(id,))
        if  not  cursor.fetchone():
            print("student id doesn't exist")
            continue
        print("\n 1 - id updation")
        print("\n 2 - name updation")
        print("\n 3 - marks updation")
        update_choice = input("\nEnter your choice: ")
        if update_choice == "1":
            new_id = int(input("\nEnter new student id: "))
            query ="update student_info set id = %s where id = %s"
            values = (new_id,id)

        elif update_choice == "2":
            new_name = input("\nEnter new student name: ")
            query ="update student_info set name =%s  where id = %s "
            values = (new_name, id)


        elif update_choice == "3":
            new_marks = int(input("\nEnter new student mark: "))
            query ="update student_info set marks = %s where id = %s "
            values = (new_marks,id)

        else:
            print("Invalid choice")
            continue
        cursor.execute(query,values)
        con.commit()
        print("\nstudents data updated succesfully")
    elif sub_choice == "5":
        id = int(input("Enter student id you want to view: "))
        cursor.execute("select * from student_info where id =%s ",(id,) )
        search_result = cursor.fetchone()
        if not search_result:
            print("student id doesn't exist")
        else:
            print(search_result)




    elif sub_choice == "6":
        print("\nyou are exited from the student system")
        break
    else:
        print("\ninvalid selection")


cursor.close()
con.close()