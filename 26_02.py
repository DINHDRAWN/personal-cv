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

def solveQuadrat1(list):
    D = list[1]**2-4*list[0]*list[2]
    if D>0:
        x1 = (-list[1]+(D)**0.5) / (2*list[0])
        x2 = (-list[1]-(D)**0.5) / (2*list[0])
    elif D==0:
        x1 = 0
        x2 = 0
    else: print("Es gibt keine Lösungen")
    return list[x1,x2]


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




      
# a=int(input("a="))
# b=int(input("b="))
# c=int(input("c="))


print("Geben Sie Zahlen durch Enter")
meineListe = [i for i in int(input())]

if list[0]>0:
    x = solveQuadrat1(meineListe)
    print(f"Die Lösung von {a}x^2+{b}x+{c}=0 ist x1={str(x[0])} und x2={str(x[1])}")
elif list[1]>0: 
    solveLinear(b,c)
    # print(f"Die Lösung von {b}x+{c}=0 ist {x}")








