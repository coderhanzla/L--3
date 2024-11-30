class parrot:
    species = "Bird"

    def __init__(self , name , age):
        self.name = name
        self.age = age

rangila = parrot("Rangila" , 5)
kallu = parrot("Kallu" , 3)

print("Rangila is a" , rangila.species)
print("Kallu is a" , kallu.species)


print(f"{rangila.name} is {rangila.age} years old" )
print(f"{kallu.name} is {kallu.age} years old" )
