# Builtins Assignment #1

Implement the function `convert_number_lists_to_text(list1, list2)` in [assignment1.py](src/assignment1.py). The function takes two lists (`list1` and `list2`)
 that contain numbers, converts each number into its `ascii` representation and joins the strings based on their matching index.
 
> **HINT:** Most of the operations here (including the ascii conversion) can be done by a Builtin function.
> We highly recommend you go through the different Builtin functions thoroughly before you decide to implement.

Confusing? see further details below.

## Function Logic
For a given 2 lists of `n` equal size, the `convert_number_lists_to_text(list1, list2)` will:
1. Convert each number in the two lists to its `ascii` representation.
1. Concatenate all the values in the two lists by the order of their indexes  (e.g `the value in index 0 in list1` + `the value in index 0 in list2` + `the value in index 1 in list1` + `the value in index 1 in list2` etc.).
1. return the concatenated string

> NOTE: the values in `list1` must always be concatenated before the value in `list2`
Still don't get it? See examples below.

## Real Example
Given two lists:
* `list1 = [65,80]`
* `list2 =  [109,77]`

The `ascii` representation of the number 65 found in `list1` at index **0** is `A` \
The `ascii` representation of the number 109 found in `list2` at index **0** is `m` \
The `ascii` representation of the number 80 found in `list1` at index **1** is `P` \
The `ascii` representation of the number 77 found in `list2` at index **1** is `M`

Hence the output that would be return from the `convert_number_lists_to_text(list1, list2)` function would be: 

**"AmPM"**


## Testing the output

In order to help you be sure your implementation works you can simply run the [assignment1.py](src/assignment1.py) as follows:
```shell script
$ python src/assignment1.py 
```
> This should print out to the terminal a **meaningful sentence**.
> If the output is not clear, something is wrong...check again.


Done? Good job!

[Go to assignment #2](assignment2.md)

---
