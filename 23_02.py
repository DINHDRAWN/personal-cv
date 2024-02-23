a=int(input("a="))
b=int(input("b="))

#print(f'{3:x}')
if b==0 & a==0:
    print("Die Gleichung stimmt nicht")    
else: 
    x=float(-b/a)
    print("Die Lösung von "+str(a)+"x"+str(b)+"=0: x="+str(x))