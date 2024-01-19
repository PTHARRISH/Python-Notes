def age_state(age,state):
    if age>=18 and age <=60 and state in ["TN","KL","KR"]:
        return True
    else:
        return False

age=int(input("enter the age of the person: "))
state=input("Enter the state: ").upper()
mydict={"TAMILNADU":"TN","KERALA":"KL","KARNATAKA":"KR"}
print(age_state(age,mydict[state]))