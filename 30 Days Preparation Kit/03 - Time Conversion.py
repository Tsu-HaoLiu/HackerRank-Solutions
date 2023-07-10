# https://www.hackerrank.com/challenges/one-month-preparation-kit-time-conversion/problem

def timeConversion(s):
    
    time_parts = s.split(':')
    hour = int(time_parts[0])
    minute = int(time_parts[1])
    second = int(time_parts[2][:2])

    period = time_parts[2][2:].upper()
    if period == 'PM' and hour != 12:
        hour += 12
    elif period == 'AM' and hour == 12:
        hour = 0

    return "{:02d}:{:02d}:{:02d}".format(hour, minute, second)
