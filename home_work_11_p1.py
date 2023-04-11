class Cat:

    def __init__(self, name: str, age: int, color: str, ration: str, *args, **kwargs):
        self.name = name
        self.age = age
        self.color = color
        self.ration = ration

    def __str__(self):
        return f'Cat {self.name}. Color = {self.color}. Years = {self.age}. Ration = {self.ration}'

    def meow(self):
        return f'Cat {self.name} say Meooow'

    @staticmethod
    def mau():
        return 'MAAAUU'


cat_murchik = Cat('Murchik', 2, 'orange', 'fish')
print(cat_murchik)
print(Cat.meow(cat_murchik))
print(cat_murchik.mau())
