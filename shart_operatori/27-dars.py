class Car:
    color = 'white'

    def __init__(self, model, color):
        self.model = model
        self.color = color

    def get_model(self):
        return self.model.upper()
    
    def get_color(self, color):
        self.color = color

    @property
    def info(self):
        return self.model + " " + self.color.c()
    
    @info.setter
    def info(self, name):
        self.model, self.color = name.split(' ')

    @info.deleter
    def info(self):
        self.model = ''
        self.color = ''

    @classmethod
    def c(self):
        return self.color
    
    @staticmethod
    def s(x):
        return x*x


print(Car.s(2))