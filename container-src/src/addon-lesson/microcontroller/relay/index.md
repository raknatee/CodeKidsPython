# Relay 5V with LED 12V


## Off

```py
from machine import Pin

signal = Pin(26,Pin.OUT)
signal.off()
```

![img](./off.png)

## On

```py
from machine import Pin

signal = Pin(26,Pin.OUT)
signal.on()
```
![img](./on.png)