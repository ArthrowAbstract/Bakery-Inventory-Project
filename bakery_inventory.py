import pickle
import os



#Creation Of Inventory
def create_rec_inv():
    f=open("inventory.dat","wb")
    ftxt=open("number.txt","w")
    ftxt.write('0')
    ftxt.close()
    ino=0
    while True:
        d={}
        ino+=1
        l=[]
        name=input("Enter Item's Name: ")
        l.append(name)
        phno=float(input("Item Index Number: "))
        l.append(phno)
        add=input("Item's Price: ")
        recipe = {}
        recipe_step_num = int(input("Number of steps to make the item",))
        for i in range(1,recipe_step_num+1):
            step = input("Enter Step"+str(i))
            recipe[i] = step
        l.append(recipe)
        d[ino]=l
        print(d)
        pickle.dump(d,f)
        ch=input("do you want to enter more records(y/n): ")
        if not ch=='y' or ch=='Y':
            break
    f.close()
    ftxt=open("number.txt","w")
    ftxt.write(str(ino))
    ftxt.close()



#Adding Entries to inventory
def append_rec_inv():
    f=open("inventory.dat","ab")
    ftxt=open("number.txt","r+")
    ino=int(ftxt.read())
    
    while True:
        d={}
        ino+=1
        l=[]
        name=input("Enter Item's Name: ")
        l.append(name)
        phno=input("Item Index Number: ")
        l.append(phno)
        add=input("Item's Price: ")
        recipe = {}
        recipe_step_num = int(input("Number of steps to make the item",))
        for i in range(1,recipe_step_num+1):
            step = input("Enter Step"+str(i))
            recipe[i] = step
        l.append(recipe)
        d[ino]=l
        print(d)
        pickle.dump(d,f)
        ch=input("do you want to enter more records(y/n): ")
        if not ch=='y' or ch=='Y':
            break
    f.close()
    ftxt.seek(0)
    ftxt.write(str(ino))
    ftxt.close()





#Display All Records
def display_all_rec():
    f=open("inventory.dat","rb")
    try:
        while True:
            d=pickle.load(f)
            a=list(d.keys())
            print("The item number is{}, item name is {}, item Index no is {}, recipe is {}"\
                  .format(a[0],d[a[0]][0],d[a[0]][1],d[a[0]][2]))
            
    except EOFError:pass
    finally:f.close()


#Deleting through Key Number
def delete_ino_rec():
    f1=open("inventory.dat","rb")
    f2=open("temp.dat","wb")
    ino=int(input("enter inventory no to delete"))
    flag=0
    try:
        while True:
            d=pickle.load(f1)
            if ino in d:
                flag=1
                del d[ino]
                print("record deleted")
            else:
                pickle.dump(d,f2)
    except EOFError:
        if flag==0: print("sorry inventory to delete was not there")
    finally:
        f1.close()
        f2.close()




#Delete through Name Search
def delete_name_rec():
    f1=open("inventory.dat","rb")
    f2=open("temp.dat","wb")
    nm=input("enter name to be delete")
    flag=0
    try:
        while True:
            d=pickle.load(f1)
            for i in d:
                x_name,y_phno,z_add=d[i]
                if x_name.lower()==nm.lower():
                    flag=1
                else:
                    pickle.dump(d,f2)
    except EOFError:
        if flag==0: 
            print("sorry name to delete was not there")
        else:
            print("deleted record")
    finally:
        f1.close()
        f2.close()
    os.remove("inventory.dat")
    os.rename("temp.dat","inventory.dat")


#Modify the name of a Record
def modify_name_rec():
    f1=open("inventory.dat","rb")
    f2=open("temp.dat","wb")
    adm=int(input("enter inventory no to search: "))
    nm=input("enter name to be changed: ")
    flag=0
    try:
        while True:
            d=pickle.load(f1)
            if adm in d:
                d[adm][0]=nm 
                flag=1
                pickle.dump(d,f2)
            else:
                    pickle.dump(d,f2)
            print(d)
    except EOFError:
        if flag==0: print("sorry ino whose name had to be changed \
        was not there")
    finally:
        f1.close()
        f2.close()
    os.remove("inventory.dat")
    os.rename("temp.dat","inventory.dat")



#Search Record
def search_rec():
    if not os.path.isfile("inventory.dat"):   
        #checking whether file exists or not
        print("sorry file not found")
    else:
        f=open("inventory.dat","rb")
        ph=input("enter item Index no")
        flag=0
        try:
            while True:
                d=pickle.load(f)
                for i in d:
                    if d[i][1]==ph:
                        flag=1
                        print("ino is",i)
                        print("The item name is %s and item Index no is %s"%\
                              (d[i][0],d[i][1]))
                
        except EOFError:
            if flag==0:
                print("sorry phone no not found n the database")
        finally:f.close()




#Search Recipe Using The Item Index
def search_recipe():
    if not os.path.isfile("inventory.dat"):   
        print("sorry file not found")
    else:
        f=open("inventory.dat","rb")
        ph=float(input("enter item Index no"))
        flag=0
        try:
            while True:
                d=pickle.load(f)
                for i in d:
                    if ph==d[i][1]:
                        flag=1
                        print("ino is",i)
                        print("The item name is %s and item Index no is %s"%\
                              (d[i][0],d[i][1]))
                        a = list(d.values())
                        stepsx =a[0][0]
                        stepsy = a[0][2]
                        print(str(stepsx) + str(" - ") + str("Intructions for Making"))
                        for key, value in stepsy.items():
                            print(key ,' : ', value)
                
        except EOFError:
            if flag==0:
                print("sorry item no not found n the database")
        finally:f.close()




#Main Menu
def main():
    while True:
        print(" 1.Create\n 2.Append\n 3.Display\n 4. Delete by Inventory Number\n\
 5. Delete by name\n 6. Modify name\n 7. search by Item no\n 8. Get Recipe\n\
 9. Exit")
        ch=input("enter ur choice")
        if ch=='1':
            create_rec_inv()
        elif ch=='2':
            append_rec_inv()
        elif ch=='3':
            display_all_rec()
        elif ch=='4':delete_ino_rec()
        elif ch=='5':delete_name_rec()
        elif ch=='6':modify_name_rec()
        elif ch=='7':search_rec()
        elif ch=='8':search_recipe()
        elif ch=='9':break
        else:
            print("invalid choice")
main()
