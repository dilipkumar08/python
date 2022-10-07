def leap_year(year):
    if year%4==0 and year%100!=0 or year%400==0:
        return "A leap year."
    else:
        return "Not a leap year."
if __name__=="__main__":
    input_year=int(input("Enter the year: "))
    print(leap_year(input_year))
    
