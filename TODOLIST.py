def management():
    duty=[]
    print("=========WELCOME TO THE TO-DO LIST==========")
    number_of_duty=int(input("Enter the numbers of tasks you want to add in the TO-Do list : "))
    for i in range(1,number_of_duty+1):
        duty_name=input(f"Enter task {i} : ")
        duty.append(duty_name)
    for item in duty:
        print("Task you have to perform today are--> ",item)
    while True:
        print("""PRESS 1 if you want to add task 
PRESS 2 if you want to update task
PRESS 3 if you want to remove task
PRESS 4 if you want to exit """)
        choice=int(input("Enter your choice : "))
        
        if choice==1:
            insert=input("Enter the task you want to add : ")
            duty.append(insert)
            print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
            print(f"Task {insert} has been successfully added.....")
            print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")

        elif choice==2:
            updated_duty=input("Enter the task name you want to update = ")
            
            if updated_duty in duty:
                updated=input("Enter the new task : ")
                place=duty.index(updated_duty)
                duty[place]=updated
                print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                print("Task has been updated successfully")
                print(f"Updated task {updated}")
                print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")            
            
            else:
                print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")            
                print("OOPS!! Task not found")
                print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")    
        elif choice==3:
            deleted_duty=input("Enter the task which you want to delete : ")

            if deleted_duty in duty:
                ind=duty.index(deleted_duty)
                del duty[ind]
                print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")            
                print(f"Task {deleted_duty} has been deleted successfully.......")
                print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")            
            else:
                
                print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^") 
                print(f"The task {deleted_duty} does not exist in the list")
                print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")


        
        elif choice==4:
            for item in duty:
                print("Tasks for the day are--> ",item)
            

        elif choice==5:
            print("===========THANK YOU FOR USING TO-DO LIST ============")
            break
        
        else:

            print("PLEASE ENTER A VALID CHOICE!!!!!")

management()