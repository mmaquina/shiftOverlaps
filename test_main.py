import pytest
from main import parseEmployee, parseShifts, hhmmToMinutes, shiftToMinutes, dayToMinutes, doShiftsOverlap

@pytest.mark.parametrize(
    "input, expected, rest",
    [
    ('CHET=MO16:00-17:00,TU09:00-13:00', 'CHET', 'MO16:00-17:00,TU09:00-13:00'),
    ('BAKER=MO16:00-17:00,TU09:00-13:00', 'BAKER', 'MO16:00-17:00,TU09:00-13:00'),
    ]
)
def test_parseEmployee_gets_employee(input, expected, rest):
    assert parseEmployee(input) == [expected, rest]

@pytest.mark.parametrize(
    "input, expected",
    [
    ('MO16:00-17:00,TU09:00-13:00',  ['MO16:00-17:00', 'TU09:00-13:00']),
    ('MO16:00-17:00,TU09:00-13:00',  ['MO16:00-17:00', 'TU09:00-13:00']),
    ]
)
def test_parseShifts(input, expected):
    assert parseShifts(input) == expected


@pytest.mark.parametrize(
    "input, expected",
    [
    ( 'MO16:00-17:00', (0+16*60, 0+17*60) ), 
    ( 'TU09:16- 13:15', (24*60+9*60+16, 24*60+13*60+15) ), 
    ( 'MO16:00-17:32', (16*60, 17*60+32) ),
    ( 'TH09:10 -13:01', (3*24*60+9*60+10, 3*24*60+13*60+1) ) 
    ]
)
def test_shiftToMinutes(input, expected):
    assert shiftToMinutes(input) == expected

@pytest.mark.parametrize(
    "input, expected",
    [
    ( '16:00', 16*60 ),
    ( '09:16', 9*60+16),
    ( '13:15', 13*60+15),
    ( '00:00', 0) 
    ]
)
def test_hhmmToMinutes(input, expected):
    assert hhmmToMinutes(input) == expected

@pytest.mark.parametrize(
    "input, expected",
    [
    ( 'MO', 0*60*24),
    ( 'TH', 3*60*24),
    ( 'SU', 6*60*24) 
    ]
)
def test_dayToMinutes(input, expected):
    assert dayToMinutes(input) == expected

@pytest.mark.parametrize(
    "shift1, shift2, expected",
    [
    ((1234, 3456), (2345, 4567), True),
    ((2346, 3456), (2345, 4567), True),
    ((1234, 3456), (3456, 4567), True),
    ((1234, 3456), (1235, 3455), True),
    ((12, 60), (2345, 4567), False),
    ((2345, 4567), (12, 60), False)
    ]
)
def test_doShiftsOverlap(shift1, shift2, expected):
    assert doShiftsOverlap(shift1, shift2) == expected