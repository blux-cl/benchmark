import pandas as pd
import requests
import json

url = "https://www.ebi.ac.uk/unichem/api/v1/compounds"
headers = {"Content-Type": "application/json"}

with_error = []

d = pd.DataFrame([])
unichem_ids = list(range(500000))
unichem_ids = [str(x) for x in unichem_ids]
for id in unichem_ids:
    data = {
      "compound": id,
      "type": "uci"
    }
    response = requests.post(url, json=data, headers = headers)
    res = json.loads(response.text)
    try:
        inchi_key = res['compounds'][0]['standardInchiKey']
        pubchem_url = f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/inchikey/{inchi_key}/property/IUPACName,Title/json"
        r = requests.post(pubchem_url, timeout=20)
        r = json.loads(r.text)['PropertyTable']['Properties']
        iupac_name = r[-1]['IUPACName']
        common_name = r[-1]['Title']
    except KeyError:
        print("KeyError", id, inchi_key)
        try:
            if 'Title' not in r.keys():
                print("Title is not on response")
                common_name = ''
            if 'IUPACName' not in r.keys():
                print("IUPACName is not on response")
                iupac_name = ''
        except Exception as e:
            iupac_name = ''
            common_name = ''
            print("Not found")
    except requests.exceptions.ConnectionError as e:
        print("ConnectionError", id, inchi_key)
        iupac_name = ''
        common_name = ''
        with_error.append(id)
    except Exception as e:
        print("exc", id, e, inchi_key)
        with_error.append(id)
    data = pd.DataFrame({
        'uci_id': id,
        'common_name': common_name,
        'iupac_name' : iupac_name
    }, index=[0])
    d = pd.concat([d, data])

d.to_csv('uci_id_names.csv', index=False)
    
wrong_ids = {'uci_id': with_error}  
df = pd.DataFrame(wrong_ids)
df.to_csv('with_error.csv') 