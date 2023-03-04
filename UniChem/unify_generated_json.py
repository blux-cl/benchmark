import json
import pandas as pd
from pathlib import Path
import logging

logging.basicConfig(filename='unify.log',
                    filemode='a',
                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                    datefmt='%H:%M:%S', level=logging.DEBUG)

pathlist = Path('generated_json/').rglob('*.json')
data = []
i = 0
for n, file in enumerate(pathlist):
    with open(file) as f:
        file_data = json.load(f)
        file_data['uci'] = file.stem
    logging.info(f"{n} - {str(file)} processed")
    data.append(file_data)

    if n % 20000 == 0 and n != 0:
        with open(f"compounds_{i}_{n}.json", 'w') as fp:
            json.dump(data, fp)
        data = []
        i = n + 1

i = i + 20000
with open(f"compounds_{i}_{n}.json", 'w') as fp:
    json.dump(data, fp)