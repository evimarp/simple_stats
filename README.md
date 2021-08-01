# Simple stats

Computes some basic statistics on a collection of small positive integer.
<!-- GETTING STARTED -->
## Getting Started

The DataCapture object accepts numbers and returns an object for querying statistics about the inputs. Specifically, the returned object supports querying how many numbers in the collection are less than a value, greater than a value, or within a range.
### Prerequisites

- Requires python 3.

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/evimarp/simple_stats.git
   ```
2. Enter directory
   ```sh
   cd simple_stats
   ```
3. Enter python3 shell
   ```sh
   python3
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
>>> stats = capture.build_stats()
>>> stats.less(4) # should return 2 (only two values 3, 3 are less than 4)
2
>>> stats.between(3, 6) # should return 4 (3, 3, 4 and 6 are between 3 and 6)
4
>>> stats.greater(4) # should return 2 (6 and 9 are the only two values greater than 4)
2
```
- Also you can capture several items at once.
```pydocstring
>>> capture.add(3, 3, 4, 6)
```
- or passing a list of integers at initialize time. 
```python
capture = DataCapture(3, 3, 4, 6)
```
- Or use any combination of methods to add number into the collection.

```python
capture = DataCapture(3)
capture.add(4, 6)
capture.add(3)
```



<!-- LICENSE -->
## License

Distributed under the MIT License. 



<!-- CONTACT -->
## Contact

Evimar Principal - <evimar.principal@gmail.com>
[Linkedin](https://www.linkedin.com/in/evimarprincipal/)

Project Link: [https://github.com/evimarp/simple_stats](https://github.com/evimarp/simple_stats)
