# List in List

## project structure
```
+-- lesson-02
|    +-- main.py
```

## List

```py
friends = ["James", "David", "Anthony", "Larry"]
```

```py
friends = ["James", "David", "Anthony", "Larry"]
print(len(friends)) # 4
print(friends[0])   # James
print(friends[1])   # David
print(friends[2])   # Anthony
print(friends[3])   # Larry
```


## Nested List

```py
friends = [
    ["James",10,"a"], 
    ["David", 9,"b"], 
    ["Anthony", 8], 
    "Larry"
]
```

```py
friends = [
    ["James",10,"a"], 
    ["David", 9,"b"], 
    ["Anthony", 8], 
    "Larry"
]
print(len(friends))         # 4

print(friends[0])           # ["James",10,"a"]
print(len(friends[0]))      # 3
print(friends[0][0])        # James
print(friends[0][1])        # 10
print(friends[0][2])        # a

print(friends[2])           # ["Anthony", 8]
print(len(friends[2]))      # 2

print(friends[3])           # Larry
```