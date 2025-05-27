# Part C: Program that uses the attached supporting documents
import csv
from src.package_model import Package
from src.hash_table import HashTable

# Initializing the hash table and data lists
package_table = HashTable()
distance_matrix = []
address_list = []

# Function to load packages from a CSV file into the hash table
def load_packages(csv_file_path):
    with open(csv_file_path) as file:
        reader = csv.reader(file, delimiter=",")
        # Iterating through the CSV rows and insert packages into the hash table.
        for record in reader:
            package_id = int(record[0])
            destination = record[1]
            city = record[2]
            state = record[3]
            postal_code = int(record[4])
            delivery_deadline = record[5]
            package_weight = int(record[6])
            special_notes = record[7]

            # Adding the package into the hash table with ID as the key.
            package_table.add(
                package_id,
                Package(package_id, destination, city, state, postal_code,
                        delivery_deadline, package_weight, special_notes)
            )

# Function to load distances from a CSV file into the distance matrix.
def load_distances(csv_file_path):
    with open(csv_file_path) as file:
        reader = csv.reader(file, delimiter=",")
        # Add each row to the distance matrix.
        for record in reader:
            distance_matrix.append(record)

        # Filling the missing values to complete the symmetric distance matrix.
        for i in range(len(distance_matrix)):
            for j in range(len(distance_matrix[i])):
                distance_matrix[i][j] = distance_matrix[j][i]

# Function to load addresses from a CSV file into the address list.
def load_addresses(csv_file_path):
    with open(csv_file_path) as file:
        reader = csv.reader(file, delimiter=",")
        # Extracting only the address from each row and store it in the address list.
        for record in reader:
            address_list.append(record[2])  # Extracting the address field
