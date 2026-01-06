# Function to count the number of vowels in each string
def count_vowels(strings):
    vowels = 'aeiouAEIOU'
    vowel_counts = {}
    
    for string in strings:
        count = sum(1 for char in string if char in vowels)
        vowel_counts[string] = count
    
    return vowel_counts
# Add individual test cases to validate the function
# each case in a separate line, separet variable
test_case_1 = ["hello", "world", "python"]
test_case_2 = ["AI", "is", "awesome"]
test_case_3 = ["", "bcd", "xyz"]
# Running the function with test cases and printing results
print(count_vowels(test_case_1))  # Expected: {'hello': 2, 'world': 1, 'python': 1}
print(count_vowels(test_case_2))  # Expected: {'AI': 2, 'is': 1, 'awesome': 4}
print(count_vowels(test_case_3))  # Expected: {'': 0, 'bcd': 0, 'xyz': 0}
