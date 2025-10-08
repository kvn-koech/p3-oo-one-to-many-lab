# lib/owner_pet.py

class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        if pet_type not in self.PET_TYPES:
            raise Exception(f"Invalid pet type: {pet_type}. Must be one of {self.PET_TYPES}")
        
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        Pet.all.append(self)

    def __repr__(self):
        return f"<Pet name='{self.name}' type='{self.pet_type}'>"


class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]

    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception("Only Pet instances can be added as pets")
        
        pet.owner = self

    def get_sorted_pets(self):
        owner_pets = self.pets()
        return sorted(owner_pets, key=lambda pet: pet.name)

    def __repr__(self):
        return f"<Owner name='{self.name}'>"