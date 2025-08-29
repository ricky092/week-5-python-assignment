# A simple class representing a smartphone with attributes and methods
class Smartphone:
    def __init__(self, brand, model, battery_life):
        self.brand = brand            # Brand of the phone (e.g., Apple, Samsung)
        self.model = model            # Model name (e.g., iPhone 13)
        self.battery_life = battery_life  # Battery life in hours
    
    def make_call(self, number):
        print(f"Calling {number} from {self.brand} {self.model}...")
    
    def charge(self):
        print(f"Charging the {self.brand} {self.model}...")



    #adding a subclass with inheritance and polymorphism
        class CameraSmartphone(Smartphone):
    def __init__(self, brand, model, battery_life, camera_megapixels):
        super().__init__(brand, model, battery_life)  # Initialize parent class
        self.camera_megapixels = camera_megapixels    # Extra attribute
    
    # Override make_call method (polymorphism example)
    def make_call(self, number):
        print(f"Using camera smartphone to call {number} from {self.brand} {self.model}...")
    
    def take_photo(self):
        print(f"Taking a photo with {self.camera_megapixels} MP camera on {self.brand} {self.model}")

