# 2. fahrenheit to centrigrade and kelvin
f=float(input("enter the fahrenheit: "))
ftoc=(f-32)*(5/9)
print(ftoc)
ftok=ftoc+273.15
print(ftok)

# 2.1
celisus=float(input("enter the celisus: "))
ctof=(celisus*1.8)+32
print("the celisus to fahrenheit %.2f" % (ctof))
k = celisus + 273.15
print("the celisus to kelvin",round(k,2))
