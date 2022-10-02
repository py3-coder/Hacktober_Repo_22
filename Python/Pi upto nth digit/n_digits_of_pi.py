
from math import factorial
from decimal import Decimal, getcontext


"""
    One of the possible errors is "" TypeError: 'module' object is not callable ""
    happens when Decimal is mispelled as decimal
    
    can be solved by 
    making a new identifier 'dec' and 
    assigned it the data type of Decimal module from the decimal library
    why it happens : 
    confusion about the Class name and Module name. 
    The problem is in the import line . 
    You are importing a module, not a class. 
    This happend because the module name and class name have the same name .
"""

getcontext().prec = 1000
#max possible digits = 1000

"""
    The decimal library uses the concept of a "context" to decide how much precision you really want.
    Since the more precision you want the slower the calculations will run. 
    The decimal.getcontext() part returns the default context.
"""

num = int(input("\nEnter the num of digits (0-999): "))

# refer the screenshot for the formula


def pi_d(n_d):

    numerator = Decimal(0)
    denominator = Decimal(0)
    result = Decimal(0)

    for k in range(n_d):

        numerator = ((-1) ** k) * ((factorial(6 * k))) * \
            (13591409 + 54510134 * k)

        denominator = factorial(3 * k) * ((factorial(k)) ** 3) * (640320 ** (3*k))

        result += Decimal(numerator) / Decimal(denominator)
        result *= 12 / Decimal((640320 ** 1.5))
        result = (result ** -1)

        return round(result, n_d)


final_result = pi_d(num)

print(f'Values of pi to the {num} decimal places is :\n\n   {final_result}\n')