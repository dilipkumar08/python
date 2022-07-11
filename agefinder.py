from datetime import date
import datetime as dt
d=int(input("Enter the day of birth:"))
m=int(input('Enter the month of birth as digits:'))
y=int(input('Enter the year of birth:'))
bd=dt.date(y,m,d)
print("your date of birth:"+bd.strftime('%d-%b-%Y'))
Today=date.today()
dif=Today-bd
age=int(dif.days/365)
print("Your age is :",age)
