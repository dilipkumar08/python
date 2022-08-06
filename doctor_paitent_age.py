/'''Q1. A doctor has a clinic where he serves his patients. The doctor's consultation fees are
different for different groups of patients depending on their age. If the patient's age is below
17. The fee is 200 INR. If the patient's age is between 17 and 40, fees are 400 INR.
If the patient's age is above 40, fees are 300 INR. Write a code to calculate earnings in a day for
which one array/List of values representing age of patients visited on that day is passed as
input.
Note:
● Age should not be zero or less than zero or above 120.
● Doctors consult a maximum of 20 patients a day.
● Enter age value (press ENTER without value to stop):
Example 1:
Input
20
30
40
50
2
3
14
Output
Total income 2100 INR'''/
#code
age=[]
while True:
    try:
        if len(age)<20:
            x=int(input())
            if x>0 and x<120:
                age.append(x)
        else:
            print("No. of paitents reached its limit")
            break
    except:
        break
print(age)   
s=0
for i in age:
    if i<17:
        s+=200
    elif i in range(17,40):
        s+=400
    elif i in range(40,121):
        s+=300
print(s)
    
