s = input()
def is_number(text):
    try:
        if float(text):
            return True
    except:
        return False
    
print(is_number(s))