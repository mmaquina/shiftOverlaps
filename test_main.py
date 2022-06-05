import pytest
from main import parseEmployee, parseShifts, hhmmToMinutes

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


# @pytest.mark.parametrize(
#     "input, expected",
#     [
#     ( 'MO16:00-17:00', (0+16*60, 0+17*60) ), 
#     ( 'TU09:16-13:15', (24*60+9*60+16, 24*60+13*60+15) ), 
#     ( 'MO16:00-17:32', (16*60, 17*60+32) ),
#     ( 'TH09:10-13:01', (3*24*60+9*60, 3*24*60+13*60+1) ) 
#     ]
# )
# def test_toMinutes(input, expected):
#     assert toMinute(input) == expected

@pytest.mark.parametrize(
    "input, expected",
    [
    ( '16:00', 16*60 ),
    ( '09:16', 9*60+16),
    ( '13:15', 133*60+15) 
    ]
)
def test_hhmmToMinutes(input, expected):
    assert hhmmToMinutes(input) == expected
