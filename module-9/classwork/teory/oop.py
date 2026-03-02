from abc import ABC, abstractmethod
class EmployeeBase(ABC):
    def __init__(self, emp_id, name):
        self.emp_id = emp_id
        self.name = name

    @abstractmethod
    def compensation(self):
        pass

class Employee(EmployeeBase):
    company = '123'
    def __init__(self, emp_id, name, salary):
        self.emp_id =emp_id
        self.name = name
        self.salary = salary
        self._salary = 0

    def __str__(self):
        return f'{self.name}: {self.salary}'

    def __eq__(self, other):
        if not isinstance(other, Employee):
            return NotImplemented
        return self.emp_id == other.emp_id
    def compensation(self):
        return self.salary
    # def info(self):
    #     print(self.emp_id, self.name, self.salary)
    
    # @classmethod
    # def from_string(cls, raw):
    #     emp_id, name, salary = raw.split(', ')
    #     return cls(int(emp_id), name, int(salary))

    # @staticmethod
    # def valid_name(name):
    #     return len(name.strip()) >= 2
    
    # def get_salary(self):
    #     return self.salary
    
    # def set_salary(self, value):
    #     if value < 0:
    #         self.salary = 0
    #     else:
    #         self.salary = value

    # @property
    
    # def salary(self):
    #     return self._salary
    
    # @salary.setter
    # def salary(self, val):
    #     self._salary = val

    # @salary.deleter
    # def salary(self):
    #     self._salary = 0
    

    def yearly_income(self):
        return self.salary * 12



class LoggableMixin:
    def log(self, message):
        print(f'[LOG] {self.name}: {message}')


class Manager(Employee, LoggableMixin):
    def __init__(self, emp_id, name, salary, bonus):
        super().__init__(emp_id, name, salary)
        self.bonus = bonus
    
    def yearly_income(self):
        return super().yearly_income() + self.bonus

m = Manager(3, 'Anton', 2000, 5000)
m1 = Manager(3, 'Jack', 1000,3000)
print(m == m1)