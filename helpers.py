import urllib.request
import urllib.parse
import json
import csv

# use api end point to fetch data + validate url
def fetch_url(endpoint):
    try:
        # Due to mod_security, spoof by opening as browser instead python urllib.
        page = urllib.request.Request(endpoint, headers={'User-Agent': 'Mozilla/5.0'})
        sock = urllib.request.urlopen(page).read()
    except ValueError:
        return {}

    # Convert byte string to JSON
    query_result = json.loads(sock.decode('utf-8'))
    return query_result


# get name of species
def get_species(endpoint):
    species_result = fetch_url(endpoint)
    return species_result.get("name", None)



# Produce a CSV with the following columns: name, species, height, appearances
def produce_csv(results, csv_file="characters.csv"):
    csv_columns = ["name", "species", "height", "appearances"]

    try:
        with open(f'output/{csv_file}', 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
            writer.writeheader()
            for data in results:
                writer.writerow(data)

    except IOError:
        print("I/O error")
        return False

    except TypeError:
        print("TypeError error")
        return False

    print("results csv produced")
    return True


# get all characters who appear in Star Wars films
def get_characters(endpoint):
    query_result = fetch_url(endpoint)

    # root: previous == null, leaf: next == null.
    results = query_result.get("results", [])
    next_endpoint = query_result.get("next", None)

    # recursively check if next node exists and extract results data if so
    if next_endpoint is not None:
        results += get_characters(next_endpoint)

    return results



# convert string to float
def string_to_float(numeric_string):
    height = 0.0

    try:
        height = float(numeric_string)

    except ValueError:
        pass

    return height
