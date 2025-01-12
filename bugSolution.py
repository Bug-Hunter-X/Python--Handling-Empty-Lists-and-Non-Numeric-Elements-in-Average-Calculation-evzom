def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list case
    numeric_numbers = [num for num in numbers if isinstance(num, (int, float))]
    if not numeric_numbers:
        return 0  # Handle case where all elements are non-numeric
    return sum(numeric_numbers) / len(numeric_numbers)

# Example usage with potential error:
my_list = [1, 2, 3, 'a']
average = calculate_average(my_list)
print(f"The average is: {average}")

my_list = []
average = calculate_average(my_list)
print(f"The average is: {average}")

my_list = ['a', 'b', 'c']
average = calculate_average(my_list)
print(f"The average is: {average}") 