P=500000
r=8
n=24
def EMI(P,r,n):
   r_mon=r/(12*100)
   emi=P*r_mon*((1+r_mon)**n)/(((1+r_mon)**n)-1)
   return emi
value=EMI(P,r,n)
print("EMI for 24 months:",value)