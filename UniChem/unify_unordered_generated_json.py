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
with open(f"compounds_{i}_{n}.json", 'w') as fp:
    json.dump(data, fp)