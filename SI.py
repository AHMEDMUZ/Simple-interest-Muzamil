# Calcution of SI

#input
p=float(input ("what is the principal amount ?"))
R=float(input("what is the rate of intrest?"))
t=float(input("what is the tenure ?"))
#r=(R/100)
#x=(1+(rd))**n

        
#processing
#emi=p*rd*(x/(x-1))
#amt = p*(1+(r*t))
amt=p*t*R/100



#output
print("the total amount to be paid is " ,amt)
