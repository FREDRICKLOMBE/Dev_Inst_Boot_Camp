# Daily Challenge: Advanced Algorithm
# Find and print each unique pair of numbers that adds up to the target.

import random  # Provides the function for generating random numbers.

# Step 1: Create a list of 20,000 random integers between 0 and 10,000.
list_of_numbers = [random.randint(0, 10000) for _ in range(20000)]

target_number = 3728  # The sum we want each pair to have.


# Step 2: Define a function that finds the matching pairs.
def find_pairs(numbers, target):
    seen_numbers = set()  # Stores numbers from earlier in the list.
    found_pairs = set()   # Stores unique pairs without duplicates.

    # Step 3: Go through the numbers one at a time.
    for number in numbers:
        missing_number = target - number  # Calculate the needed partner.

        # Step 4: Check whether the partner appeared earlier in the list.
        if missing_number in seen_numbers:

            # Put the smaller number first so reversed pairs count as duplicates.
            # Convert to a tuple because tuples can be stored in a set.
            pair = tuple(sorted([number, missing_number]))
            found_pairs.add(pair)  # Save the pair if it is not already stored.

        # Step 5: Remember this number for the next iterations.
        # Adding it after the check prevents using the same occurrence twice.
        # For example, 1864 + 1864 requires two occurrences of 1864.
        seen_numbers.add(number)

    # Step 6: Sort the matching pairs and print each one.
    for first_number, second_number in sorted(found_pairs):
        print(f"{first_number} and {second_number} sum to {target}")


# Step 7: Run the function using the generated list and target.
find_pairs(list_of_numbers, target_number)
