# College Time Table
def time_table(current_time):
    time_period={"9.00":"C","10:00":"C++","11:00":"Break","11:15":"Python","12:15":"DSA"}
    curent_hrs,current_min=map(int,current_time.split("."))
    for start_time,subject in time_period.items():
        start_hrs,start_min=map(int,start_time.split("."))
        if start_hrs<curent_hrs or (start_hrs==curent_hrs)and start_min<=current_min:
            end_hrs=start_hrs+1
            if start_min==0 :
                pass
            else:
                pass

time_table("10:00")
