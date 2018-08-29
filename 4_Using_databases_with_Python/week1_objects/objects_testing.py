# Empty class with the x attribute; a single instance af a class
class PartyAnimal:
    x = 0

    def __init__(self):  # moment of construction
        print('I am constructed!')

    def party(self):
        self.x = self.x + 1
        print('So far:', self.x)

    def __del__(self):  # moment of destruction
        print('I am destructed with value:', self.x)

# Create a PartyAnimal object/instance of the PartyAnimal class and store it into the variable an
an = PartyAnimal()

# Call the object.method()
an.party()
an.party()
an.party()
an.party()

an = 42
print('Variable an contains:', an)

# Find out the type and methods of the variable an
print('Type:', type(an))
print('Methods;', dir(an))


# Multiple instances of a single class with parameters
# Two independent! instances
class PartyAnimal:
    x = 0
    name = ''

    def __init__(self, z):
        self.name = z
        print(self.name, 'I am constructed!')

    def party(self):
        self.x = self.x + 1
        print(self.name, 'Party count:', self.x)

    def __del__(self):
        print(self.name, 'I am deconstructed!')

s = PartyAnimal('Sally')  # Sally is a parameter z
j = PartyAnimal('Jim')  # Jim is a parameter
s.party()
j.party()
j.party()


# Class inheritance
class PartyAnimal:
    x = 0
    name = ''

    def __init__(self, z):
        self.name = z
        print(self.name, '== I am constructed ==')

    def party(self):
        self.x = self.x + 1
        print(self.name, '== Party count ==', self.x)

    def __del__(self):
        print(self.name, '== I am deconstructed ==')

class FootballFan(PartyAnimal):
    points = 0

    def touchdown(self):
        self.points = self.points + 7
        self.party()
        print(self.name, '== Points ==', self.points)


s = PartyAnimal('Sally')
s.party()

j = FootballFan('Jim')
j.party()
j.touchdown()

s.party()