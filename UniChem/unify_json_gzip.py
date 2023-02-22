import json
import os
import gzip
import logging

logging.basicConfig(filename='unify.log',
                    filemode='a',
                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                    datefmt='%H:%M:%S', level=logging.DEBUG)

# Set the directory path where the JSON files are located
directory = "generated_json/"

# Create an empty list to store the data from each JSON file
json_data = []

# Loop through each file in the directory
for n, filename in enumerate(os.listdir(directory)):
    if filename.endswith(".json"):
        with open(os.path.join(directory, filename), "r") as f:
            data = json.load(f)
            data['uci'] = filename.split('.')[0]
            json_data.append(data)
    logging.info(f"{n} - {filename} processed")

# Write the merged data to a new JSON file
with gzip.open("compounds.json.gz", "wb") as f:
    f.write(json.dumps(json_data).encode())
logging.info("compounds.json.gz file generated")


