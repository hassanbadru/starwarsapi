# Hassan Badru
### YouGov - Starwars API

## Libraries
- [x] PYTEST

### Install Virtual Environment
With Python 3, run the following command to create a new virtual environment
```bash
python3 -m venv [ENVIRONMENT NAME]
```
Activate the new virtual environment
```bash
source '[ENVIRONMENT NAME]/bin/activate'
```
## Solution
Navigate to project folder
### Root Folder
```
solution
    ├── yougov.py
    └── testdata/
    |   └── solution_result.json
    |   └── starship9.json
    └── output/
        └── characters.csv
        └── test.csv
    ├── README.md
    ├── requirements.txt
    ├── helpers.py
    ├── test_yougov.py
    ├── .git/
    └── .gitignore

```

### Install Dependencies
Use pip to install the necessary dependencies with requirements.txt
```bash
pip install -r requirements.txt
```

### Run solution
```bash
python yougov.py
```
Output
```
$ results csv produced
```

This solution would produce the file ```characters.csv``` and add this file to **output** folder within the root directory. **output** folder is created if it doesn't  exist.



## Test App
To run test:
```bash
py.test -vv
```
Sample Test
```
platform darwin -- Python 3.7.3, pytest-5.3.1, py-1.8.0, pluggy-0.13.1 -- /path/to/yougovenv/bin/python3
cachedir: .pytest_cache
rootdir: /path/to/solution
collected 5 items                                                                                                                                                                   

test_yougov.py::test_float_conv PASSED                                                                                                                                        [ 20%]
test_yougov.py::test_endpoint PASSED                                                                                                                                          [ 40%]
test_yougov.py::test_csv PASSED                                                                                                                                               [ 60%]
test_yougov.py::test_species PASSED                                                                                                                                           [ 80%]
test_yougov.py::test_solution PASSED                                                                                                                                          [100%]

================================================================================ 5 passed in 25.03s =================================================================================

```


## Functionality
- [x] Finds characters who appear in the most Star Wars films
- [x] Sorts top ten characters by height in descending order
- [x] Produces a CSV with the following columns: name, species, height, appearances
- [x] Sends the CSV to httpbin.org


## Design & Approach
- Traverse recursively to extract characters, starting from the endpoint's first page
- Compute appearances, height and finds species details for each character
- Create table / dictionary of name, species, height and appearances for each character
- Sort list of characters in descending order of appearance and slice to extract the top 10
- Take top 10 most appearances and sorts by height (tallest to shortest)
- Store as  name, species, height, appearances values as fields / records in a CSV file

### Using a custom (helpers) module
fetch_url() - extracts data from endpoint
get_species() - gets name of species from endpoint
produce_csv() - produces csv of the format 'name, species, height, appearances'
get_characters() - fetches all the characters from all endpoint pages
string_to_float() - converts any numeric string to float
find_characters() - produces list of solution after sorting by height


### Assumptions
- 0.0 float for unknown heights
- N/A for no species data
