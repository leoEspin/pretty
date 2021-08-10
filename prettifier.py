from math import log10
from math import pow
import sys

def _format_it(n: float, powstr: str)-> str:
    if round(n, 1).is_integer():
        return f'{round(n, 1):0.0f}' + powstr
    return f'{round(n, 1):0.1f}' + powstr
    
def _pretty(x: float)-> str:
    exp = log10(x)
    if exp >= 6:
        if exp >= 12:
            return _format_it(x/pow(10,12), 'T')
        elif exp >= 9:
            return _format_it(x/pow(10,9), 'B')
        else:
            return _format_it(x/pow(10,6), 'M')
    else:
        return _format_it(x, '')
    
def pretty(z: float)-> str:
    try:
        x = float(z)
        return _pretty(x)
    except ValueError:
        print("Input must be a valid number.")
        return None

