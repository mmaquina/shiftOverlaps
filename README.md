# shiftOverlaps
The goal of this exercise is to output a table containing pairs of employees and how often they have coincided in the office.

## Example (input is contained in a separate .txt file)
### INPUT (one line for each employee)
RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00- 21:00

ASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00

### OUTPUT
ASTRID-RENE: 2


## Process:
- Input data is converted to a more useful format: a list of tuples for each employee. Tuples are shifts composed of enter and exit time.
- Next, for each employee, every shift is compared with the working time of the other employees. 
- Finally, result is printed in standard output.

## Architecture
The solution is divided into three layers.

The first layer is responsible for reading the input file and parsing the data, to be stored locally in a list of employees. Employee is a class, which may be extended and used for other programs for the organization.

Furthermore, the next layer uses a method of Employee in order to find all overlaps.

Lastly, the final layer is responsifble for showing the result.

Every layer is lightly coupled to the next, in order for the program to be able to accomdate changes in an indiviudual layer without impact on the others. For example: instead of printing to standard output, an html file could be generated, which would not affect the previous 2 layers. Or the input file format could change, and that would require changes in the first layer only.

### Writen for Python 3.8.10
### Usage: 
$ python3 main.py input.txt

### To run tests: 
$ pytest-3