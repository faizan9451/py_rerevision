# WAP of factorial number

value = int(input("Enter you factorial"))
copy = value
cout = 1
print(copy)
while cout<copy:
    copy = copy -1
    copy  *=copy
    
    print(copy)