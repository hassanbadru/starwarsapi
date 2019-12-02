import operator
from helpers import get_species, produce_csv, get_characters, string_to_float

# species loading cache
# N/A for no species
# 0.0 float for unknown heights
# Sort characters by appearances, then by height in descending order (i.e., tallest first)
def find_characters(endpoint):
    results = get_characters(endpoint)
    new_results = []

    for r in results:
        name = r.get("name")
        species = 'N/A'

        species_endpoints = r.get("species")
        if len(species_endpoints) > 0:
            species = get_species(species_endpoints[0])

        url = r.get("url")
        appearances = len(r.get("films"))
        height = r.get("height")

        new_results.append({"name": name, "species": species,
                            "appearances": appearances, "height": string_to_float(height)})


    new_results.sort(key = operator.itemgetter('appearances', 'height'), reverse=True)
    return sorted(new_results[:10], key = operator.itemgetter('height'), reverse=True)




results = find_characters('https://swapi.co/api/people/')
if results:
    produce_csv(results)



#4 - Send the CSV to httpbin.org
#5 - Create automated tests that validate your code
# pip install pytest
