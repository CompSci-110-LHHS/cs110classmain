####### Python Working With Date and Time ############

#Python uses several modules to work with date and
#time programmatically. 

################ EXAMPLE 1 - Start ##################
############### UNCOMMENT BELOW TO RUN ############## 

# import datetime
# current = datetime.datetime.now()
# print(current)


################ EXAMPLE 1 - END ##################

################ EXAMPLE 2 - Start ##################
############### UNCOMMENT BELOW TO RUN ##############

# import datetime
# current = datetime.datetime.now()
# dateString = current.strftime("%A, %B %d, %Y") # DAYofWEEK, MONTH DAY, YEAR 
# print(f"{dateString} looks a lot nicer than {current}")

#Datetime Formatting Strings 

# %a	Weekday, short version	Wed	
# %A	Weekday, full version	Wednesday	
# %w	Weekday as a number 0-6, 0 is Sunday	3	
# %d	Day of month 01-31	31	
# %b	Month name, short version	Dec	
# %B	Month name, full version	December	
# %m	Month as a number 01-12	12	
# %y	Year, short version, without century	18	
# %Y	Year, full version	2018	
# %H	Hour 00-23	17	
# %I	Hour 00-12	05	   
# %p	AM/PM	PM	
# %M	Minute 00-59	41	
# %S	Second 00-59	08	
# %f	Microsecond 000000-999999	548513	
# %z	UTC offset	+0100	
# %Z	Timezone	CST	
# %j	Day number of year 001-366	365	
# %U	Week number of year, Sunday as the first day of week, 00-53	52	
# %W	Week number of year, Monday as the first day of week, 00-53	52	
# %c	Local version of date and time	Mon Dec 31 17:41:00 2018	
# %C	Century	20	
# %x	Local version of date	12/31/18	
# %X	Local version of time	17:41:00	
# %G	ISO 8601 year	2018	
# %u	ISO 8601 weekday (1-7)	1	
# %V	ISO 8601 weeknumber (01-53)	01

################ EXAMPLE 2 - End ##################

################ EXAMPLE 3 - Start ##################
############### UNCOMMENT BELOW TO RUN ##############

# import datetime

# currentDate = datetime.datetime.today()
# lastClassDay = datetime.datetime(2024, 6, 25)
# daysRemaining = lastClassDay - currentDate
# print(f"{daysRemaining.days} until summer break!")

################ EXAMPLE 3 - End ##################

################ EXAMPLE 4 - Start ##################
############### UNCOMMENT BELOW TO RUN ##############
# import datetime

# currentDate = datetime.datetime.today()
# futureDate = currentDate + datetime.timedelta(days = 7)
# print(f"{futureDate.strftime('%A, %B %d')}")
################ EXAMPLE 3 - End ##################

################ EXAMPLE 5 - Start ##################
############### UNCOMMENT BELOW TO RUN ##############

# import datetime, time
# while True:
#     current = datetime.datetime.now()
#     Time = current.strftime("%I:%M:%S %p")
#     print(f"{Time}")
#     time.sleep(1)

################ EXAMPLE 5 - END ##################
    
################ EXAMPLE 6 - Start ##################
############### UNCOMMENT BELOW TO RUN ##############

# import datetime, time

# while True:
#     currentDate = datetime.datetime.now()
#     lastClassDay = datetime.datetime(2024, 6, 25)
#     timeRemaining = lastClassDay - currentDate
#     print(f"{timeRemaining.total_seconds()} until summer break!")
#     time.sleep(1)
    
################ EXAMPLE 6 - END ##################
    
################ EXAMPLE 6 - Start ##################
############### UNCOMMENT BELOW TO RUN ##############

import datetime, time
from tkinter import *

def getCount():
    currentDate = datetime.datetime.now()
    lastClassDay = datetime.datetime(2024, 6, 25)
    timeRemaining = lastClassDay - currentDate
    print(f"{timeRemaining.total_seconds()} until summer break!")    

root =Tk()
root.minsize(width=300, height=150)
clockTime = StringVar()
clockTime.set("HERE IS MY CLOCK")
mainFrame = Frame(root)
mainFrame.pack()
clock = Label(mainFrame, textvariable=clockTime, anchor="center")
clock.pack()

root.mainloop()


    
################ EXAMPLE 6 - END ##################