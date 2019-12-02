import operator
from helpers import get_species, produce_csv, get_characters, string_to_float

# Sort characters by appearances, then by height in descending order (i.e., tallest first)
def find_characters(endpoint):
    results = get_characters(endpoint)
    new_results = []
    species_cache = {} # use cache of loading species details

    for r in results:
        name = r.get("name")

        species = 'N/A'
        species_endpoints = r.get("species")

        if species_endpoints and len(species_endpoints) > 0:
            species_endpoints = species_endpoints[0]
            # check if species exists in cache, if so, use name value instead
            species = species_cache.get(species_endpoints, None)
            if not species:
                species = get_species(species_endpoints)
                species_cache[species_endpoints] = species



        appearances = len(r.get("films"))
        height = r.get("height")

        new_results.append({"name": name, "species": species,
                            "appearances": appearances, "height": string_to_float(height)})


    new_results.sort(key = operator.itemgetter('appearances', 'height'), reverse=True)
    return sorted(new_results[:10], key = operator.itemgetter('height'), reverse=True)




results = find_characters('https://swapi.co/api/people/')
# if result exists, produce csv of result
if results:
    produce_csv(results)
