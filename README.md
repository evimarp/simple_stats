# Simple stats

Computes some basic statistics on a collection of small positive integer.
<!-- GETTING STARTED -->
## Getting Started
The core class is the `DataCapture` class, that add numbers to the collection, and creates a stats object, to query some stats (less, greater, between).

The DataCapture object accepts numbers and returns an object for querying statistics about the inputs. Specifically, the returned object supports querying how many numbers in the collection are less than a value, greater than a value, or within a range.
### Prerequisites

- Requires python 3.6+

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/evimarp/simple_stats.git
   ```
2. It's recommended create a virtual environment with `python3` and `pip` on it. 
[See more](https://docs.python.org/3/library/venv.html#module-venv)
   ```sh
   python3 -m venv ./venv
   ```

3. Install the requirements with pip.
   ```sh
   pip install -r requirements.txt
   ```


<!-- USAGE EXAMPLES -->
## Usage
Several ways to add number into the collection.

`add` method is used to add one or more integers to the collection.
```pydocstring
>>> from stats import DataCapture
>>> capture = DataCapture()
>>> capture.add(3)
>>> capture.add(3)
>>> capture.add(4)
>>> capture.add(6)
```
- Also you can capture several items at once.
```pydocstring
>>> capture.add(3, 3, 4, 6)
```
- or passing a list of integers at initialization time. 
```python
capture = DataCapture(3, 3, 4, 6)
```
- Or use any combination of methods to add number into the collection.

```python
capture = DataCapture(3)
capture.add(4, 6)
capture.add(3)
```
### Quering stats
After finish capture all data, you can generate `stats` object with `build_stats` method.
```pydocstring
>>> stats = capture.build_stats()
```
With this `stats` objects, you can invoke methods to query stats.

**Important: You can only query stats from numbers that are small positive integer up to 1000 included.**
#### Query: Less than
To know how many items are less than a specific number.    
```pydocstring
>>> stats.less(4) # should return 2 (only two values 3, 3 are less than 4)
2
```
#### Query: Greater than
To know how many items are great than a specific number.    
```pydocstring
>>> stats.greater(4) # should return 2 (6 and 9 are the only two values greater than 4)
2
```
#### Query: Between
To know how many items are between a specific range.    
```pydocstring
>>> stats.between(3, 6) # should return 4 (3, 3, 4 and 6 are between 3 and 6)
4
```

## Testing
Use `pytest` command for run the test suite in the command line.
```sh
>>> pytest
============================================================== test session starts ===============================================================
platform linux -- Python 3.9.1, pytest-6.2.4, py-1.10.0, pluggy-0.13.1
rootdir: ...
collected 4 items                                                                                                                                

test/test_stats.py ....                                                                                                                    [100%]

=============================================================== 4 passed in 0.02s ================================================================
```

<!-- LICENSE -->
## License

Distributed under the MIT License. 



<!-- CONTACT -->
## Contact

Evimar Principal - <evimar.principal@gmail.com>
[Linkedin](https://www.linkedin.com/in/evimarprincipal/)

Project Link: [https://github.com/evimarp/simple_stats](https://github.com/evimarp/simple_stats)
