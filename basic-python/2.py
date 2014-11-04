#! /usr/bin/python

balance = int(raw_input('Enter balance'))
annualInterestRate = .2
payment = 0
TempBalance = balance
while TempBalance > 0:
    payment += 10
    TempBalance = balance
    for month in range (1,13):
        TempBalance = (TempBalance - payment) * (1+(annualInterestRate/12))
	print(TempBalance)
        if TempBalance <= 0:
		print str('Lowest Payment: ' + str(round(payment,2)))
		break
