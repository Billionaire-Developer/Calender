import calender

def display_calender():
    
    year = int(input("Enter year: "))
    month = int(input("Enter month (1-12): "))
    
    cal = calender.TextCalender(calender.SUNDAY)
    
    month_calender = cal.formatmonth(year, month)
    print(month_calender)
    
display_calender()