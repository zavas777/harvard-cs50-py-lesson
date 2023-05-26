class Point():

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

p = Point(1, 3, 7)

print("x: ", p.x)
print("y: ", p.y)
print("z: ", p.z)

class Flight():

    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []
    
    def get_open_seats(self):
        return self.capacity - len(self.passengers)

    def add_passenger(self, name):
        if self.get_open_seats() > 0: 
            self.passengers.append(name)
            return True
        
        print("The flight is already full")
        return False
    
people = ["Bruce", "Roy", "Rob", "Bob"]
flight = Flight(3)

for individual in people:
    if flight.add_passenger(individual):
        print(f"{individual} added to passengers")
    else:
         print(f"no seat left for {individual} on this flight")







