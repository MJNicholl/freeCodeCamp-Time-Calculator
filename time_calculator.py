def add_time(start, duration, day_of_week = ""):

    day = "AM"
    night = "PM"
    week = ["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]

    start_time_list = start.split(" ")
    time_split = start_time_list[0].split(":")
    start_hour = int(time_split[0])
    start_minutes = int(time_split[1])
    day_time = start_time_list[1]

    split_duration = duration.split(":")
    duration_hour = int(split_duration[0])
    duration_minutes = int(split_duration[1])


    total_minutes = start_minutes + duration_minutes
    
    if(total_minutes > 59):
        duration_hour += int(total_minutes / 60)
        total_minutes = int(total_minutes % 60)

    extra_days = 0
    extra = 0 if (duration_hour / 24) < 0.5 else int(duration_hour / 24) +1
    remaining = duration_hour if extra < 1 else (24 - abs((duration_hour - (extra * 24))))

    total_hour = start_hour + remaining
    extra_days = extra if extra > 0 else 0

    # change day time
    if total_hour >= 12:
        day_time = night if day_time == day else day

        # passed from night to another day
        if day_time == day and extra_days == 0:
            extra_days = 1

        # formatation (12h)
        if total_hour > 12:
            total_hour -= 12


    # formatation (h?h:ss)
    if total_minutes < 10:
        total_minutes = "0" + str(total_minutes)


    # correct day of the week
    new_day_of_the_week = ""
    if day_of_week != "":
        future = week.index(day_of_week.lower()) + extra_days
        new_day_of_the_week = day_of_week if extra_days == 0 else week[future].title()


    # final composition
    final_minutes = total_minutes
    final_hour = total_hour
    final_day_time = day_time
    final_day_of_week = "" if day_of_week == "" else f", {new_day_of_the_week}"
    extra_days_text = ""
    if extra_days > 0:
        extra_days_text = " (next day)" if extra_days == 1 else f" ({extra_days} days later)"
    
    final_time = f"{final_hour}:{final_minutes} {final_day_time}{final_day_of_week}{extra_days_text}"
    print(final_time)

    return final_time

'''add_time("3:00 PM", "3:10")
print("Returns: 6:10 PM")

add_time("11:30 AM", "2:32", "Monday")
print("Returns: 2:02 PM, Monday")

add_time("11:43 AM", "00:20")
print("Returns: 12:03 PM")

add_time("10:10 PM", "3:30")
print("Returns: 1:40 AM (next day)")

add_time("11:43 PM", "24:20", "tueSday")
print("Returns: 12:03 AM, Thursday (2 days later)")

add_time("6:30 PM", "205:12")
print("Returns: 7:42 AM (9 days later)")'''
