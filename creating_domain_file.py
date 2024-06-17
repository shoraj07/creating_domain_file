import random
import string
import os
import csv

# Path for the output file
output_file_path = os.path.join("domain_file", "domain_files.txt")

# Function to generate a random alphanumeric string of length 8
def generate_random_string(length):
    letters_and_digits = string.ascii_lowercase + string.digits
    return ''.join(random.choice(letters_and_digits) for _ in range(length))

# Load elements from the CSV file
def load_elements_from_csv(csv_file_path):
    elements1 = []
    elements2 = []
    elements4 = []
    elements7 = []
    with open(csv_file_path, mode='r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            elements1.append(row['first_element'].strip())
            elements2.append(row['second_element'].strip())
            elements4.append(row['fourth_element'].strip())
            elements7.append(row['seventh_element'].strip())
    # Filter out empty strings
    elements1 = [element for element in elements1 if element]
    elements2 = [element for element in elements2 if element]
    elements4 = [element for element in elements4 if element]
    elements7 = [element for element in elements7 if element]
    return elements1, elements2, elements4, elements7

# Path to the input CSV file
csv_file_path = 'input/extracted_columns.csv'

# Load elements from the CSV file
elements1, elements2, elements4, elements7 = load_elements_from_csv(csv_file_path)

# Debugging prints to check loaded elements
print("Elements for first position:", elements1)
print("Elements for second position:", elements2)
print("Elements for fourth position:", elements4)
print("Elements for seventh position:", elements7)

# Function to generate a single entry
def generate_entry():
    # Generate random elements
    # element1 = generate_random_string(8)
    element1 = random.choice(elements1)
    element2 = random.choice(elements2)
    element3 = random.randint(1, 100)  # Random value
    element4 = random.choice(elements4)
    element5 = random.randint(1, 100)  # Random value
    element6 = random.randint(1, 100)  # Random value
    element7 = random.choice(elements7)
    element8 = random.randint(1, 100)  # Random value

    # Return the formatted entry
    return f"{element1}/{element2}/{element3}/{element4}/{element5}/{element6}/{element7}/{element8}/"

# Generate 40,000 entries and write them to the output file
with open(output_file_path, "w") as file:
    for _ in range(50000):
        entry = generate_entry()
        file.write(entry + "\n")

print("Entries have been written to", output_file_path)
