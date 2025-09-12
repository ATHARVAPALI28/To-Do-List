#to-do-list:

def add():
    try:
        task=input("Enter your task:").strip()
        with open("tasks.txt","a") as x:
            x.write(task+"\n")
        print("✅ Task Added!")
    except(Exception):
        print("⚠️ Unable to Add Task! ⚠")

def view():
    try:
        x=open("tasks.txt","r")
        y=[task.strip() for task in x.readlines() if task.strip()]
        if not y:   
            print("⚠️ No Tasks Found! ⚠️")
        else:
            print("📋 Your Tasks:")
            for i,task in enumerate(y,start=1):
                print(f"{i}.{task}")
    except(Exception):
        print("Got Error!")

def delete():
    try:
        x=open("tasks.txt","r")
        y=[task.strip() for task in x.readlines() if task.strip()]
        if not y:   
            print("⚠️ No Tasks Found! ⚠️")
        else:
            print("📋 Your Tasks:")
            for i,task in enumerate(y,start=1):
                print(f"{i}.{task}")

        n=int(input("Enter task number to delete:"))
        if(1<=n<=len(y)):
            remove=y.pop(n-1)
            x=open("tasks.txt","w")
            for task in y:
                x.write(task+"\n")
            print("🗑 Task Deleted!")
        else:
            print("⚠️ Invalid Task Number ⚠️")
    except(Exception):
        print("Got Error!")
        
def start():
    try:
        print("[📝 TO-DO-LIST 📝]")
        print("1. ➕ Add Task\n2. 📋 View Task\n3. 🗑 Delete Task\n4. 🚪 Exit\n")

        while(True):
            choice=input("Enter your choice:")

            if(choice=='1'):
                add()
            elif(choice=='2'):
                view()
            elif(choice=='3'):
                delete()
            elif(choice=='4'):
                print("[🚪 EXITING 🚪]")
                break
            else:
                print("[⚠️ INVALID CHOICE ⚠️]")
                continue
    except(Exception):
        print("Got Error!")

start()
