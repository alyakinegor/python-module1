obj = {
    "hello": "bonjour",
    "goodbye": "au revoir",
    "cat": "chat",
    "dog": "chien",
    "house": "maison",
    "car": "voiture",
    "book": "livre",
    "water": "eau",
    "apple": "pomme",
    "tree": "arbre"
}






def add(key, value):
    obj[key] = value
    
def delete(key):
    del obj[key]

def search(key):
    return obj[key]

def swap_value(key, newVal):
    obj[key] = newVal