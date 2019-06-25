def valor(x):
    x= str(x)
    l= str.__len__(x)
    v=','
    if l==1:
        print (x[0])
    elif l==2:
        print(x[0:2])
    elif l==3:
        print (x[0:3])
    elif l==4:
        msg= "mil"
        print(x[0],v,x[1:3],msg)
    elif l==5:
        msg= 'mil'
        print(x[0:2],v,x[2:4],msg)
    elif l==6:
        msg= "mil"
        print (x[0:3],v,x[1:3],msg)
    elif l==7:
        msg="milhões"
        print (x[0],v,x[1:3],msg)
    elif l==8:
        msg="milhões"
        print (x[0:2],v,x[1:3],msg)
    elif l==9:
        msg="milhões"
        print (x[0:3],v,x[2:4],msg)
    elif l==10:
        msg= "bilhão"
        print (x[0],v,x[1:3],msg)
    elif l==11:
        msg= "bilhões"
        print (x[0:2],v,x[1:3],msg)
    elif l==12:
        msg="bilhões"
        print(x[0:3],v,x[2:4],msg)

valor("INSIRA O VALOR AQUI")
    
