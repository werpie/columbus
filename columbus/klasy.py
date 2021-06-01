class Paprociara():

    def __init__(self,name):
        self.name = name
        self.eq = equipment()
        self.eq.show_items()
        self.life = 1

    def check_life(self):
        if self.life<=0:
            self.death()
            return True
        else:
            return False

    def death(self):
        self.say("paprociara is dead")

    def say(self,text):
        print(text)

    def found(self,item):
        self.say("".join([self.name," has found ",item]))
        self.eq.item_add(item)

    def use(self,item):
        if self.check_pockets(item):
            return True

    def check_pockets(self,item):
        if item in self.eq.show_items():
            return True
        else:
            return False

    def empty_pockets(self):
        return self.eq.show_items()

class equipment():

    def __init__(self):
        self.items = []

    def item_add(self,item):
        self.items.append(item)

    def item_remove(self,item):
        self.items.remove(item)

    def show_items(self):
        print("list of my items: ", self.items)
        return self.items
