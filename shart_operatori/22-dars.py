class Car:
    def __init__(self, model, color):
        self.model = model
        self.color = color

    def info(self):
        print(self.model + " " + self.color)

spark = Car('Spark', 'black')
nexia = Car('Nexia', 'white')

spark.info()
nexia.info()