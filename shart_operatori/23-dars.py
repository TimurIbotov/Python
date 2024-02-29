class Car:
    def __init__(self, model, color):
        self.model = model
        self.color = color

    def get_model(self):
        return self.model.upper()
    
    def get_color(self, color):
        self.color = color

    def info(self):
        print(self.model + " " + self.color)

spark = Car('Spark', 'black')
nexia = Car('Nexia', 'white')

spark.set_color("blue")

print(spark.get_model())
print(nexia.get_model())