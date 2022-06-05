# shiftOverlaps
The goal of this exercise is to output a table containing pairs of employees and how often they have coincided in the office.

Example (input is contained in a separate .txt file)

*INPUT* 

RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00- 21:00
ASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00

*OUTPUT:*

ASTRID-RENE: 2


**Process:**
- Input data is converted to more useful format: a list of tuples for each employee. Tuples are shifts composed of enter and exit time.
- Next, for each employee, every shift is checked against the working time of the other employees. 
- Finally, propper output should be generated

