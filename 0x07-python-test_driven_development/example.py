test max/min numbers Python can handle ("inf" is infinity)
>>> print(add_integer(float("inf")))
Traceback (most recent call last):
...
OverflowError: cannot convert float infinity to integer
>>> print(add_integer(float("-inf")))
Traceback (most recent call last):
...
OverflowError: cannot convert float infinity to integer