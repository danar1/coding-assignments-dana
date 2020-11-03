# Builtins Assignment #2

Implement the function `is_won_loto` in [assignment2.py](src/assignment2.py) that receives two parameters:
1. A list of tuples (contains only numbers) 
1. A given `loto number`. 

The function `is_won_loto(list_of_tuples, loto_number)` will return `True` if **EITHER** of these conditions are met
- The **max** number in **ALL** tuples is equal to the given `loto_number` \
`OR`
- The **sum** of the first 2 numbers in **ALL** the tuples is equal to the given `loto_number` \
`OR`
- The **next to last** number in **ALL** the tuples is equal to the given `loto_number`

If **NONE** of the 3 checks above return `True`, then the function should return `False`
> **HINT:** Most of the operations here (including the True/False checks) can be done by a Builtin function.
> We highly recommend you go through the different Builtin functions thoroughly before you decide to implement.

## Testing the output

In order to help you be sure your implementation works you can simply run the [assignment2.py](src/assignment2.py) as follows:
```shell script
$ python src/assignment2.py 
```
> This should print out to the terminal a number of tests and their expected result.
> If the output result is wrong, check again.

---