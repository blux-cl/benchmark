import json
import pandas as pd
from pathlib import Path

pathlist = Path('generated_json/').rglob('*.json')
data = []

for file in pathlist:
    with open(file) as f:
        file_data = json.load(f)
        file_data['uci'] = file.stem
    data.append(file_data)

with open(f"compounds.json", 'w') as fp:
    json.dump(data, fp)
