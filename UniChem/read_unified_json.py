import gzip
import json

# Open the gzipped JSON file
with gzip.open("compounds.json.gz", "rb") as f:
    # Load the JSON data from the file object
    json_data = json.load(f)

# Print the first 10 items in the JSON data
for key, value in list(json_data.items())[:10]:
    print(key, value)
