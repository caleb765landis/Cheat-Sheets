class MyClass:
    # Constructor
    def __init__(self, nums, name="Anonymous"):
        # Create member variables
        self.nums = nums
        self.size = len(nums)
        self.name = name

    # self key word required as param
    def getLength(self):
        return self.size

    def getDoubleLength(self):
        return 2 * self.getLength()
    
    def getName(self):
        return self.__name

    def setName(self, name):
        self.__name = name

    name = property(getName, setName)


myObj = MyClass([1, 2, 3])
print(myObj.getLength())
print(myObj.getDoubleLength())
print(myObj.name)
myObj.name = "Guido"
print(myObj.name)
