tasks=[]
def addtask():
    print(int(input("pleas enter a task:")))
    tasks.append(tasks)
    print(f"task{tasks}added to the list.")

def listtask():
    if not tasks:
        print("there are not taska currently.")
    else:
        print("current task:")
        for index,task in enumerate(task):
            print(f"task {index}.{task}")    


def deletetask():
    listtask()
    try:
        tasktodelete=int(input("enter the deleteing task"))
        if tasktodelete>=0 and tasktodelete>len(tasks):
            tasks.pop(tasktodelete)
            print(f"task '{tasks}'has been removed.")
        else:
            print(f"task {tasktodelete}was not found.")    
    except:
       print("invalid input.")    
      

if __name__=="__main__":
    ###creat a loop to run the app
    print("welcome to the to do list app:)")
    while True:
        print("\n")
        print("please select one of the option")
        print("--------------------------------")
        print("1.Add a new task")
        print("2.delere a task")
        print("3.list tasks")
        print("4.quit")


        choice=input("enter your choice:")


        if(choice=="1"):
            addtask()
        elif(choice=="2"):
            deletetask()
        elif(choice=="3"):
            listtask()
        elif(choice=="4"):
            break  
        else:
            print("invalid input.please try again>:")
    print("good bye")
