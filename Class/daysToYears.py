days = int(input("Enter number of days"))

years = days//365
months = (days%365)//30
days = (days%365)%30

print("Years: ",years,"Months: ",months,"Days: ",days)