# Part D: Intuitive Interface
from src.delivery_manager import *
import datetime

# Printing a divider line with the specified character and length
def print_divider(char='=', length=100):
    print(char * length)

# Displaying a banner-style message
def banner_message(message):
    print_divider('=')
    print(f"{message.center(100)}")
    print_divider('=')

# Converting time string in HH:MM:SS format to a timedelta object
def convert_time(time_str):
    hours, minutes, seconds = map(int, time_str.split(":"))
    return datetime.timedelta(hours=hours, minutes=minutes, seconds=seconds)

# Main function displaying the user interface and interact with the user
def user_interface():
    # Displaying the welcome banner
    banner_message("WGUPS Delivery Tracker")

    # Calculating and display the total distance traveled by all trucks
    total_distance = round(
        delivery_truck_1.distance_traveled + delivery_truck_2.distance_traveled + delivery_truck_3.distance_traveled, 1
    )
    print(f"\n🚚 Total Distance Traveled by All Trucks: {total_distance} miles")

    # Displaying summary of delivered packages by each truck
    print_divider('-')
    print(f"📦 {delivery_truck_1.truck_id} Delivered Packages: {delivery_truck_1.delivered}")
    print(f"📦 {delivery_truck_2.truck_id} Delivered Packages: {delivery_truck_2.delivered}")
    print(f"📦 {delivery_truck_3.truck_id} Delivered Packages: {delivery_truck_3.delivered}")
    print_divider('-')

    # Main loop presenting options and receive user input
    while True:
        # Displaying menu options
        print("\n✨ What would you like to do?")
        print(" (1)  STATUS OF SINGLE PACKAGE")
        print(" (2)  STATUS OF ALL PACKAGES")
        print(" (0)  EXIT OUT OF PROGRAM")

        # Prompting the user for an option and handle their input
        try:
            option = input("\n💡 Enter your choice (1, 2, or exit): ").strip().lower()

            # Option 0 or "exit" quits the program.
            if option == "exit" or option == "0":
                print("\n👋 Exiting... program closed.")
                break  # Exit the loop and terminate the program

            # Option 1: Check the status of a single package
            elif option == "1":
                check_single_package_status()

            # Option 2: Check the status of all packages at a given time
            elif option == "2":
                check_all_packages_status()

            # Handling invalid options
            else:
                print("❌ Invalid option. Please select 1, 2, or exit.")
        except ValueError:
            print("❌ Please enter a valid number.")  # Handling invalid inputs


# Function to check the status of a single package based on user input
def check_single_package_status():
    try:
        print_divider('~')
        time_input = input("⏰ Enter time (HH:MM:SS): ").strip()
        lookup_time = convert_time(time_input)
        package_id = int(input("📦 Enter the package ID: ").strip())
        package = package_table.lookup(package_id)

        if package:
            truck_id = package_to_truck.get(package_id, "Unknown")  # Lookup the truck ID in the dictionary
            print(f"🚚 Associated Truck Number: {truck_id}")
            print(package.packages_information(lookup_time))
        else:
            print(f"❌ No package found with ID {package_id}.")
    except (ValueError, AttributeError) as e:
        print(f"❌ Error: {e}. Please try again.")

# Function to display the status of all packages at a specific time
def check_all_packages_status():
    try:
        print_divider('~')
        time_input = input("⏰ Enter time (HH:MM:SS): ").strip()
        lookup_time = convert_time(time_input)
        print("\n📋 Package Statuses at the Given Time:")
        print_divider('-')

        for package_id in range(1, 41):
            package = package_table.lookup(package_id)
            if package:
                truck_id = package_to_truck.get(package_id, "Unknown")  # Lookup truck ID
                print(f"🚚 Associated Truck Number: {truck_id}")
                print(package.packages_information(lookup_time))
            else:
                print(f"❌ Package with ID {package_id} not found.")
    except ValueError as e:
        print(f"❌ Error: {e}. Please try again.")
