# Get all domains and print your aim
doamins=[x for x in input("Enter domains: ").split(",")]
aim=input("Enter the aim: ")
for i in doamins:
    if aim.lower()==i.lower():
        continue
    else:
        doamins.remove(i)
print(doamins)

# Enter domains: ML,AI,DS
# Enter the aim: AI
# ['AI']