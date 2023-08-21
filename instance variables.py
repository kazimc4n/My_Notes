class worker:
    department_section = 1
    def __init__(self,name, surname, age, id):
        self.name = name
        self.surname = surname
        self.age = age
        self.id = id

    def show_info(self):
        print(f"ad: {self.name}, surname: {self.surname}, age: {self.age}, id: {self.id}")


worker1 = worker("ahmet","can",25,1)
worker2 = worker("mehmet","uh",30,2)

worker1.show_info()
worker2.show_info()

print(worker1.__dict__)
print(worker2.__dict__)
print(worker1.department_section)
print(worker.department_section)

print("--------")

print(worker2.department_section)
worker2.department_section = 2
print(worker2.department_section)