lines = [
    "SHP-1001,North,Chicago,3,3,40,delivered",
    "SHP-1002,North,Boston,4,6,20,delivered",
    "SHP-1003,East,Miami,2,2,35,cancelled",
    "SHP-1004,East,Chicago,5,8,15,delivered",
    "SHP-1005,West,Dallas,1,1,50,delivered",
    "SHP-1006,West,Miami,2,4,30,delivered",
    "SHP-1002,North,Boston,4,6,20,delivered",
    "SHP-1007,South,Atlanta,6,6,25,in_transit",
    "SHP-1008,South,Dallas,3,5,10,delivered"
]

deliveries = []
# список словарей с записями доставок
# ключи: shipment_id, warehouse, city, planned_day, actual_day, items, status

warehouse_stats = {}
# warehouse -> {"total": 0, "delayed": 0}

cities = set()
# множество городов доставки

shipment_counter = {}
# shipment_id -> количество встреч

duplicate_shipments = []
# список shipment_id, которые дублируются

city_delivered_items = {}
# city -> суммарное количество items для status == delivered


with open("delivery_log.txt", "w", encoding="utf-8") as file:
    # TODO: записать строки lines в файл
    for el in lines:
        file.write(el + '\n')


with open("delivery_log.txt", "r", encoding="utf-8") as file:
    for line in file:
        line = line.strip('\n')
        if not line:
            continue
        arr = line.split(',')
        obj = {}
        obj['shipment_id'] = arr[0]
        obj['warehouse'] = arr[1]
        obj['city'] = arr[2]
        obj['planned_day'] = int(arr[3])
        obj['actual_day'] = int(arr[4])
        obj['items'] = int(arr[5])
        obj['status'] = arr[6]
        deliveries.append(obj)


for d in deliveries:
    warehouse_stats.setdefault(d['warehouse'], {"total": 0, "delayed": 0})
    warehouse_stats[d['warehouse']]['total'] += 1
    if d['planned_day'] < d['actual_day']:
        warehouse_stats[d['warehouse']]['delayed'] += 1
    cities.add(d['city'])
    shipment_counter.setdefault(d['shipment_id'], 0)
    shipment_counter[d['shipment_id']] += 1
    if d['status'] == 'delivered':
        city_delivered_items.setdefault(d['city'], 0)
        city_delivered_items[d['city']] += d['items']



for shipment_id, count in shipment_counter.items():
    if count > 1:
        duplicate_shipments.append(shipment_id)

worst_warehouse = None
max_delay_rate = -1

m = 0 
for k in warehouse_stats.keys():
    delay_rate = int((warehouse_stats[k]['delayed'] / warehouse_stats[k]['total']) * 100)
    if m < delay_rate:
        m = delay_rate
    warehouse_stats[k]['delay_rate'] = delay_rate

with open("delivery_report.txt", "w", encoding="utf-8") as file:

    file.write(str(warehouse_stats) + '\n')
    file.write(str(cities)+'\n')
    file.write(str(duplicate_shipments)+'\n')
    m = 0

    for k in warehouse_stats:
        if warehouse_stats[k]['delay_rate']> m:
            m = warehouse_stats[k]['delay_rate']
            worst_warehouse = k

    file.write(f'Склад с самым большим количеством просрочек: {worst_warehouse}\n')
    file.write(str(city_delivered_items))