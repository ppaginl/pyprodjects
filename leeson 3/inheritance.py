class Familymember:
    def __init__(self, eye_color, hight_cm):
        self.eye_color = eye_color
        self.hight_cm = hight_cm
    def show_traits(self):
        print("eye color:",self.eye_color)
        print("hight(cm)", self.hight_cm)
class kid(Familymember):
    def __init__(self, name, age, eye_color, hight_cm):
                self.name = name
                self.age = age
                super().__init__(eye_color, hight_cm)
    def show_traits(self):
        print("Name", self.name)
        print("age", self.age)
        super().show_traits()
    def favorite_hobby(self, hobby):
        print(self.name, "loves", hobby)
child = kid("maya", 10, "brown", 140)
child2 = kid("steve", 20, "black", 185)
child.show_traits()
child2.show_traits()
child.favorite_hobby("painting")
print("Is kid a subclass of family member?", issubclass(kid, Familymember))