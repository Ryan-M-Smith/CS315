#
# Filename: multiply.py | Homework 1
# Description: Implement multiplication without the * operator.
# Created: 2025-08-31
#

def multiply(a: int, b: int) -> int:
    """ Multiplies two integers using bitwise operations. """
    
    result = 0
    
    while b > 0:
        result += a if b & 1 else 0
        a <<= 1
        b >>= 1
    
    return result

def multiply_recursive(a: int, b: int) -> int:
    """
    Recursive implementation of multiplication using bitwise operations.
    
    ---
    
    ### Question 3
    
    In my testing, I was able to use extremely large integers without any issues.
    Python has a max recursion depth of `1000` by default, which evidently I wasn't able to
    hit with the large integers I was using. I was able to multiply numbers as large as 14 digits,
    and even then I couldn't hit the recursion limit. This is likely because the number of recursive
    calls in my solution is proportional to the number of bits in `b`, which grows logarithmically

    With a more traditional solution that affectively adds `a` to itself `b` times, I would be
    able to hit the max recursion depth with much smaller integers. This makes sense, because
    the number of recursive calls would be equal to `b` in that case. Any number larger than around
    1000 (or whatever the Python recursion depth is user-configured to) will result in a RecursionError.
    This shows that recursive algorithm efficiency decreases significantly when the input size is large
    or when many recursive calls are needed to solve the problem.
    """
    
    if b > 0:
        add = a if b & 1 else 0
        return add + multiply_recursive(a << 1, b >> 1)
    else:
        return 0

def main():
    """ The main function. """
    
    a = int(input("Enter the first integer: "))
    b = int(input("Enter the second integer: "))
    
    product = multiply_recursive(a, b)
    print(f"{a} * {b} = {product}.")

if __name__ == "__main__":
    import sys
    sys.exit(main())
