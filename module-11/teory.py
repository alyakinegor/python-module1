import json
import pickle
obj = {
    'id': 1,
    'name': 'chair',
    'price': 1000
}

json_text = json.dumps(obj, indent=2)
n = json.loads(json_text)

with open('product.json', 'w', encoding='utf-8') as f:
    json.dump(obj, f, indent=2)

with open('product.json', 'r', encoding='utf-8') as f:
    l = json.load(f)

data = pickle.dumps(obj)
r_data = pickle.loads(data)
with open('product.pkl', 'wb') as f:
    pickle.dump(obj, f)

with open('product.pkl', 'rb') as f:
    load_pkl = pickle.load(f)
print(load_pkl)