"""Counting Sundays"""

def leap_year(year):
    """Return True if `year` is leap year"""
    return year%400==0 if year%100==0 else year%4==0
#   return not year%400 if not year%100 else not year%4

weeks = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday',
'Sunday']
months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
date0 = [1900, 1, 1]
date  = [2014, 4, 11]

def days_from_origin(date):
    delta = [i-j for i, j in zip(date, date0)]
    days = sum(months[:delta[1]]) + delta[2]
    # Took me hours to repair this bug!!
#   days = days + (1 if leap_year(date[0]) and delta[1]>=3 else 0)
    days = days + (1 if leap_year(date[0]) and delta[1]>=2 else 0)
    for year in range(date0[0], date[0]):
        days += 365 + leap_year(year)
    return days
#   day = days % 7
#   print weeks[day]

count = 0
for i in xrange(1901, 2001):
    for j in xrange(1, 13):
        if days_from_origin([i, j, 1]) % 7 == 6:
            count += 1
print count
