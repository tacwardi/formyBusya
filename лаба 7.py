class Employee:
    def __init__(self,name,id):
        self.name = name
        self.id = id
    def get_info(self):
        return f'Сотрудник и его id:{self.name , self.id}'
class Manager(Employee):
    def __init__(self,name,id,department):
        Employee.__init__(self,name,id)
        self.department = department
    def manage_project(self):
        return (f'{self.name} управляет отделом {self.department}')
class Technician(Employee):
    def __init__(self,name,id,specialization):
        Employee.__init__(self,name,id)
        self.specialization = specialization
    def perform_maintenance(self):
        return (f'{self.name} выполняет тех. обслуживание {self.specialization}')
class TechManager(Technician,Manager):
    def __init__(self,name,id,department,specialization):
        Technician.__init__(self, name, id, specialization)
        Manager.__init__(self, name, id, department)
        self.team= []
    def project_manage_perform_maintenance(self):
        return (f'{self.name} выполняет тех. обслуживание {self.specialization} и управляет отделом {self.department}')
    def add_employee(self,employee):
        self.team.append(employee)
        print(f"Сотрудник {employee.name} добавлен в команду.")
    def get_team_info(self):
        if not self.team:
            print("В команде нет сотрудников.")
            return
        print(f"Команда {self.name}:")
        for member in self.team:
            print(f" - {member.get_info()}")
tech = Technician("Дмитрий", 105, "Сетевой инженер")
emp = Employee("Ольга", 106)
boss = TechManager("Сергей", 777, "IT-отдел", "Архитектор ПО")
boss.add_employee(emp)
boss.add_employee(tech)
boss.get_team_info()
print(boss.project_manage_perform_maintenance())
