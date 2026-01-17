class Pet:
    def __init__(self, name):
        self.name = name
        self.energy = 5

    def play(self):
        if self.energy > 0:
            self.energy -= 1
            print(self.name, "is playing! 🐾")
        else:
            print(self.name, "is tired! 😴")

    def eat(self):
        self.energy += 2
        print(self.name,"is eating! 🍔" )

    def status (self):
        print(self.name, "energy:", self.energy)


pet = Pet("Adelade")  

print(" 🐶PET GAME🐶 ")

while True:
    choice = input("play/eat/status/quit: ").lower()
            
    if choice == "play":
       pet.play()
    elif choice == "eat":
         pet.eat()
    elif choice == "status":
         pet.status()
    elif choice == "quit":
         print("Goodbye")
         break

         
            