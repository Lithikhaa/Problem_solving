class Animal:             #class name (Animal)
    
    def __init__(self,name,animaltype,speciesgender): # self means  (animal1)indha object oda name,animaltype,gender nu oru ref address ha it stores
        self.name = name                # only one self.name = name na attributes
        self.type = animaltype                      # multiple attributes(name,type,gender) called  properties
        self.gender = speciesgender
    
    def println(self):
        print(self.name,'this is the name of the animal')
        print(self.type,'this is the type of the animal')
        
    def checking(self):                                   # methods -- println,checking
        if self.gender == 'male':
            print('This is cannot produce a baby animal')
        else:
            print('This is can produce a baby animal')          # __init__  'lion','wildanimal','male' these values will be initialized without calling the functions
        
animal1 = Animal('lion','wildanimal','male')
animal1.println()

animal2 = Animal('Tiger','wildanimal','female')
animal2.checking()

        
animal1.name = 'elephant'                 # modifying the name from lion into elephant
animal1.println()
        
animal1.type = input()
animal1.println()    
        
