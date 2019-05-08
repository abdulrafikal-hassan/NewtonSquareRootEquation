""" Creating a newton square root function
    thst will be accepting 2 args: the number to find the square root
    from and the number of times that the program has to iterate
    to find the square root.
"""
def newtonSqrt(n, howmany):
    approx = 0.5 * n
    for i in range(howmany):
        betterapprox = 0.5 * (approx + n/ approx)
        approx = betterapprox
    return betterapprox

print(newtonSqrt(9,3))
print(newtonSqrt(10,5))
print(newtonSqrt(25,5))