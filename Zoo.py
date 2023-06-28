class Zoo:


    name = "Askaniya"
    location = "Lviv"
    area = 90
    capacity = 45
    regions = 5


    def __init__ (self, name, location, area, capacity, regions):
        self.name = name
        self.location = location
        self.area = area
        self.capacity = capacity
        self.regions = regions
        print("Name: "+name+" location: "+location+"area:"+str(area)+"capacity:"+str(capacity)+"regions:"+str(regions))


    @classmethod
    def increaseCapacity(cls):
        cls.capacity += 20
        print("Capacity increased, now: "+str(cls.capacity))


    @classmethod
    def spillArea(cls):
        cls.area /= 2
        print("The area decreased by 2 times. Now: "+str(cls.area))

    @classmethod
    def addNewRegion(cls):
        cls.regions += 1
        cls.area *= 2
        print("The number of regions was increased by 1 and the area is twice as large. Regions: "+str(cls.regions) + ", " +  "Area: " +str(cls.area))


zoo = Zoo('Askania nova', 'Lviv', 90, 45, 5)
zoo.increaseCapacity()
zoo.spillArea()
zoo.addNewRegion()
