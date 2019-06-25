def resumir(x):
    b= str.__len__(x)
    c= x[0:140]
    if b > 140:
        print (c+"...")
        return c
    else:
        print (x)
resumir("INSIRA O TEXTO AQUI")
