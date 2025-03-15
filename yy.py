def calculator(a: int, b: int, operation: str = 'add') -> int:
    # Perform the operation based on the value of the operation argument
    if operation == 'add':
        return a + b
    elif operation == 'sub':
        return a - b
    elif operation == 'mul':
        return a * b
    elif operation == 'div':
        # Handle division by zero error
        if b != 0:
            return a / b
        else:
            return "Error: Division by zero"
    else:
        return "Invalid operation"

# Example usage
result = calculator(10, 5, 'add')
print(result)  # Output: 15

result = calculator(10, 5, 'sub')
print(result)  # Output: 5

result = calculator(10, 5, 'mul')
print(result)  # Output: 50

result = calculator(10, 5, 'div')
print(result)  # Output: 2.0

result = calculator(10, 0, 'div')
print(result)  # Output: Error: Division by zero

result = calculator(10, 5)  # Default operation is 'add'
print(result)  # Output: 15



print("*************************************program 37***************************************")

print("""eate a method to accept a string like “inceptez technologies” and return the following values in multiple result types (capitalize, upper case,
 length of the string, number of words, ends with “s” or not, replace ‘e’ with ‘a’) for eg. the result should be like this.. 
 (Inceptez Technologies, INCEPTEZ TECHNOLOGIES, 21, 2, True,incaptaz tachnologias)""")

def analyze_string(input_string):
    # Capitalized version
    capitalized = input_string.title()

    # Uppercase version
    upper_case = input_string.upper()

    # Length of the string
    length = len(input_string)

    # Number of words
    word_count = len(input_string.split())

    # Check if the string ends with 's'
    ends_with_s = input_string.endswith('s')

    # Replace 'e' with 'a'
    replaced_string = input_string.replace('e', 'a')

    # Return all results in a tuple
    return (capitalized, upper_case, length, word_count, ends_with_s, replaced_string)


# Example usage
input_string = "inceptez technologies"
result = analyze_string(input_string)

# Print the results
print(result)


print("program 39")

# Lambda function for calculating amount - (amount * offer_percent)
lam = lambda amount, offer_percent: amount - (amount * offer_percent)

# Regular function that takes the lambda function as an argument
def promo(amount, offer_percent, offer_cap_limit, lam):
    if amount * offer_percent < offer_cap_limit:
        return lam(amount, offer_percent)  # Apply the lambda function
    else:
        return amount - offer_cap_limit  # Apply the cap limit

# Call the promo function with 1000, 0.10, 200 and the lambda function 'lam'
result = promo(1000, 0.10, 200, lam)
print(result)


print("program 40")

# Lambda function version of promo
promo_lambda = lambda amount, offer_percent, offer_cap_limit=0: amount - (amount * offer_percent) if (amount * offer_percent) < offer_cap_limit else amount - offer_cap_limit

# Testing the lambda function
print(promo_lambda(1000, 0.10, 200))  # Output should be 800, because 1000*0.10 = 100, and 100 is less than 200, so 1000 - 100 = 900
print(promo_lambda(1000, 0.10))  # Output should be 900, because the offer_cap_limit defaults to 0


print("program 41")

def calculator(a: int, b: int, operation: str = 'add') -> int:
    try:
        # Check if both a and b are integers, if not raise an exception
        if not isinstance(a, int) or not isinstance(b, int):
            raise Exception("Both arguments must be integers")

        # Perform the operation based on the value of the operation argument
        if operation == 'add':
            return a + b
        elif operation == 'sub':
            return a - b
        elif operation == 'mul':
            return a * b
        elif operation == 'div':
            # Handle division by zero error
            if b != 0:
                return a / b
            else:
                return "Error: Division by zero"
        else:
            return "Invalid operation"
    except Exception as e:
        # If exception is raised, attempt to cast the arguments to integers and call the function again
        print(f"Exception: {e}. Attempting type casting...")
        try:
            # Attempt to type cast and call the function again
            a = int(a)
            b = int(b)
            return calculator(a, b, operation)  # Recursively call with type casted values
        except ValueError:
            return "Error: Invalid value for conversion to integer."

# Example usage
result = calculator("10", 5, 'add')
print(result)  # Output: 15 (after type casting "10" to integer)

result = calculator(10, "5", 'sub')
print(result)  # Output: 5 (after type casting "5" to integer)

result = calculator(10, 5, 'mul')
print(result)  # Output: 50

result = calculator(10, 5, 'div')
print(result)  # Output: 2.0

result = calculator(10, 0, 'div')
print(result)  # Output: Error: Division by zero

result = calculator("10", "20", "add")  # Both arguments as strings, should be typecasted
print(result)  # Output: 30 (after type casting both "10" and "20" to integers)

print("program 42")


def promo(amount, offer_percent, offer_cap_limit=0):
    # Check if offer_percent is negative and raise an exception
    if offer_percent < 0:
        raise ValueError("Offer percent cannot be negative")

    if amount * offer_percent < offer_cap_limit:
        return amount - (amount * offer_percent)
    else:
        return amount - offer_cap_limit


def promo1(*amount):  # Arbitrary arguments
    if amount[1] < 0:
        raise ValueError("Offer percent cannot be negative")

    if amount[0] * amount[1] < amount[2]:
        return amount[0] - (amount[0] * amount[1])
    else:
        return amount[0] - amount[2]


def promo2(**amount_1):  # Arbitrary keyword arguments
    if amount_1['offer_percent'] < 0:
        raise ValueError("Offer percent cannot be negative")

    if amount_1['amount'] * amount_1['offer_percent'] < amount_1['offer_cap_limit']:
        return amount_1['amount'] - (amount_1['amount'] * amount_1['offer_percent'])
    else:
        return amount_1['amount'] - amount_1['offer_cap_limit']


# Test cases with exception handling
try:
    print(promo(1000, .10, 200))  # Normal case
    print(promo(1000, -.10, 200))  # This should raise an exception
except ValueError as e:
    print(e)

try:
    print(promo1(1000, .10, 200))  # Normal case
    print(promo1(1000, -.10, 200))  # This should raise an exception
except ValueError as e:
    print(e)

try:
    print(promo2(offer_percent=.10, offer_cap_limit=200, amount=1000))  # Normal case
    print(promo2(offer_percent=-.10, offer_cap_limit=200, amount=1000))  # This should raise an exception
except ValueError as e:
    print(e)


#dd