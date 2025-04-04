class Animal:
    def speak(self):
        print("Animal makes a sound")

class Dog(Animal):
    def speak(self):   
        print("Dog barks")

a = Animal()
a.speak()   

d = Dog()
d.speak()  
