class house:
    def __init__(self,name,number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        p = (f"Название: {self.name}, кол-во этажей: {self.number_of_floors}")
        return p

    def go_to(self,new_floor):
        if new_floor > self.number_of_floors or new_floor < 1:
            print("Такого этажа не существует")
        else:
            for i in range(new_floor):
                print(i+1)

h1 = house('ЖК Эльбрус', 10)
h2 = house('ЖК Акация', 20)
# __str__
print(h1)
print(h2)

# __len__
print(len(h1))
print(len(h2))