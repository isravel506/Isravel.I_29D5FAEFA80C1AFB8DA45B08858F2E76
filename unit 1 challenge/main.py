def isleapyear(year):
  if(year%400==0):
    return True
  else:
    return False
year=int(input("Enter a Number:"))
if isleapyear(year):
  print("{} is not a leap year.".format(year))
else:
  print("{} is a leap year.".format(year))