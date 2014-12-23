MultipleReturn
==============

An implementation of multiple return for python using the power of the `@multiplereturn` decorator.

A function that returns a tuple when decorated by `@multiplereturn` will instead return the first value in the tuple.

But if the caller wraps their call with the `values` function then the decorated function instead returns the original tuple.

A simple example:

```python
import * from multiplereturn

@multiplereturn
def divide(x, y):
  # Returns the dividend and remainder.
  return (x // y, x % y)
  
divide(5, 3)          # returns 1
values(divide(5, 3))  # returns (1, 2)
```
