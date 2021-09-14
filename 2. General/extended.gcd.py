
def extended_gcd(a, b):
    if(a == 0):
        return b,0,1

    gcd,x1,y1 = extended_gcd(b %a , a)
    x = y1 - (b//a) * x1
    y = x1

    return gcd,x,y


p = 26513
q = 32321
g, u, v = extended_gcd(p, q)

# ax + by = gcd(p,q)
print("Coefficients: crypto{%d,%d}" % (u, v))
print("Greatest Common Divisor: %d" % (g))