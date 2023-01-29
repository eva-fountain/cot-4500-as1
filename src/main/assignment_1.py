# Eva Fountain
# COT4500, Spring 2023
# Assignment 1

import math

# Number 1
given = "0100000001111110101110010000000000000000000000000000000000000000"

sign_bit = given[0]
exponent_bits = given[1:12]
fraction_bits = given[12:]

sign = int(sign_bit)

exponent = 0

for i in range(0,11):
    bit = int(exponent_bits[i])
    exponent += bit * 2**(10 - i)

exponent = exponent - 1023

fraction = 0

for i in range(0,52):
    bit = int(fraction_bits[i])
    fraction += bit * 0.5**(i + 1)

answer1 = ((-1)**sign) * (2**exponent) * (1 + fraction)
answer1print = round(answer1, 5)
print(answer1print)
print(" ")

# Number 2
given = "0100000001111110101110010000000000000000000000000000000000000000"

sign_bit = given[0]
exponent_bits = given[1:12]
fraction_bits = given[12:]

sign = int(sign_bit)

exponent = 0

for i in range(0,11):
    bit = int(exponent_bits[i])
    exponent += bit * 2**(10 - i)

exponent = exponent - 1023

fraction = 0

for i in range(0,52):
    bit = int(fraction_bits[i])
    fraction += bit * 0.5**(i + 1)

answer2 = ((-1)**sign) * (2**exponent) * (1 + fraction)

num_divisions = 0
while answer2 > 1:
    answer2 = answer2 / 10
    num_divisions += 1

answer2 = math.trunc(answer2 * 1000) / 1000
answer2 = answer2 * 10**num_divisions

print(answer2)
print(" ")

# Number 3
given = "0100000001111110101110010000000000000000000000000000000000000000"

sign_bit = given[0]
exponent_bits = given[1:12]
fraction_bits = given[12:]

sign = int(sign_bit)

exponent = 0

for i in range(0,11):
    bit = int(exponent_bits[i])
    exponent += bit * 2**(10 - i)

exponent = exponent - 1023

fraction = 0

for i in range(0,52):
    bit = int(fraction_bits[i])
    fraction += bit * 0.5**(i + 1)

answer3 = ((-1)**sign) * (2**exponent) * (1 + fraction)

num_divisions = 0
while answer3 > 1:
    answer3 = answer3 / 10
    num_divisions += 1

answer3 = round(answer3, 3)
answer3 = answer3 * 10**num_divisions

print(answer3)
print(" ")

# Number 4
abs_err = abs(answer1 - answer3)
print(abs_err)

rel_err = abs(answer1 - answer3) / abs(answer1)
print(rel_err)
print(" ")

# Number 5
min_err = 10**-4
n = min_err**(-1/3)
print(math.floor(n))
print(" ")

# Number 6
def f(x):
    return x**3 + (4 * (x**2)) - 10

def f_p(x):
    return (3 * (x**2)) + (8 * x)
tol = 10**-4
max_iterations = 100

# a) Bisection Method
right = 7
left = -4
iterations1 = 0

while abs(right - left) > tol and iterations1 < max_iterations:
    iterations1 += 1
    p = (left + right) / 2

    if((f(left) < 0 and f(p) > 0) or (f(left) > 0 and f(p) < 0)):
        right = p
    else:
        left = p

print(iterations1)
print(" ")

# b) Newton-Raphson Method
p = -4
iterations2 = 0

while(iterations2 < max_iterations):
    if(f_p(p) != 0):
        old_p = p
        p = old_p - (f(old_p) / f_p(old_p))
        iterations2 += 1
        if(abs(old_p - p) < tol):
            print(iterations2)
            break

    else:
        print("Derivative is zero")
        break

if(iterations2 == max_iterations):
    print("Max iterations performed")
