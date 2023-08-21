

class worker:

    def __init__(self, name, surname, age, id):
        self.name = name
        self.surname = surname
        self.age = age
        self.id = id

    def show_info(self):
        print(f"name: {self.name}, surname: {self.surname}, age: {self.age}, id: {self.id}")


worker1 = worker("ahmet", "can", 25, 1)
worker2 = worker("mehmet", "san",30, 2)

worker1.show_info()
worker2.show_info()

worker.show_info(worker1)
worker.show_info(worker2)