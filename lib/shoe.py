#!/usr/bin/env python3

class Shoe:
    def __init__ (self, brand, size):
        self.brand = brand
        if (isinstance(size, int)):
            self.size = size
        else :
            print ("size must be an integer")
    
    def cobble(self):
        self.condition = "New"
        print("Your shoe is as good as new!")

converse = Shoe("converse", 45)