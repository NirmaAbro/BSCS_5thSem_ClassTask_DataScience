print('Roll No.22BSCS30')
print('lab4:loops')
print('Date:9th february 2023')

import numpy as np

a = float(input('a='))
b = float(input('b='))
c = float(input('c='))
D = (b**2-4*a*c)

if a ==0:
    print('No Solution')
elif D>0:
    print('The Roots are real and distict')
elif D==0:
    print('Roots are real and equal')
else:
    print('roots are complex or conjugates') 
    