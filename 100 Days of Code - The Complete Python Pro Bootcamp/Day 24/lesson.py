#inheritance of classes


class Animal:
    def __init__(self):
        self.num_eyes = 2
    
    def breathe(self):
        print("Inhale, Exhale")
        

# you can inherit attributes from a different class by inserting into the parentheses, like below, and calling super().__init__()
class Fish(Animal):
    def __init__(self):
        super().__init__()

    def breathe(self):
        super().breathe()
        print("Doing so underwater")
        
    def swim(self):
        print("Moving in Water")


nemo = Fish()
nemo.swim()
nemo.breathe()
print(nemo.num_eyes)