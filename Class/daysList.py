from attr.setters import convert

d =[1250,273871,3325]


days =  lambda convert: (convert//365)
months = lambda convert: (convert%365)//30
years = lambda convert : (convert%365)%30

for i in d:
    print("Input Days : ",i,", Years: ",years(i),", Months: ",months(i),", Days: ",days(i))