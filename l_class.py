class People:
    def __init__(self, birth, name, surname):
        self.birth = birth
        self.name = name
        self.surname = surname

    def about_myself(self, string="About me "):
        print(f'{string} - {self.name} {self.surname} - {self.birth}')

p1 = People(1995, "Max", "Ivanov")
p1.set_keywora("key")
p1.get_sym_ttitle()

print("---------------")

p2 = People(2000, "Denis", "Petrov")
p2.about_myself()


