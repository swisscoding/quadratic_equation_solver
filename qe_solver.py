#!/usr/local/bin/python3

import colored
from math import sqrt

print(colored.stylize("\n---- | Solve quadratic equations (ax² + bx + c = 0) | ----\n", colored.fg("red")))

a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
qe = colored.stylize(f"{a}x² + {b}x + {c} = 0", colored.fg("red"))
print(f"Quadratic equation to solve: {qe}")
discriminant = (b*b) - (4*a*c)

def xValues():
    global n1, n2, z, x1, x2
    n1 = -b + sqrt(discriminant)
    n2 = -b - sqrt(discriminant)
    z = 2*a
    x1 = n1/z
    x2 = n2/z
    if x1 > x2:
        x1_1 = x1
        x1 = x2
        x2 = x1_1

if a == 0:
    if b == 0:
        if c == 0:
            print("\nThis equation has infinity solutions.\n=> 0 = 0\n")
        else:
            print("\nThis equation hasn't any solution.\n")
    else:
        x = -c/b
        x = colored.stylize(x, colored.fg("red"))
        print(f"\nThis equation has one solution.\n=> {x}\n")
elif discriminant < 0:
    print("\nThis equation hasn't any solution.\n")
elif discriminant == 0:
    xValues()
    x1 = colored.stylize(x1, colored.fg("red"))
    print(f"\nThis equation has one solution.\n=> {x1}\n")
else:
    xValues()
    x1, x2 = colored.stylize(x1, colored.fg("red")), colored.stylize(x2, colored.fg("red"))
    print(f"\nThis equation has two solutions.\n=> x1 = {x1}, x2 = {x2}\n")
