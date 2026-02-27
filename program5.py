set1 = set()
set2 = set()
x=(int(input("enter the number of mebers ")))
for i in range(x):
    name=input("enter your name")
    if name not in set:
        set1.add(name)
    else:
        set2.add(name)

    a=len(set1)
    b=len(set2)
    print("accepted are:",set1)
    print("rejected are :",set2)
    print("CCEPTED NOS",a)
    print("rejected nos",b)