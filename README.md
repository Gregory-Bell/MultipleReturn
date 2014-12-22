MultipleReturn
==============

An implementation of multiple return for python using the power of the `@multiplereturn` decorator.

A function decorated by `@multiplereturn` that returns a tuple, will instead return the first value in the tuple.

But, if the caller wraps their call with the `all_results` function, it instead returns the original tuple.

```python
import * from multiplereturn

@multiplereturn
def divide(x, y):
  # Returns the dividend and remainder.
  return (x // y, x % y)
  
divide(5, 3)               # returns 1
all_results(divide(5, 3))  # returns (1, 2)
```
