# Part C: Arnes Kapic - 012280583
from src.data_loader import load_packages, load_addresses, load_distances
from src.user_interface import *

# Loading package details into the hash table
load_packages("data/WGUPS_Package_File.csv")

# Loading address data into the array
load_addresses("data/WGUPS_Address_File.csv")

# Loading distance matrix data into a 2D array
load_distances("data/WGUPS_Distance_Table.csv")

# Calling delivery functions for each truck from delivery_manager.py module
execute_delivery(delivery_truck_1)
execute_delivery(delivery_truck_2)
execute_delivery(delivery_truck_3)

# Starting program's ui from user_interface.py module
user_interface()
