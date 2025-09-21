
class Vehicle:
    def __init__(self, vehicle_id, base_rate):
        self._vehicle_id = vehicle_id
        self._base_rate = base_rate

    def display_details(self):
        return f"Vehicle ID: {self._vehicle_id}, Base Rate: {self._base_rate}"
    
    def rental_charge(self):
        return 0.0
    
class Car(Vehicle):
    def __init__(self, vehicle_id, base_rate, num_seats):
        Vehicle.__init__(self,vehicle_id, base_rate)
        self._num_seats = num_seats

    def rental_charge(self):
        return self._base_rate * self._num_seats
    
    def display_details(self):
        return f"Car ID: {self._vehicle_id}, Base Rate: {self._base_rate}, Number of Seats: {self._num_seats}"
    
class Bike(Vehicle):
    def __init__(self, vehicle_id, base_rate, bike_type):
        Vehicle.__init__(self,vehicle_id, base_rate)
        self.bike_type = bike_type

    def rental_charge(self):
        return self. _base_rate * 0.5
    
    def display_details(self):
        return f"Bike ID: {self._vehicle_id}, Base Rate: {self._base_rate}, Bike Type: {self.bike_type}"
    
def calculate_rental(Vehicle):
    return Vehicle.rental_charge()

car1 = Car("C123", 100.0, 4)
bike1 = Bike("B456", 50.0, "Scooter")
print(car1.display_details())
print(f"Car Rental Charge: {calculate_rental(car1):.2f}")
print(bike1.display_details())
print(f"Bike Rental Charge: {calculate_rental(bike1):.2f}")