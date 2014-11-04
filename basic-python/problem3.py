#! /usr/bin/python

balance=int(raw_input('Enter balance'))
annualInterestRate=float(raw_input('Enter ani'))
monthlyInterestRate = annualInterestRate / 12
lowerMonthlyPayment = balance / 12
upperMonthlyPayment = (balance * ((1 + monthlyInterestRate)**12)) / 12
minMonthlyPayment = (upperMonthlyPayment + lowerMonthlyPayment) / 2

for m in range(1,13):
    balance = (balance - minMonthlyPayment)*(1 + monthlyInterestRate)
    if balance >= 0.01:
        upperMonthlyPayment = minMonthlyPayment
    elif balance>=-0.01:
        lowerMonthlyPayment = minMonthlyPayment
    else:
	break	
    minMonthlyPayment= (upperMonthlyPayment + lowerMonthlyPayment) / 2 
      
print('Lowest Payment: %.2f ' % minMonthlyPayment)
