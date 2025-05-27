# Part C: Creating truck class for creating truck objects for implementing delivery program
class Truck:
    def __init__(self, packages, departure_timestamp, truck_id):
        # Identifiers for the truck
        self.truck_id = truck_id
        self.maximum = 16
        self.miles_per_hour = 18

        # Addresses the truck will operate from
        self.start_address = "4001 South 700 East"
        self.current_address = self.start_address
        self.end_address = "4001 South 700 East"

        # Tracking the distance and packages during the journey
        self.distance_traveled = 0.0
        self.not_delivered = packages
        self.delivered = []

        # Timestamps to manage the delivery schedule
        self.departure_timestamp = departure_timestamp
        self.current_timestamp = departure_timestamp
        self.return_timestamp = None

        # Log to store timestamps with cumulative mileage
        self.distance_log = []
