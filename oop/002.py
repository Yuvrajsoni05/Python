class Sample():

    species = 'mammal'


    def __init__(self,breed,name):
        self.breed = breed
        self.name = name


x = Sample(breed = 'Lab',name="Send")
y = Sample(breed="Huskie",name="Send")
print(type(x))
print(x.breed)
print(x.name)
print(x.species)




