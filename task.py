while True:
    print("\n📃 To-Do list menu")
    print("1. ➕ add tasks")
    print("2. 👀 view tasks")
    print("3. 🗑️ Delete task")
    print("4. 🏃 exist")

    choice=input("entre your choice:")

    if choice == "1":
        add= input("entre your tasks:")
        with open("file.txt","a") as f:
            f.write(add+"\n")
            print("add task succesfull")

    elif choice == "2":
        try:
            with open("file.txt","r") as f:
                empty=True
                for line in f:
                    empty=False
                    print(line.strip())
                if empty:
                    print("no any records")
        except FileNotFoundError:
            print("❌ no such file found")

    elif choice=="3":
        try:
            with open("file.txt","r") as f :
                empty=True
                for i,line in enumerate(f,start=1):
                    empty=False
                    print(f"{i}.{line.strip()}")
                if empty:
                    print("no any task to delete")
                else:
                   num=int(input("entre task number to delete:"))
                   if num<1 or num>i:
                     print("invalide task number")
                   else:
                     with open("file.txt","r") as src,open("title.txt","w") as wrc:
                         for i,line in enumerate(src,start=1):
                             if i != num:
                                 wrc.write(line)
            import os
            os.remove("file.txt")
            os.rename("title.txt","file.txt")
            print("delete task succesfull")
        except FileNotFoundError:
            print("no task file found")
            
                    
    elif choice=="4":
        print("now you exixt----")
        print("thank you for using system💕")
        break

    else:
        print("❌ invalid no. please choose the the no. that show in the menu")