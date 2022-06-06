import sys

class Employee():

    def __init__(self, name, shifts):
        self.name = name
        self.shifts = shifts

    def __repr__(self):
        return f"Employee(name = {self.name}, shifts = {self.shifts}"

def dayToMinutes(day):
    return {'MO':0, 
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

def shiftToMinutes(shift):
    hours = shift[2:].split('-')
    return (
        dayToMinutes(shift[0:2]) + hhmmToMinutes(hours[0]),
        dayToMinutes(shift[0:2]) + hhmmToMinutes(hours[1])
            )

def parseMultipleShifts(multipleShifts):
    shiftsInMinutes = []
    for shift in parseShifts(multipleShifts):
        shiftsInMinutes.append(shiftToMinutes(shift))
    return shiftsInMinutes

employees=[]

if len(sys.argv)<2:
    print("Usage:\npython3 main.py input.txt")
    exit(-1)

with open(sys.argv[1]) as input_file:
    for line in input_file:
        name, rest = parseEmployee(line)
        employees.append(Employee(name, parseMultipleShifts(rest)))

    print (employees)
    input_file.close()

    