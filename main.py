import sys
BEGIN = 0
END = 1

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

def doShiftsOverlap(shift1, shift2):
    if (shift1[BEGIN] > shift2[END]):
        return False
    elif (shift1[END] < shift2[BEGIN]):
        return False
    else:
        return True

employees=[]

if __name__ == '__main__':
    if len(sys.argv)<2:
        print("Usage:\npython3 main.py input.txt")
        exit(-1)

    with open(sys.argv[1]) as input_file:
        for line in input_file:
            name, rest = parseEmployee(line)
            employees.append(Employee(name, parseMultipleShifts(rest)))

        for i in range(len(employees) - 1):
            for j in range(i+1, len(employees)):
                count = [employees[i].name + '-' + employees[j].name, 0 ] 
                for shift1 in employees[i].shifts:
                    for shift2 in employees[j].shifts:
                        if doShiftsOverlap(shift1, shift2):
                            count[1] +=1 

                if count[1]>0:
                    print(f"{count[0]}: {count[1]}")

        input_file.close()

    