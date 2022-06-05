def dayToMinutes(day):
    {'MO':0, 
    'TU': 1, 
    'WE': 2,
    'TH': 3,
    'FR': 4,
    'SA': 5,
    'SU': 6
    }[day]*24*60

def hhmmToMinutes(hhmm):
    hour, minute = map(int, hhmm.split(':'))
    return (hour*60+minute)

def parseEmployee(line):
    return line.split('=')

def parseShifts(shifts):
    return shifts.split(',')

def shiftInMinutes(shift):
    hours = shift[2:].split('-')
    return (
        dayToMinutes(shift[0:2]) + hhmmToMinutes(hours[0]),
        dayToMinutes(shift[0:2]) + hhmmToMinutes(hours[1])
            )