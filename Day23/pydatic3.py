from typing import Annotated
from annotated_types import Gt
from pydantic import BaseModel, PositiveInt


class User(BaseModel):
    A: Annotated[int, Gt(18)]
    B: str = 'B'  
 
external_data = {   
    'A' : 20,
    'B' : 'a',
    'A' : 3,
    'B' : 'B',
    'A' : 2,
    'B' : 2 
}
try:
    user = User(**external_data)

except Exception as e:
    print("ivalid", e)

o = User(**external_data)
print(o)


'''
from typing import Annotated
from pydantic import BaseModel
# from datetime import datetime
class User(BaseModel):
    id: int
    name: str = "John Doe"
   
    
external_data = {
    'id': 1890,
    'name': 'bharath',
    'signup_ts': '2019-06-01 12:22',  
    'tastes': {
        'wine': 9,
        b'cheese': 7,  
        'cabbage': '1',  
    },
}

user = User (**external_data)
print(user.id)
print(user.name) 

'''