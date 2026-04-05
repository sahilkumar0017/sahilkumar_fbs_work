principal=int(input('enter principal amount:'))
rate=int(input('enter rate: '))
time=int(input('enter time: '))
amount=principal*(1+rate/100)**time
compound_interest=amount-principal
print('compound interest is:',compound_interest)