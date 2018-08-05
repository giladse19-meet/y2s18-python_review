# Write your solutions for 1.5 here!
class Superheros:
    def __init__(self, name, superpower, strengh):
        self.name = name
        self.superpower = superpower
        self.strengh = strengh

    def hero(self):
        print(self.name)
        print(self.strengh)

    def save_civilian(self, work):
        if self.strengh - work < 0:
            print("not strong enough") 
        else:
            left = self.strengh - work
            self.strengh  = left
            print(left)
hero_1 = Superheros("dicktetor", "superpoop", 7)

hero_1.hero()
hero_1.save_civilian(3)

