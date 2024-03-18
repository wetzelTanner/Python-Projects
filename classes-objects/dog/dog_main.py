class Dog:
    '''
    This is a dog class that has color and weight attributes
    '''
    # Constructor
    def __init__(self, input_color, input_weight):
        self.color = input_color
        self.__weight = input_weight

    # Object methods
    def speak(self):
        print('Woof')

    def gain_weight(self, extra):
        self.__weight += extra

    # Getter
    def get_weight(self):
        return self.__weight

    # Setter
    def set_weight(self, new_weight):
        self.__weight = new_weight

    # to_str()
    def __str__(self):
        return 'This ' + self.color + ' dog is ' + str(self.__weight) + ' pounds'


dog1 = Dog('white', 30)
dog2 = Dog('green', 50)

print(dog1)

print(dog1.color)
print(dog1.get_weight())

dog1.set_weight(60)
print(dog1.get_weight())
