from typing import TypedDict

class Persone(TypedDict):
    
    name : str
    age : int
    
new_persone : Persone = {'name': 'Ayush', 'age': 35}
print(new_persone)