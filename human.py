class Human:
    _count = 0


    def __init__(self, name, surname, age, alive):
        self.name = name
        self.surname = surname
        self.age = age
        self.alive = alive
        Human._count += 1


    def _define_majority(self):
        return "Underage" if self.age <= 18 else "Adult"

    def __str__(self):
        return f"{self.name} {self.surname}: \nage = {self.age};" \
               f" \nalive = {self.alive};" \
               f" \nstatus = {self._define_majority()}"



def main():
    human1 = Human("Alex", "Peterson", 32, "alive")
    human2 = Human("Jon", "Snow", 12, "alive")
    print(human1.__str__(), human2.__str__(), sep='\n')
    print("You have", Human._count, "people")



if __name__ == "__main__":
    main()







