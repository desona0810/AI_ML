
    
# Fix syntax errors and handle negative inputs
# Function to calculate factorial of a number
def factorial(n):
    if n < 0:
        return "Error: Factorial is not defined for negative numbers."
    elif n == 0:
        return 1
    else:
        return n * factorial(n - 1)
# Add individual test cases to validate the function
test_case_1 = 5
test_case_2 = 0 
test_case_3 = -3
# Running the function with test cases and printing results
print(factorial(test_case_1))  # Expected: 120
print(factorial(test_case_2))  # Expected: 1    
print(factorial(test_case_3))  # Expected: "Error: Factorial is not defined for negative numbers."= 0

