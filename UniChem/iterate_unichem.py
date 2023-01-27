import requests
import json
import time
import pandas as pd
from tqdm import tqdm

unichem_ids = list(range(20000000))
unichem_ids = [str(x) for x in unichem_ids]

url = "https://www.ebi.ac.uk/unichem/api/v1/sources"
payload = ""
response = requests.request("GET", url, data=payload)

res = json.loads(response.text)
sources = [sources['name'] for sources in res['sources']]
sources.insert(0, 'uci')

start = time.time()
url = "https://www.ebi.ac.uk/unichem/api/v1/compounds"
headers = {"Content-Type": "application/json"}

correct, incorrect = [], []
df = pd.DataFrame([], columns=sources)
min_idx = 500000
max_idx = 1000000
for unichem_id in tqdm(unichem_ids[min_idx:max_idx]):
    data = {
      "compound": unichem_id,
      "type": "uci"
    }
    try:
        response = requests.post(url, json=data, headers = headers)
        res = json.loads(response.text)
        compounds = res['compounds']
        if res['response'] != 'Not found':
            sources_dict = dict.fromkeys(sources, '')
            sources_dict['uci'] = unichem_id
            for c in compounds:
                compound_sources = c['sources']
                for s in compound_sources:
                    sources_dict[s['shortName']] = s['compoundId']
            correct.append(unichem_id)
            df_dictionary = pd.DataFrame([sources_dict])
            df = pd.concat([df, df_dictionary], ignore_index=True)
            df.to_csv(f'unichem_master_ids[{min_idx}-{max_idx}].csv', index=None)
        else:
            incorrect.append(unichem_id)
    except Exception as e:
        print('EXCEPTION: ', e)
        incorrect.append(unichem_id)