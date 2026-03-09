# def devide(a, b):
#     return a / b

# print(devide(10, 0))

raw_val = ['10', '6', 'abc', '3']

# nums = []
# for el in raw_val:
#     try:
#         nums.append(int(el))
#     except ValueError:
#         print(f'{el} - не число')
#         continue
    

# print(nums)

# def parse(a, b):
#     try:
#         x = int(a)
#         y = int(b)
#         return x / y
#     except ValueError:
#         return 'Некорректные входные данные'
#     except ZeroDivisionError:
#         return 'На 0 делить нельзя'
    
# print(parse(10, 'bb'))
# print(parse(10, 0))
# print(parse(10, 5))


# try:
#     data = {'name': 'Alice'}
#     print(data['email'])
# except KeyError as e:
#     print(type(e).__name__)
#     print(e.args)
#     print(e)

# def set_discount(percent):
#     if not 0 <= percent <= 100:
#         raise ValueError('Скидка должна быть в диапазоне 0-100')


# print(set_discount(1000))

# def load_user(data, user_id):
#     try:
#         return data[user_id]
#     except KeyError:
#         print(f'Пользователь не найден: {user_id}')
#         raise 

# users = {1: 'Alice'}
# try:
#     print(load_user(users, 2))
# except KeyError:
#     print('Ошибка')

# class ConfigError(Exception):
#     pass

# def load_port(raw_port):
#     try:
#         return int(raw_port)
#     except ValueError as e:
#         raise ConfigError('Поле PORT должно быть целым числом') from e
    
# try:
#     load_port('aaa')
# except ConfigError as e:
#     print('Тип:', type(e).__name__)
#     print(type(e).__cause__)

# class EmployeeError(Exception):
#     pass

# class EmployeeNotFoundError(EmployeeError):
#     message2 = 'Сотрудник не найден'
#     pass

# class SalaryValidationError(EmployeeError):
#     pass

# def find_employee(employees, emp_id):
#     if emp_id not in employees:
#         raise EmployeeNotFoundError(f'Сотрудник {emp_id} не найден')
#     return employees[emp_id]
# def validate_salary(value):
#     if value < 0:
#         raise SalaryValidationError('ЗП не может быть отрицательной')
    
# try:
#     find_employee({}, 1)

# except EmployeeNotFoundError as e:
#     print(e.message2)
# except SalaryValidationError as e:
#     print(e)

def normalize_percent(x):
    assert isinstance(x, int), 'должен быть числом'
    if not 0 <= x <= 100:
        raise ValueError('Процент должен быть от 0 до 100')
    return x / 100

print(normalize_percent(25))
print(normalize_percent('aa'))