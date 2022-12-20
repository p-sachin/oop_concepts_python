from item import Item
# For broken phones it is best to inherit the parent class Item as adding a instance attribute broken
# phone to the constructor is not a good practice and make it complex.

# Parent Class are those class which we inherit and Child Class are mutiple classes that inherit from parent class

class Phone(Item):
    def __init__(self, name: str, price: float, quantity, broken_phones):
        # Call to super function to have access to all attributes / methods including class attributes
        super().__init__(
            name, price, quantity
        )

        # Run validations to the received argument
        assert broken_phones >= 0, f"Broken Phones {broken_phones} is not greater or equal to zero!"

        # Assign to self object
        self.broken_phones = broken_phones