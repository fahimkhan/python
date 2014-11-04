#! /usr/bin/python


    #Test Case 1:
balance = 320000
annualInterestRate = 0.2
     
    #copy from here
monIntRate = annualInterestRate / 12 # Monthly interest rate
lowBound = balance / 12 #low
hiBound = (balance * (1 + monIntRate)**12) / 12 #high
minMonPayment = (hiBound + lowBound) / 2.0 #ans
epsilon = 0.01
numGuesses = 0
finalBalance = balance #x
     
while abs(finalBalance) >= epsilon: # while finalBalance gets closer to 0
        month = 1 # month start
        newBalance = balance # Asing original balance
        numGuesses += 1 # number of guesses, print if you want to control
        while month <= 12: # while 12 months
            newBalance = newBalance - minMonPayment # balance minus payment for every month
            monInterest = newBalance * monIntRate # get Month Interest amount
            newBalance += monInterest # balance plus interest for every month
            month += 1 # one month has pass
        finalBalance = newBalance # asing the balance after 12 months to finalBalance
        if finalBalance > 0: # check if finalBalance stills big
            lowBound = minMonPayment # then re-asings lowBound
        else:
            hiBound = minMonPayment # else re-asings hiBound
        minMonPayment = (hiBound + lowBound) / 2.0 # re- define minMonPayment or #ans
print ('Lowest Payment: ' + str(round(minMonPayment, 2))) # print rounding

