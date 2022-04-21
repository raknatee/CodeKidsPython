# Data container 

We can use ```dict``` for data/object representation.
```py
dad = {
    "name":"Father",
    "age":40,
    "car_ids": ["123", "567"]
}
mom = {
    "name":"Mother",
    "age":39,
    "car_ids": ["015"]
}
me = {
    "name":"CodeKids",
    "age":4,
    "car_ids": None,
    "toys": ["car1", "car2", "doll1", "doll2"]
}

diff = dad["age"]-mom["age"]
print(f"The difference between my dad age and my mom age is {diff}.")

number_of_my_toys = len(me["toys"]) 
print(f"I have {number_of_my_toys} toys.")
```
:::output
The difference between my dad age and my mom age is 1.
I have 4 toys.
:::