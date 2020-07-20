def ggT(a,b):
    x = a
    y = b
    steps = []
    print("Weg zum ggT(" + str(a) + ", "  + str(b) + ")")
    while y != 0:
        print(str(x) + ' = ' + str(x//y) + " * " + str(y) +  " + " + str(x % y) )
        steps.append([x, (x//y), y, x%y])
        r = x % y
        x = y
        y = r
    print(("~> ggT(" + str(a) + "," + str(b) + ") = " + str(x)))
    ggt = x
    backwards = [x for x in steps[::-1] if x[0] > steps[-1][0]]
    print("Gleichungen nach dem Rest umgestellt:")
    for x in backwards:
        print(str(x[-1]) + " = " + str(x[0]) + " " + str(x[1] * -1) + " * " + str(x[2]))
    # Weil ich zu faul bin umd das programmatisch zu machen
    print("Substitution bitte selbst machen")
    print("Lineare Kombination (zur Kontrolle):")
    gcd, mul1, mul2 = extended_euclid(a,b)
    if(mul2 > -1):
        mul2 = "+ " + str(mul2)
    print(str(gcd) + " = " + str(mul1) + " * " + str(a) + " " + str(mul2) + " * " + str(b))
    
# Gestohlen von https://www.inf.hs-flensburg.de/lang/krypto/algo/euklid.htm  
def extended_euclid(a,b):
    u,v,s,t = 1,0,0,1
    while b!=0:
        q = a//b
        a,b = b, a-q*b
        u,s = s, u-q*s
        v,t = t, v-q*t
    return a,u,v
    
