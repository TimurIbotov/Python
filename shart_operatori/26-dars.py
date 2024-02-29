class Car:
    def __init__(self, model, color):
        self.model = model
        self.color = color

    def get_model(self):
        return self.model.upper()
    
    def get_color(self, color):
        self.color = color

    @property
    def info(self):
        return self.model + " " + self.color
    
    @info.setter
    def info(self, name):
        self.model, self.color = name.split(' ')

    @info.deleter
    def info(self):
        self.model = ''
        self.color = ''

spark = Car('Spark', 'black')

delattr(spark, 'info')

print( getattr(spark, 'info') ) 

#print( hasattr(spark, 'info')) True ili Foulse