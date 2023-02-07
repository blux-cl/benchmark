from utils import export_database
import json

if __name__ == '__main__':
    #database = 'zinc'
    #id = 'ZINC000000000053' 
    #'https://zinc15.docking.org/substances/ZINC000000000053/'
    #https://pubs.acs.org/doi/10.1021/acs.jcim.5b00559
    #database = 'bindingdb'
    #id = '26193'
    #database = 'pubchem_tpharma'
    #id = ''
    #database = 'nikkaji'
    #id = ''
    database_name = 'chebi'
    id = '3612'
    database = export_database(database_name, id)

    compound_dict = {}
    compound_dict['chebi'] = database
    with open(f"generated_json/test.json", 'w') as fp:
        json.dump(compound_dict, fp)