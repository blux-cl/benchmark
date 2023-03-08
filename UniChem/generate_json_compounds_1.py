import numpy as np
import json
import pandas as pd
from utils import export_database
from os.path import exists

if __name__ == '__main__':
    
    unichem = pd.read_csv("unichem_master_ids.csv")
    #unichem = pd.read_csv("unichem_master_missing_ids.csv")
    
    for i, compound in enumerate(unichem.iterrows()):
        if i >= 100000 and i < 150000:
            compound_dict = {}
            file_exist = False
            for database_name, id in compound[1].items():
                if database_name == 'cas_rn' or database_name == 'CAS-RN':
                    database_name = 'fda'
                if (type(id) == str) or (type(id) == int and database_name != 'uci') or (type(id) == np.float64 and not np.isnan(id)) or (database_name == 'chebi' and not np.isnan(id)):
                    database = export_database(database_name, id)
                    compound_dict[database_name] = database
                else:
                    if database_name == 'uci':
                        uci = int(id)
                        if exists(f"generated_json_2/{uci}.json"):
                            file_exist = True
                            break
            if not file_exist:
                with open(f"generated_json_2/{uci}.json", 'w') as fp:
                    json.dump(compound_dict, fp)
        if i == 150000:
            break
