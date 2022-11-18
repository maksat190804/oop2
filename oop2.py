class Human:
    def __init__(self,name,age):
        self.name = name 

    def __str__(self):
        return f' имя {self.name}, возраст {self.age}'

    def eat_spaghetti(self):
        return f' я могу есть спагетти'

class Robot:
    def __init__(self,name):
        self.name =  name 

    def __str__(self):
        return f'имя {self.name}'

    def drink_oil(self):
        return f'я могу потреблять машинное масло'
    
class Cyborg(Human,Robot):
    def __init__(self,name,age,nomber):
        self.name = name 
        self.age = name 
        self.nomber = nomber

    def __str__(self):
        return f' имя {self.name}, возраст {self.age}, номер {self.nomber} '

    

b = Cyborg('Макс', 17, 100)
print(b.eat_spaghetti())
print(b.drink_oil())




