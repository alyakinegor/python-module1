lines = [
    "2026-03-10,Room-A,09:00,Иван,Project,confirmed",
    "2026-03-10,Room-A,09:00,Мария,HR,cancelled",
    "2026-03-10,Room-A,10:00,Олег,Sales,confirmed",
    "2026-03-10,Room-B,09:00,Иван,Project,confirmed",
    "2026-03-10,Room-B,09:00,Нина,Finance,confirmed",
    "2026-03-10,Room-C,11:00,Мария,HR,confirmed",
    "2026-03-11,Room-A,09:00,Иван,Project,confirmed",
    "2026-03-11,Room-A,09:00,Павел,Support,confirmed",
    "2026-03-11,Room-B,10:00,Мария,HR,cancelled",
    "2026-03-11,Room-B,10:00,Мария,HR,cancelled",
    "2026-03-11,Room-C,10:00,Нина,Finance,confirmed",
    "2026-03-11,Room-D,10:00,Нина,Finance,confirmed"
]

bookings = []
# список словарей: date, room, slot, employee, team, status

room_stats = {}
# room -> {"total": 0, "confirmed": 0, "employees": set()}

slot_confirmed = {}
# (date, room, slot) -> список сотрудников с confirmed (ключ-кортеж)

employee_stats = {}
# employee -> {"hours": 0, "rooms": set()}

employee_time_rooms = {}
# (date, employee, slot) -> set комнат (ключ-кортеж)

daily_cancellations = {}
# date -> количество отмен

conflicts = []
# список кортежей (date, room, slot, employees)

double_booked_employees = set()
# сотрудники с бронью в нескольких комнатах в один слот


with open("rooms_schedule.txt", "w", encoding="utf-8") as file:
    # TODO: записать lines в файл
    for line in lines:
        file.write(line + '\n')


with open("rooms_schedule.txt", "r", encoding="utf-8") as file:
    for line in file:
        line = line.strip()
        if not line:
            continue

        arr = line.split(',')
        obj = {}
        obj['date'], obj['room'], obj['slot'], obj['employee'], obj['team'], obj['status'] = arr[0], arr[1],arr[2],arr[3],arr[4],arr[5]
        bookings.append(obj)



for b in bookings:
    room_stats.setdefault(b['room'], {"total": 0, "confirmed": 0, "employees": set()})
    room_stats[b['room']]['total'] += 1
    room_stats[b['room']]['employees'].add(b['employee'])
    if b['status'] == 'confirmed':
        room_stats[b['room']]['confirmed'] += 1
        slot_confirmed.setdefault((b['date'], b['room'], b['slot']), [])
        slot_confirmed[(b['date'], b['room'],b['slot'])].append(b['employee'])

        employee_stats.setdefault(b['employee'], {"hours": 0, "rooms": set()})
        employee_stats[b['employee']]['hours'] += 1
        employee_stats[b['employee']]['rooms'].add(b['room'])

        employee_time_rooms.setdefault((b['date'],b['employee'], b['slot']), set())
        employee_time_rooms[(b['date'],b['employee'], b['slot'])].add(b['room'])
    elif b['status'] =='cancelled':
        daily_cancellations.setdefault(b['date'], 0)
        daily_cancellations[b['date']] += 1


for key, employees in slot_confirmed.items():
    if len(employees) > 1:
        conflicts.append(tuple(key) + tuple(employees))


for (date, employee, slot), rooms in employee_time_rooms.items():

    if len(rooms) > 1:
        double_booked_employees.add(employee)

top_room = None
top_room_confirmed = -1


for k in room_stats.keys():
    if room_stats[k]['confirmed'] > top_room_confirmed:
        top_room_confirmed = room_stats[k]['confirmed']
        top_room = k

cancel_day = None
cancel_day_count = -1

for k in daily_cancellations.keys():
    if daily_cancellations[k] > cancel_day_count:
        cancel_day_count = daily_cancellations[k]
        cancel_day = k

with open("rooms_report.txt", "w", encoding="utf-8") as file:

    file.write(str(room_stats) + '\n')
    file.write(str(daily_cancellations) + '\n')
    file.write(str(employee_stats) + '\n')
    file.write('сотрудники с двойным бронированием: ' + str(double_booked_employees)+'\n')
    m = 0
    day = None
    for k in daily_cancellations:
        if m < daily_cancellations[k]:
            m = daily_cancellations[k]
            day = k
    file.write(f'топ-комната: {top_room}, день с максимумом отмен: {day}')