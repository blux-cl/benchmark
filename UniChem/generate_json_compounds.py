import numpy as np
import json
import pandas as pd
from utils import export_database
from os.path import exists

if __name__ == '__main__':
    
    unichem = pd.read_csv("unichem_master_ids.csv")
    #unichem = pd.read_csv("unichem_master_missing_ids.csv")
    
    compound_dict = {}
    for compound in unichem.iterrows():
        file_exist = False
        for database_name, id in compound[1].items():
            if database_name == 'cas_rn' or database_name == 'CAS-RN':
                database_name = 'fda'
            if (type(id) == str) or (type(id) == np.float64 and not np.isnan(id)) or (database_name == 'chebi' and not np.isnan(id)):
                database = export_database(database_name, id)
                compound_dict[database_name] = database
            else:
                if database_name == 'uci':
                    uci = int(id)
                    if exists(f"generated_json/{uci}.json"):
                        file_exist = True
                        break
        if not file_exist:
            with open(f"generated_json/{uci}.json", 'w') as fp:
                json.dump(compound_dict, fp)