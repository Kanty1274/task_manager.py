#=====importing libraries===========
import datetime
'''This is the section where you will import libraries'''
# Created an Empty dictionary for user information.
# Open 'user.txt' file.
# Splitting the string into keys and values from the comma using split() & strip function.

user_info = {}                                                                                                           
with open("user.txt") as file:                                                                                                 
    for lines in file:                                                                                                                                                  
        (key, val) = lines.strip().split(",")                                                                                
        user_info[str(key)]= val.strip()
print(user_info)

#===================== Log in========================#
# Checking to see if username is a key in the dictionary,if so, then ask for the user password.
# Password has to match the key-value pair.  

while True:
    
    username = input(" Please enter your username: ")
    if username in user_info.keys():                                                                                        
        password = input(" Please enter your password: ")                                                                          
        if password in user_info.values() and password == user_info[username]:                                            
            print("\n————————————————————————\n")
            break
    
# Presenting the menu to the user and making sure that the user input is converted to lower case.

while True:

    if username != "admin":
        menu = input('''Select one of the following Options below:
        a - Adding a task
        va - View all tasks
        vm - view my task
        e - Exit
        :''').lower()

# Presenting menu to the Admin.
    else:
        menu = input('''Select one of the following Options below:
        r - Registering a user
        a - Adding a task
        va - View all tasks
        vm - view my task
        ds_ display statistics
        e - Exit
        :''').lower()

# Admin to add a new username and password to user.txt  
    new_username =[]
    new_password =[]

    if menu == 'r' and username ==  "admin":
        n_username = input("Please enter your username:")
        n_password = input("Please enter your password:")
        confirm_password =input("confirm password:")

        if n_username ==confirm_password:
            new_username.append(n_username)
            new_password.append(n_password)

            with open("user.txt", "a")as file:
                file.write(f"\n{n_username}, {confirm_password} ") 

        if n_password == confirm_password:
            print("The password is correct")
        else:
            print("The password is incorrect, try again!")
            
# Admin to enter the details of tasks and add them to tasks.txt file 
    elif menu == 'a':
        assigned_to = input("Please enter the username of the person whom the task is assigned to: ")
        task = input("Please enter  a title of the task:  ")
        task_description = input ("Please enter the description of the task: ")
        today_date = datetime.datetime.today().strftime("%d/%m/%y")  # Getting current date using import.datime function.
        due_date = input("Please enter the due date of the task:")
        task_status  = input("Please indicate if the task has been completed or not ? ")

# Adding task to the tasks.txt file.
        file = open("tasks.txt","a")
        file.write(f"\n{assigned_to}, {task},{task_description}, {today_date}, {due_date},{task_status},\n")
        file.close

        print("task added successfully.")
        
    # using a for loop to read the file lines.
    elif menu == 'va':
        with open("tasks.txt","r" ,encoding= "utf-8") as file:

            for lines in file:
        
                data = lines.split(",")
                output = "————————————————————————\n"
                output += "\n"
                output += f"Assined to:\t\t{data[0]}\n"
                output += f"Task:\t\t\t{data[1]}\n"
                output += f"Description:\t\t{data[2]}\n"
                output += f"Assigned Date:\t\t{data[3]}\n"
                output += f"Due Date:\t\t{data[4]}\n"
                output += f"Task Status:\t\t{data[5]}\n"
                output += "\n"
                output += "————————————————————————\n"
                print(output)


# opening the task file, reading each line and checking if the username of the person logged in is the same as the username in the file.
    elif menu == 'vm':
        with open("tasks.txt","r" ,encoding= "utf-8") as file:

            for lines in file:
                data = lines.split(",")
                if username == data[0]:
                        
                    output = "————————————————————————\n"
                    output += "\n"
                    output += f"Assigned to:\t\t{data[0]}\n"
                    output += f"Task:\t\t\t{data[1]}\n"
                    output += f"Description:\t\t{data[2]}\n"
                    output += f"Assigned Date:\t\t{data[3]}\n"
                    output += f"Due Date:\t\t{data[4]}\n"
                    output += f"Task Status:\t\t{data[5]}\n"
                    output += "\n"
                    output += "————————————————————————\n"
    
                    print(output)


    elif menu == "ds" and username == "admin":
        
        # Declaring  variables tasks_num and nuser_num initializing values to 0 so that we can get the desired statistics
        tasks_num = 0
        users_num = 0

        with open("tasks.txt", "r") as task_file:
                for lines in task_file:
                    tasks_num += 1
                print (f"\nTotal number of tasks: {tasks_num}")

        with open("user.txt", "r") as username:
                for lines in username:
                    users_num += 1
                    print (f"Total number of users: {users_num}")               

    elif menu == 'e':
        print("Goodbye!!!")
        exit()

    else:
        print("You have made a wrong choice, Please Try again.")
