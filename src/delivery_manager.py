# Part C: Program that will deliver all packages
import datetime

from src.data_loader import address_list, distance_matrix, package_table
from src.truck_model import Truck

# Defining and initializing truck instances with assigned packages and departure times
# Truck 1 (8:00 a.m. Departure)
delivery_truck_1 = Truck(
    [1, 13, 14, 15, 16, 19, 20, 29, 30, 31, 34, 37, 40],
    datetime.timedelta(hours=8, minutes=0), "Truck 1"
)

# Truck 2 (9:05 a.m. Departure)
delivery_truck_2 = Truck(
    [3, 6, 18, 25, 28, 32, 36, 38, 7, 8, 5, 22, 23, 24, 26],
    datetime.timedelta(hours=9, minutes=5), "Truck 2"
)

# Truck 3 (10:20 a.m. Departure)
delivery_truck_3 = Truck(
    [2, 4, 9, 10, 11, 12, 17, 21, 27, 33, 35, 39],
    datetime.timedelta(hours=10, minutes=20), "Truck 3"
)

# Defining what truck goes with the package id
package_to_truck = {
    **{package_id: "Truck 1" for package_id in delivery_truck_1.not_delivered},
    **{package_id: "Truck 2" for package_id in delivery_truck_2.not_delivered},
    **{package_id: "Truck 3" for package_id in delivery_truck_3.not_delivered},
}

# Printing a divider line with a specified character and length
def print_divider(char='=', length=100):
    print(char * length)

# Finding the index of an address in the address list
def find_address_index(address):
    return address_list.index(address)

# Calculating the distance between two addresses from the distance matrix
def calculate_distance(addr1, addr2):
    return float(distance_matrix[find_address_index(addr1)][find_address_index(addr2)])

# Finding the nearest package's index and distance from the truck's current location
def find_nearest_package(truck):
    distances = []

    # Looping through all undelivered packages on the truck
    for package_id in truck.not_delivered:
        # Looking up the package in the hash table and get the distance
        package = package_table.lookup(package_id)
        distance = calculate_distance(truck.current_address, package.delivery_address)
        distances.append(float(distance))

    # Finding the minimum distance and its index
    min_distance = min(distances)
    min_index = distances.index(min_distance)

    return min_index, min_distance

# Nearest Neighbor Algorithm to deliver all packages on a truck
def execute_delivery(truck):
    # Setting packages as "en route" when the truck departs
    for package_id in truck.not_delivered:
        package = package_table.lookup(package_id)
        package.status = "en route"
        package.departure_time = truck.departure_timestamp

    truck.current_timestamp = truck.departure_timestamp

    # Delivering packages until all are delivered
    while truck.not_delivered:
        # Finding the nearest package's index and distance
        nearest_index, nearest_distance = find_nearest_package(truck)
        nearest_package = package_table.lookup(truck.not_delivered[nearest_index])

        # Updating truck's current location and mileage
        truck.current_address = nearest_package.delivery_address
        truck.distance_traveled += nearest_distance
        truck.current_timestamp += datetime.timedelta(hours=nearest_distance / truck.miles_per_hour)

        # Marking the package as delivered
        nearest_package.status = "delivered"
        nearest_package.delivered_time = truck.current_timestamp

        # Moving the package to the delivered list
        truck.delivered.append(truck.not_delivered.pop(nearest_index))

    # Calculating the distance from the last delivery back to the hub
    last_package = package_table.lookup(truck.delivered[-1])
    return_distance = calculate_distance(last_package.delivery_address, truck.end_address)

    # Updating truck's mileage and timestamp for the return trip
    truck.distance_traveled += return_distance
    truck.distance_traveled = round(truck.distance_traveled, 1)
    truck.current_timestamp += datetime.timedelta(hours=return_distance / truck.miles_per_hour)

    # Printing a summary of the truck's journey
    print_divider('-')
    summary_text = f"📊 Summary for {truck.truck_id}"
    print(summary_text.center(100))
    print_divider('-')
    print(f"🚚 Departure Time: {truck.departure_timestamp}")
    print(f"🏠 Return Time: {truck.current_timestamp}")
    print(f"🛣️ Total Distance Traveled: {truck.distance_traveled} miles")
    print_divider('=')
