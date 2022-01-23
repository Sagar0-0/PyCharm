try:
    rows=int(input("Enter no. of rows: "))
    i=int(input("Enter design:\n1. Ascending\n2. Descending\n"))
    ascending=True
    if i==1:
        ascending=True
    elif i==2:
        ascending=False
    else:
        print("Invalid input!!\nDefault pattern is Ascending")

    if ascending:
        row=1
        while(row!=rows+1):
            print(row *"*")
            row+=1
    else:
        row=rows
        while(row!=0):
            print(row *"*")
            row-=1
except Exception as e:
    print("Invalid input!!")