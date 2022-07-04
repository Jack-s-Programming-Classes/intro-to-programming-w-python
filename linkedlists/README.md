# Linked Lists

We will write a python implementation of linked lists. According to [Wikipedia](https://en.wikipedia.org/wiki/Linked_list), a linked list is “a linear collection of data elements whose order is not given by their physical placement in memory. Instead, each element points to the next”

We will have 3 files: `linkedlist.py`, and `test.py`. 

- `linkedlist.py` will contain the `node` and `linkedlist` classes that you will implement.
- `test.py` is where you will be writing and running your unit tests. Make sure to thoroughly test the functionality of your linked list program to ensure that it behaves correctly and reacts to invalid inputs accordingly.

**The starter code is available on our class github repo.**

# Implementation

Here are the things that must be implemented. Think about what is needed before you start writing the code! Use only what you need, or your code might become cluttered. Also, make sure to give your variables names that are easy to understand.

### `class node`

- member variables
    - `self.value`  - the value that this node is storing
    - `self.next`  - the `Node` object that comes next
- methods
    - `__init__(self, value=None)`
        - initializes a caesarCipher class instance, is an identity map by default (`_shift = 0`)
        - **input:** `value` (default = None), can be any datatype
        - **output:** void
    - `__repr__(self)`
        - when `print()` is called on this object, it prints a representative string that shows what this instance is. 
        - **input:** void
        - **output:** `whatever datatype self.value is`

### `class LinkedList`

- member variables
    - `head`  - the first node of the list
- methods
    - `__init__(self, head = None)`
        - initializes a linkedlist class instance
        - **input:** `node head' (default = None)
        - **output:** void
    - `insert(self, value, index=None)`
        - inserts a value into the specified index location in the list. if index not provided, insert value at the end of the list. **if index is out of range, throw an exception! use references found below to learn how to throw exceptions, and also how to test for them.**
        - **input:** `any value`, `int index` (default = None)
        - **output:** void
    - `pop(self, index=None)`
        - **returns**, then removes value from specified location in the list. if index not provided, return then remove value at the end of the list. **if index is out of range or the list is empty, throw an exception! use references found below to learn how to throw exceptions, and also how to test for them.**
        - **input:** `int index` (default = None)
        - **output:** `the value stored in location`
    - `__repr__(self)`
        - when `print()` is called on this object, it prints a representative string that shows what this instance is.
        - **input:** void
        - **output:** `string` (in the form **“<linkedlist object at 0x106caaee0, [1,2,3,4,5]>”** where 0x106caaee0 is replaced by the actual memory location of object, and [1,2,3,4,5] with the actual list representation of your linked list.)

# Testing

As we covered in class, please be thorough in your testing process. Test for as many cases as you can think of, especially edge cases (first element, last element, etc.) and base cases (empty data structures or single-element data structures, trivial cases, etc.)

Refer to the documentation for help on using the `unittest` module in python.

You are responsible for making sure your program works correctly!!

# Helpful Resources

Misc reference

- [python unittest module docs](https://docs.python.org/3/library/unittest.html)
- [python exceptions](https://docs.python.org/3/tutorial/errors.html)
- [python try-except block / handling exceptions](https://docs.python.org/3/tutorial/errors.html#handling-exceptions)

