class Myclass:
    def __init__(self,a,b):
       self.a=a
       self.b=b
       print("this is the initilazation block")
    def mymethod1(self):
        print(self.a)
        print(self.b)
objects = Myclass(76,89)
objects.mymethod1()
objects1=Myclass(2516,8597)
print(objects1.b)
Myclass(860,86).mymethod1()
print(Myclass(34,56).a)
print(objects.a)
print(objects.b)
