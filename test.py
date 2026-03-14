#object oriented programing
class dog:
    def __init__(self,name):
        self.name=name
    def display(self):
        print("my name is "+self.name)

name=dog("nusaybah")
name.display()

class car:
    def __init__(self,color,brand,model):
        self.color=color
        self.brand=brand
        self.model=model
    def start(self):
        print("car started")
    def stop(self):
        print("car stopped")
    
    def get_color(self):
        return self.color
    def set_model(self,newmodel):
        self.model=newmodel
    
vihecle=car("black","volvo","xc60")

vihecle.start()
print(vihecle.get_color())
vihecle.set_model("ab5")
print(vihecle.model)

class person():
    def __init__(self,age,height):
        self.age=age
        self.height=height
    def get_age(self):
        return self.age
    def set_height(self,newheight):
        self.height=newheight
    def info(self):
        print(self.height,self.age)

human=person(19,190)

print(human.get_age())
print(human.set_height(234))
human.info()