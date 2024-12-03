class Dog:
    animal = "Dog"

    def __init__(self, breed, color):
        self.breed = breed
        self.color = color
    
    def doginfo(self):
        print("Breed:", self.breed)
        print("Color:", self.color)
        print()

dog1 = Dog("Labrador", "golden")
dog2 = Dog("Beagle", "white")

print("Dog1 details are :")
dog1.doginfo()
print("Dog2 details are :")
dog2.doginfo()
