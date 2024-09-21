try :
    days = int(input("Enter number of days"))
except:
    days = 0
    print("Entered value is not a number")

years = days//365
months = (days%365)//30
days = (days%365)%30

print("Years: ",years,", Months: ",months,", Days: ",days)