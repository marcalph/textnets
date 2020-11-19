msg: str = "Hello World"

print(msg)

from typing import List


def greet_all(names: List[str]) -> None:
# def greet_all(names):
    for name in names:
        print('Hello ' + name)


names = ["Alice", "Bob", "Charlie"]
ages = [10, 20, 30]

greet_all(names)   # Ok!
# greet_all(ages)
