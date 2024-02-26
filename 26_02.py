def solveQuadrat(a, b, c):
    D = b**2-4*a*c
    if D>0:
        x1 = (-b+(D)**0.5) / (2*a)
        x2 = (-b-(D)**0.5) / (2*a)
    elif D==0:
        x1 = 0
        x2 = 0
    else: print("Es gibt keine Lösungen")
    return x1, x2


def solveLinear(a,b):
    if a==0 and b==0:
        print("0=0 hat unendlich viele Lösungen")
    elif a==0:
        print(f"{str(b)}=0 hat keine Lösung")
    else:
        x=-b/a
        if b<0:
            print(f"Die Lösung von {str(a)}x + {str(b)} = 0 ist {str(x)}")
        else: 
            print (f"Die Lösung von {str(a)}x + {str(b)} = 0 ist {str(x)}")




      
a=int(input("a="))
b=int(input("b="))
c=int(input("c="))

if a>0:
    x = solveQuadrat(a,b,c)
    print(f"Die Lösung von {a}x^2+{b}x+{c}=0 ist x1={str(x[0])} und x2={str(x[1])}")
elif b>0: 
    solveLinear(b,c)
    # print(f"Die Lösung von {b}x+{c}=0 ist {x}")






