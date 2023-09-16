## Python LRU Cache

### Prerequisites
* [Python](https://www.python.org) Installed
* Computer you can install Python packages

### How to run the tests
pytest is used for testing for this LRU cache project

To install pytest, simply run the command:  `pip install -r requirements.txt`. This command may vary on your version and installation of Python.

Once you have installed pytest, run the command `pytest tests` in the root directory of this project.

You will see the test results in your terminal.

### How to use this project

I have initialized an example cache in **main.py**, but you may instantiate it anywhere you like.

The cache has two methods, put_value and get_value.

_put_value_: Adds a value on the cache, you provide a key and value, and removes the oldest value from the cache

_get_value_: Gets a value from the cache based on a key you provide then move the value you got to the newest accessed value position


Example of project LRU Cache:

LRUCahe(3)

put_value(1, 'A')
put_value(2, 'B')
put_value(3, 'C')

cache = [(1, 'A'), (2, 'B'), (3, 'C')]

get_value(1)

cache = [(2, 'B'), (3, 'C'), (1, 'A')]

put_value(4, 'D')

cache = [(3, 'C'), (1, 'A'), (4, 'D')]
