# Challenge 7

This challenge will require you to do Lunar Arithmatic (borrowed from [here](https://programmingpraxis.com/2019/01/22/lunar-arithmetic/)), a different way of doing math. The requirements boil down to the following:

- The calculation is still done digit by digit
- Addition would be the larger of the two digits
    - Examples:
        - `1 + 5 = 5`
        - `2 + 2 = 2`
        - `8 +  4 = 8`
- Multiplication would be the smaller of two digits
    - Examples:
        - `1 * 5 = 1`
        - `2 * 2 = 2`
        - `8 * 4 = 4`

## More complicated examples

*Addition:*
```
  123
 + 45
 ----
  145
```

*Multiplication:*
```
  123
 x 45
 ----
  123
 123
 ----
 1233
```

## Running your code

The functions for you to implement has already been included in [solution.py](./src/solution.py). You may use these to get started. Like in the previous task, a [test.py](./src/test.py) file has also been included to help you validate your code. Unlike the previous challenge, there are no time requirements.
