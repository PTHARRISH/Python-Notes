# College Time Table
def time_table(given_time):
    time_period={"9.00":"C","10:00":"C++","11:00":"Break","11:15":"Python","12:15":"DSA"}
    for time_min,periods in time_period.items():
        hrs,minu=time_min.split(".")
        print(hrs,periods)
time_table("10:00")
