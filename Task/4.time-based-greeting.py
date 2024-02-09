import datetime
# from datetime import datetime
time=datetime.datetime.now().hour
print(time)
if 5<=time and time<12:
    print("Good morning")
elif 12<=time and time<16:
    print("Good Afternoon")
elif 16<=time and time<21:
    print("Good evening")
else:
    print("Good Night")

# 22
# Good Night