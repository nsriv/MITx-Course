"""
DebtPayment was created as part of MIT 6.00.1x by Nishant Srivastava
on June 22 10 43

Write a program to calculate the credit card balance after one year if a person only pays the minimum monthly payment
required by the credit card company each month.
The following variables contain values as described below:

balance - the outstanding balance on the credit card
annualInterestRate - annual interest rate as a decimal
monthlyPaymentRate - minimum monthly payment rate as a decimal

For each month, calculate statements on the monthly payment and remaining balance.
Finally, print out the total amount paid that year and the remaining balance at the end of the year.
The code you paste into the following box should not specify the values for the variables balance, annualInterestRate,
or monthlyPaymentRate - our test code will define those values before testing your submission.
"""

# Test Case 1:
balance = 42
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
# Result should be 31.38

# Test Case 2:
# balance = 484
# annualInterestRate = 0.2
# monthlyPaymentRate = 0.04
# Result should be 361.61

# Code for Part 1
month = 0
totalPayment = 0
monthlyInterestRate = annualInterestRate / 12.0
while month < 12:
    minPayment = monthlyPaymentRate * balance
    unpaidBalance = balance - minPayment
    totalPayment += minPayment
    balance = unpaidBalance + (monthlyInterestRate * unpaidBalance)
    month += 1
print(' Remaining balance: ' + str(round(balance, 2)))

#Code for Part 2
month = 0
totalPayment = 0
monthlyInterestRate = (annualInterestRate / 12.0)
while month < 12:
    minPayment = monthlyPaymentRate * balance
    unpaidBalance = balance - minPayment
    totalPayment += minPayment
    balance = unpaidBalance + (monthlyInterestRate * unpaidBalance)
    month += 1
    print('Month: ' + str(month))
    print('Minimum monthly payment: ' + str(round(minPayment, 2)))
    print('Remaining balance: ' + str(round(balance, 2)))
print('Total paid: ' + str(round(totalPayment, 2)))
print(' Remaining balance: ' + str(round(balance, 2)))
