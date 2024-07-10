from datetime import datetime as dt
def daysBetweenDates( date1, date2):
    """
    :type date1: str
    :type date2: str
    :rtype: int
    """
    date1, date2= list(map(int,date1.split('-'))), list(map(int,date2.split('-')))
    m = dt(date1[0], date1[1], date1[2])
    n = dt(date2[0], date2[1], date2[2])
    return abs((n - m).days)

date1 = "2019-06-29"
date2 = "2019-06-30"
print(daysBetweenDates(date1,date2))
