import sys

class Employee():
    ''' TODO: could have an ID field to handle employees with same name '''

    def __init__(self, name, shifts):
        self.name = name
        self.shifts = shifts

    def __repr__(self):
        return f"Employee(name = {self.name}, shifts = {self.shifts}"

    def __do_shifts_overlap(self, shift1, shift2):
        if (shift1[0] > shift2[1]):
            return False
        elif (shift1[1] < shift2[0]):
            return False
        else:
            return True        

    def count_shift_overlaps_with(self, employee2):
        count = 0
        for shift1 in self.shifts:
            for shift2 in employee2.shifts:
                if self.__do_shifts_overlap(shift1, shift2):
                    count += 1 
        return count


def day_to_minutes(day):
    return {'MO':0, 
    'TU': 1, 
    'WE': 2,
    'TH': 3,
    'FR': 4,
    'SA': 5,
    'SU': 6
    }[day]*24*60

def hhmm_to_minutes(hhmm):
    hour, minute = map(int, hhmm.split(':'))
    return (hour*60+minute)

def parse_employee(line):
    return line.split('=')

def parse_shifts(shifts):
    return shifts.split(',')

def shift_to_minutes(shift):
    hours = shift[2:].split('-')
    return (
        day_to_minutes(shift[0:2]) + hhmm_to_minutes(hours[0]),
        day_to_minutes(shift[0:2]) + hhmm_to_minutes(hours[1])
            )

def parse_multiple_shifts(multiple_shifts):
    shifts_in_minutes = []
    for shift in parse_shifts(multiple_shifts):
        shifts_in_minutes.append(shift_to_minutes(shift))
    return shifts_in_minutes



employees=[]

if __name__ == '__main__':
    if len(sys.argv)<2:
        print("Usage:\npython3 main.py input.txt")
        exit(-1)

    with open(sys.argv[1]) as input_file:
        for line in input_file:
            name, shifts = parse_employee(line)
            employees.append(Employee(name, parse_multiple_shifts(shifts)))

        for i in range(len(employees) - 1):
            for j in range(i+1, len(employees)):
                count = employees[i].count_shift_overlaps_with(employees[j])
                if count:
                    print(f"{employees[i].name}-{employees[j].name}: {count}")

        input_file.close()

    