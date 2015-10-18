""" If i leave my house at 6:52 AM and run 1 Mile at an easy pace (8:15 per mile) then three miles
at tempo (7:12 per mile) and one mile at easy pace again: What time do i get home for breakfast ?
"""


# we will be using the dateTime function in python
# for doing that we need to import the function first

import datetime

# the format for dateTime is like this
# Year,Month,Day,Hour,Minute,Second,microsecond
# We will be supplying a dummy date and just print the time in this example


beforeTime = datetime.datetime(2015, 1, 1, 6, 52, 00)

# Finding seconds for both the runs
easyPace = 2 * ((8 * 60) + 15)
tempo = (7 * 60) + 12

AfterTime = beforeTime + datetime.timedelta(seconds=(easyPace + tempo))
print(AfterTime.time())
