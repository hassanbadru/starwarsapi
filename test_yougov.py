import pytest
import json
from helpers import fetch_url, get_species, produce_csv, get_characters, string_to_float
from yougov import find_characters


with open('testdata/solution_result.json') as solution_json:
    solution_result = json.load(solution_json)

with open('testdata/starship9.json') as starships_json:
    starship_data = json.load(starships_json)

def test_float_conv():
    assert string_to_float("4.6") == 4.6
    assert string_to_float("unknown") == 0.0
    assert string_to_float("bad float string") == 0.0

def test_endpoint():
    assert fetch_url("bad url") == {}
    assert fetch_url("https://swapi.co/api/people/").get("count") == 87
    assert fetch_url("https://swapi.co/api/starships/9/") == starship_data

def test_csv():
    assert produce_csv([{"name": "a", "species": "b", "appearances": 1, "height": 20}], "test.csv") == True
    assert produce_csv([{"name": "a", "species": "b", "appearances": 1, "height": 20}], "test/test.csv") == False
    assert produce_csv(None, "test.csv") == False

def test_species():
    assert get_species("bad url") == None
    assert get_species("https://swapi.co/api/species/1/") == "Human"

def test_solution():
    assert find_characters('bad url') == []
    assert find_characters('https://swapi.co/api/people/') == solution_result
