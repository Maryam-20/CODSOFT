# TASK 1 ---- TO-DO LIST
import datetime as dt  # Import datetime module
import sys   # Import sys module 

class TaskManager:
    def __init__(self, MyTasks, RecentTasks, Priority, DismissedTask):
        
        # MyTasks = []
        # RecentTasks = []
        # Important = []
        # DismissedTask = []
        
        # print(MyTasks)
        self.MyTasks = MyTasks
        self.RecentTasks = RecentTasks
        self.Priority = Priority
        self.DismissedTask = DismissedTask
        
        self.homepage()
    
    # Function that cater for the hompage/Landing page
    def homepage(self):
        
        print("Task Manager \n T -- My Task \n R -- Recent \n P -- Priority  \n D -- Dismissed \n NL -- New Category \n NT -- New Task")
        ManagerInput = input("Welcome Champ! What do you want to do today? \n")
        
        if ManagerInput.upper() == "T":
            self.AllTask()
        elif ManagerInput == "R":
            recent()
        elif ManagerInput.upper() == "P":
            self.priority()
        elif ManagerInput == "D":
            dismis()
        elif ManagerInput.upper() == "NL":
            self.newCategory()
        elif ManagerInput.upper() == "NT":
            self.newTask()
        else:
            print("Invalid operation!")
        
    
    # Function that create New Category/New Label
    def newCategory(self):
        global Task_CategoryName
        Task_CategoryName = input(" Enter the Task Category Name:\n ")
        createTask_input = input("Create a task? Yes or No : \n  ")
        if createTask_input.capitalize() == "Yes":
            self.createTask()
        elif createTask_input.capitalize() == "No":
            self.homepage()
        else:
            print("Invalid input!")
       
    
    # Function that create new task
    def createTask(self):
        num = 1
        createTask = True
        while createTask:
            TaskNum = num
            taskName = input("Task Name: \n")
            taskDescription = input("Task Description: \n ")
            
            print("When does this task due? \n ")
            dueDate = dt.date.today()
            hour = int(input("Enter the hour in digit: "))
            minute = int(input("Enter the minute in digtit: "))
            seconds  = int(input("Enter the seconds in digit: "))
            dueDateTime = dt.datetime(dueDate.year, dueDate.month, dueDate.day,  hour, minute, seconds)
            
            prioritize = input(" Prioritize the task: \n IU -- Important & Urgent \n INU -- Important but Not Urgent \n NI -- Not Important and not Urgent \n Input Here:  ")
            
            if prioritize.upper() == "IU":
                priorityValue = "Important and Urgent"
            elif prioritize.upper() == "INU":
                priorityValue = "Important but not Urgent"
            elif prioritize.upper() == "NIU":
                priorityValue = "Not Important and not urgent"
            else:
                print("Invalid Input")  
                
            dateCreated = dt.datetime.now()
            formatted_dateCreated = dateCreated.strftime("%Y-%m-%d %H:%M:%S")

            TaskDict = {"Task No": TaskNum, "Task Name": taskName, "Task Description": taskDescription, "Date Created" : formatted_dateCreated, "DueDateTime" : f"Task '{taskName}' is due on {dueDateTime}", "Priority": priorityValue}
            self.MyTasks[Task_CategoryName] = TaskDict
            
            continueTask = input("DO YOU WANT TO CREATE ANOTHER TASK? YES/NO? : \n")
            if continueTask.upper() != "YES":
                createTask = False
                self.homepage() 
            num += 1  
            print(self.MyTasks)    
        
    # Function that print out al task created
    def AllTask(self):
        print("All Task Created \n \n")
        
        for key1, val1 in self.MyTasks.items():
            print(f"Category {key1} has the following task assigned -- ")
            
            for key2 in val1:
                print(f"{key2} : {val1[key2]}")
                
        another_operation = input("Do you want perform another operation?  Yes/No \n")
        if another_operation.title() == "Yes":
            self.homepage()
        elif another_operation.title() == "No":
            sys.exit()
        else:
            print ("invalid operation")
           
    # Function that print out the order of priority of task
    def priority(self):
        priorityInput = input(" IU -- Important and Urgent \n INU -- Important but not Urgent \n NIU -- Not Important and not Urgent \n -- ")
        if priorityInput.upper() == "IU":
            self.impUrg()
        elif priorityInput.upper() == "INU":
            self.impNurg()
        elif priorityInput.upper() == "NIU":
            self.NimpNurg()
        else:
            print("Invalid Input")
                 
    #Function that print all important and Urgent task  
    def impUrg(self):
        for key1, val in self.MyTasks.items():
            for key2 in val:
                if key2 == "Priority" and val[key2] ==  "Important and Urgent":
                    return f"Category Name: {key1} \n Task Name: {val[key2]}"
                      
    #Function that print  all Important but not urgent task  
    def impNurg(self):
        for key1, val in self.MyTasks.items():
            for key2 in val:
                if key2 == "Priority" and val[key2] == "Important but not Urgent":
                    return f"Category Name: {key1} \n Tak Name: {val[key2]}"
                         
    #Function that print  Not all important and not urgent task  
    def NimpNurg(self):
        for key1, val in self.MyTasks.items():
            for key2 in val:
                if key2 == "Priority" and val[key2] == "Not Important and not urgent":
                    return f"Category Name: {key1} \n Tak Name: {val[key2]}"
            
            
    # Function to update a category with a new task directly from homepage
    def newTask(self):
        categoryName =  input("Enter Category name:  ")
        for key in self.MyTasks.keys():
            if categoryName in key:
                print(categoryName)
                self.createTask()
            else:
                print("CATEGORY NAME DOES NOT EXIST")
                categoryName_new = input("Would you like to create new category? YES/NO\n")
                if categoryName_new.upper() == "YES":
                    self.newCategory()
                elif categoryName_new.upper() == "NO":
                    self.homepage()
                else:
                    print("INVALID OPERATION!! ") 
              
   
myManager = TaskManager({}, [], [], [])
# myManager = TaskManager(MyTasks, RecentTasks, Important, DismissedTask)#MyTasks, RecentTasks, Important=)        