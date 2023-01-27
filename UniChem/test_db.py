from utils import export_database

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
    export_database(database, id)
