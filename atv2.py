def leia():
    x= str(input('Insira um número:'))
    l= str.__len__(x)
    if l==1:
        print (x[0])
    elif l==2:
        print(x[0:2])
    elif l==3:
        print (x[0:3])
    elif l>4 and l<=6:
        msg= "mil"
        v= ','
        print (x[0],v,x[1:3],msg)
    elif l>=7 and l<=9 and x[0]=="1":
        v= ','
        msg="milhão"
        print (x[0],v,x[1:3],msg)
    elif l>=7 and l<=9 and x[0] !="1":
        v= ','
        msg= "milhões"
        print (x[0],v,x[1:3],msg)
    elif l>=10 and l<=12 and x[0] == "1":
        v= ','
        msg= "bilhão"
        print (x[0],v,x[1:3],msg)
    elif l>=10 and l<=12 and x[0]!= "1":
        v= ','
        msg= "bilhões"
        print (x[0],v,x[1:3],msg)
        
leia()
    
