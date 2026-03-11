# from typing import Any
# from typing import Optional, Union
from typing import Sequence, Mapping, Iterable
from typing import Callable
from typing import TypedDict

from dataclasses import dataclass
class Employee(TypedDict):
    emp_id: int
    name: str
    salary: int

payload: Employee = {
    'emp_id': 1,
    "name": 'Alice',
    'salary': 1000

}

@dataclass
class EmployeeCard:
    emp_id: int
    name: str

card = EmployeeCard(emp_id=1, name='alice')
print(card.emp_id)



EmployeeId = int
SalaryMap = dict[str, int]
Taglist = list[str]

emp_id: EmployeeId = 20
skills: Taglist = ['tag']
def print_names(items: Iterable[str]) -> None:
    for el in items:
        print(el)

def first_two(items: Sequence[str]) -> list[str]:
    return list(items[:2])

def get_salary(data: Mapping[str, int], name: str) -> int:
    return data[name]

def apply_formatter(text: str, formatter: Callable[[str], str]) -> str:
    return formatter(text)
# def stringify(val: Any) -> str:
#     return str(val)

# def find_by_name(emps: dict[int, str], emp_id: int) -> Optional[str]:
#     return emps.get(emp_id)

# def parse_emp_id(raw: Union[str, int]):
#     return int(raw)
# def apply_bonus(salary: int, bonus_percent: float) -> float:
#     return salary * (1 + bonus_percent / 100)

# res = apply_bonus(1000, 10.0)

#-----

# def uppercase_name(name: str)-> str:
#     return name.upper()

# print(uppercase_name(''))

# a: int = 5
# b: bool = True
# s: str = 'a'
# class Employee:
#     company: str 
#     def __init__(self, emp_id:int, name:str, salary:int) -> None:
#         self.emp_id: int = emp_id
#         self.name: str = name
#         self.salary: int = salary


names: list[str] = ['Alice', 'Bob']
salaries: dict[str, int] = {'Alice': 1000, 'Bob': 1200}
pair: tuple[str,int] = ('alice', 1)
s: set[str] = {'read', 'write'}
