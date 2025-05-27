import datetime  # Importing datetime to handle time-based conditions

# Part B: Returning each corresponding component
# Creating package class for creating and managing packages
class Package:
    def __init__(self, package_id, delivery_address, delivery_city, delivery_state, delivery_zip_code, delivery_deadline
                 , delivery_weight, delivery_notes, truck_id=None):
        self.package_id = package_id  # Unique ID for the package
        self.delivery_address = delivery_address  # Delivery address
        self.delivery_city = delivery_city  # Delivery city
        self.delivery_state = delivery_state  # Delivery state
        self.delivery_zip_code = delivery_zip_code  # ZIP code for the delivery address
        self.delivery_deadline = delivery_deadline  # Delivery deadline time (e.g., "10:30 AM" or "EOD")
        self.delivery_weight = delivery_weight  # Package weight in kilograms
        self.delivery_notes = delivery_notes  # Any additional notes or delivery instructions
        self.truck_id = truck_id  # Associated truck ID
        self.departure_time = None  # Time when package left the hub
        self.delivered_time = None  # Time when package was delivered
        self.status = "at hub"  # Initial status of package

    # Method to get package status information based on the provided time
    def packages_information(self, user_time):
        # Check if the address update condition applies to Package #9
        if self.package_id == 9 and user_time >= datetime.timedelta(hours=10, minutes=20):
            self.delivery_address = "410 S State St"
            self.delivery_city = "Salt Lake City"
            self.delivery_zip_code = 84111

        # Determine the delivery status based on the current time
        if self.delivered_time and user_time >= self.delivered_time:
            status = f"Status: delivered\t Delivered Time: {self.delivered_time}"
        elif self.departure_time and self.delivered_time > user_time > self.departure_time:
            status = "Status: en route"
        else:
            status = "Status: at hub"

        # Return the formatted package details
        return (
            f"Package ID: {self.package_id}\t"
            f"Address: {self.delivery_address}\t City: {self.delivery_city}\t State: {self.delivery_state}\t"
            f"Zip Code: {self.delivery_zip_code}\t Deadline: {self.delivery_deadline}\t"
            f"Weight(kg): {self.delivery_weight}\t {status}\t Notes: {self.delivery_notes}"
        )
