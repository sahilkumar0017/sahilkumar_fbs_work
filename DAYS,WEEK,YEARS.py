days=int(input('enter number of days:'))
year=days//365
week=days//7
days=days%365
print('number of years is:',year)
print('number of weeks is:',week)
print('number of days is:',days)