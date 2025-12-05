import logging
logging.basicConfig(level=logging.DEBUG)
logging.info("Starting User validation")
logging.debug("Importing necessary modules")
logging.warning("Ensure that the JSON file exists ")
logging.error("Handle exceptions properly")

import json
import pydantic
from pydantic import BaseModel
from typing import Annotated
from annotated_types  import Gt
class User(BaseModel):
    A: Annotated[int, Gt(18)] 
    B:Annotated[str, pydantic.constr(min_length=3, max_length=10)]
with open('output.json', 'r') as f1:
    data=json.load(f1)    
obj=User(**data)
print(obj)
try:
    if obj.A <= 18:
      print("age must be in 18")
      print("age invalid")
    else:
        print("A valid")
except pydantic.ValidationError as e:
    print(e.json())    
