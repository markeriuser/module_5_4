class House:
    houses_history = []

    def __new__(cls, *args, **kwargs):
        instance = super(House, cls).__new__(cls)
        cls.houses_history.append(args[0])
        return instance

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __del__(self):
        print(f"{self.name} снесён, но он останется в истории")

    def go_to(self, new_floor):
        if new_floor > self.number_of_floors or new_floor < 1:
            print ('такого этажа не существует')
        else:
           # print(f'надо приехать на {new_floor} этаж') #как вариант прописать куда ехать вместо перечисления каждого этажа
            for floor in range (1, new_floor + 1):
                print (floor)
    def __len__(self):
        return self.number_of_floors
    def __str__(self):
        return (f"название:{self.name}, количество этажей:{self.number_of_floors}")

    def __eq__(self, other):
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors
        return False

    def __lt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors < other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors < other


    def __le__(self, other):
        if isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors <= other


    def __gt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors > other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors > other


    def __ge__(self, other):
        if isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors >= other


    def __ne__(self, other):
        if isinstance(other, House):
            return self.number_of_floors != other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors != other


    def __add__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value
            return self

    def __radd__(self, value):
        return self.__add__(value)

    def __iadd__(self, value):
        return self.__add__(value)


h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

del h2
del h3

print(House.houses_history)

