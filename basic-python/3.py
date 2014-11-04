#! /usr/bin/python

balance=int(raw_input('Enter Balance:'))
annualInterestRate=float(raw_input('Enter ani:'))
#z=bis(balance, annualInterestRate)
#print(z)
def bis(balance, annualInterestRate):
    MR=annualInterestRate/12
    LP=balance/12
    UP=balance*((1+MR)**12)/12
    NB=balance
    while abs(UP-LP)>.01:
        half=(UP+LP)/2.0
	#NB=balance
	print(NB)
      
        for month in range(1,13):
            NB=(NB-half)*(1+MR)
        if NB>.01:
            UP=half
        if NB<-.01:
            LP=half
           
    return(round(half,2))

z=bis(balance, annualInterestRate)
print(z)
