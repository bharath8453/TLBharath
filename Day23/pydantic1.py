from typing import Annotated
from annotated_types import Gt


class MyClass:
    age: Annotated[int, Gt(18)]  # must be > 18


class Main:
    def validate_age(self, age):
        if age <= 18:
            print("age must be > 18")
        else:
            print("Age is valid")


Main().validate_age(15)

