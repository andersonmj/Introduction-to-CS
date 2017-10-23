# Credit goes to Websten from forums and Udacity
# Use Prof. Dave's suggestions to finish your daysBetweenDates
# procedure. It will need to take into account leap years
# in addition to the correct number of days in each month.

def isLeapYear (year):
    if year %400==0:
        return True
    
    if year %100 == 0:
        return False
        
    if year %4 == 0:
        return True
    return False #I dont need to put an else because if the statements above are false, they just dont run and I end up here!
    

def daysInMonth (year, month):
    if month == 1 or month ==3 or month ==5 or month == 7 or month == 8 or month == 10 or month == 12:
        return 31
        
    else:
        if month == 2:
            if isLeapYear(year):
                return 29
            else:
                return 28
        else:
            return 30
   
def nextDay(year, month, day):
    """Simple version: assume every month has 30 days"""
    if day < daysInMonth (year, month):
        return year, month, day + 1
    else:
        if month == 12:
            return year + 1, 1, 1
        else:
            return year, month + 1, 1
        
def dateIsBefore(year1, month1, day1, year2, month2, day2):
    """Returns True if year1-month1-day1 is before year2-month2-day2. Otherwise, returns False."""
    if year1 < year2:
        return True
    if year1 == year2:
        if month1 < month2:
            return True
        if month1 == month2:
            return day1 < day2
    return False        

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    """Returns the number of days between year1/month1/day1
       and year2/month2/day2. Assumes inputs are valid dates
       in Gregorian calendar."""
    # program defensively! Add an assertion if the input is not valid!
    assert not dateIsBefore(year2, month2, day2, year1, month1, day1)
    days = 0
    while dateIsBefore(year1, month1, day1, year2, month2, day2):
        year1, month1, day1 = nextDay(year1, month1, day1)
        days += 1
    return days

def test ():
    print isLeapYear (2016)
    print isLeapYear(2013)
    assert daysBetweenDates(2010,1,2,2010,1,2) == 0
    assert daysBetweenDates (2010,1,2,2010,1,3) == 1
    assert nextDay (2010,4,30) == (2010,5,1)
    assert nextDay (2011,2,3) == (2011,2,4)
    assert nextDay (2010,2,28) == (2010,3,1)
    assert daysBetweenDates (2013,1,1,2014,1,1) == 365
    assert daysBetweenDates (2012,1,1,2013,1,1) == 366
    assert nextDay (2016,2,28) == (2016,2,29)
    print "Test done."
    
test ()
