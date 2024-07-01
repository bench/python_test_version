import math

def main():
    numbers = [2, 3, 4, 5]
    try:
        # Calculate the product of all numbers in the list
        product = math.prod(numbers)
        print(f"The product of {numbers} is {product}.")
    except AttributeError:
        print("math.prod() is not available in your Python version. It requires Python 3.8 or newer.")
