class mammal:
    def walk(self):
        print("walk")


class dog(mammal):
    def bark(self):
        print("i am kutttaa")


class cat(mammal):
    def mew(self):
        print("i am billooooi")


dog1 = dog()
dog1.walk()
dog1.bark()
cat1 = cat()
cat1.walk()
cat1.mew()


