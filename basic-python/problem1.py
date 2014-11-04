#! /usr/bin/python


balance = 4213
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
total_paid=0.0
monthlyInterestRate = annualInterestRate/12

for month in range(1, 13):
	minimum_monthly_payment=round(monthlyPaymentRate*balance,2)
	balance=round((balance-minimum_monthly_payment)*(1+monthlyInterestRate),2)
	total_paid+=round(minimum_monthly_payment,2)
	print('Month:'+ ' '+str(month))
	print('Minimum monthly payment:'+' '+str(minimum_monthly_payment))
	print('Remaining Balance:'+' '+str(balance))

print('Total Paid:'+' '+str(total_paid))
print('Remaining Balance:'+' '+str(balance))
