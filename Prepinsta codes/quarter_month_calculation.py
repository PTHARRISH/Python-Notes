def quarter_month(month):
    quarter=(month-1)//3+1
    print("Quarter: ",quarter)

month=int(input("Enter the month from 1 to 12: "))
if month>=1 and month<=12 :
    quarter_month(month)