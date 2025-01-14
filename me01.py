l1=[]
c=1
while c==1:
    print("1.Add an element at end")
    print("2.Remove an element from end")
    print("3.clear all")
    print("4.Insert an element in between")
    print("5.Remove an element in between")
    ch=int(input('enter your choice'))
    if ch==1:
        e=int(input("enter the element"))
        l1.append(e)
        print("list after adding the element")
        print(l1)

    elif ch==2:
        l1.pop()
        print("list after removing element")
        print(l1)
        
    elif ch==3:
        l1.clear()
        print("list after clear all elements")
        print(l1)
       
    elif ch==4:
        i1=int(input("enter index"))
        e1=int(input("enter element"))
        l1.insert(i1,e1)
        print("list after inserting element")
        print(l1)
        
    elif ch==5:
        i2=int(input("enter index"))
        del l1[i2]
        print("list after removing element")
        print(l1)
       
    elif ch<0 or ch>5:
        print("enter valid choice")
       

    c=int(input("Do you want to continue 1.yes 2.No"))
        
    
              
    


