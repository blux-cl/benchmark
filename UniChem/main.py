import numpy as np
import json
import pandas as pd
from utils import export_database

if __name__ == '__main__':
    
    unichem = pd.read_csv("unichem_master_ids.csv")
    
    compound = unichem.loc[1]
    compound_dict = {}
    
    for database_name, id in compound.items():
        if (type(id) == str) or (type(id) == np.float64 and not np.isnan(id)):
            database = export_database(database_name, id)
            compound_dict[database_name] = database
        else:
            if type(id) == np.int64:
                uci = id
            
        with open(f'{uci}.json', 'w') as fp:
            json.dump(compound_dict, fp)