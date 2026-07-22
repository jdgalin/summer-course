def interest(P,r,t=10,n=1):
    return P*(1+r/n)**(n*t)

A1=interest(1000,.0061)
A2=interest(1000,.031)
A3=interest(1000,.07)

print(f'{A1:.02f}\n{A2:.02f}\n{A3:.02f}')