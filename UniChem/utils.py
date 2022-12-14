import pandas as pd
from chembl_webresource_client.new_client import new_client
from libchebipy import ChebiEntity
import pubchempy as pcp
from Bio.KEGG import REST


def export_chembl(id):
    molecule = new_client.molecule
    mols = molecule.filter(molecule_chembl_id__in=id)
    df = pd.DataFrame(mols)
    return df


def export_drugbank(id):
    pass


def export_pdb(id):
    pass


def export_gtopdb(id):
    pass


def export_pubchem_dotf(id):
    pass


def export_kegg_ligand(id):
    kegg_output = REST.kegg_get(id).read()
    results = {}
    for line in kegg_output.split('\n'):
        splits = line.split()
        if not line.startswith(' '):    
            if len(splits) > 0:
                key = splits[0]
                value = ' '.join(splits[1:])
                results[key] = value
        else:
            results[key] += ' '.join(splits)
    df_output = (pd.DataFrame(results, index=[id])
                    .drop("///", axis=1)
    )
    df_output = df_output.rename(columns=
                                 {col: col.lower() for col in df_output.columns}
                                 )
    return df_output


def export_chebi(id):
    columns = ['id', 'name', 'names', 'charge', 'comments', 'compound_origins', 'created_by', 'db_accessions',
        'definition', 'formula', 'formulae', 'inchi', 'inchi_key', 'incomings', 'mass',
        'modified_on', 'mol', 'outgoings', 'references', 'parent_id',
        'smiles', 'source', 'stars'] 

    df = pd.DataFrame([], columns =columns)

    chebi_entity = ChebiEntity(chebi_id=id)
    name = chebi_entity.get_name()
    names = chebi_entity.get_names()
    charge = chebi_entity.get_charge()
    comments = chebi_entity.get_comments()
    compound_origins = chebi_entity.get_compound_origins()
    created_by = chebi_entity.get_created_by()
    db_accessions = chebi_entity.get_database_accessions()
    definition = chebi_entity.get_definition()
    formula = chebi_entity.get_formula()
    formulae = chebi_entity.get_formulae()
    inchi = chebi_entity.get_inchi()
    inchi_key = chebi_entity.get_inchi_key()
    incomings = chebi_entity.get_incomings()
    mass = chebi_entity.get_mass()
    modified_on = chebi_entity.get_modified_on()
    mol = chebi_entity.get_mol()
    outgoings = chebi_entity.get_outgoings()
    references = chebi_entity.get_references()
    parent_id = chebi_entity.get_parent_id()
    smiles = chebi_entity.get_smiles()
    source = chebi_entity.get_source()
    stars = chebi_entity.get_star()
    row = [id, name, names, charge, comments, compound_origins, created_by, db_accessions, definition,
    formula, formulae, inchi, inchi_key, incomings, mass, modified_on, mol, outgoings,
    references, parent_id, smiles, source, stars]
    df.loc[len(df)] = row
    return df

def export_nih_ncc(id):
    pass

def export_zinc(id):
    pass

def export_emolecules(id):
    pass

def export_atlas(id):
    pass

def export_fdasrs(id):
    pass

def export_surechembl(id):
    pass

def export_pharmgkb(id):
    pass

def export_hmdb(id):
    pass

def export_selleck(id):
    pass

def export_pubchem_tpharma(id):
    pass

def export_pubchem(id):
    c = pcp.Compound.from_cid(int(id))
    df = pcp.compounds_to_frame(c)
    return df

def export_mcule(id):
    pass

def export_nmrshiftdb2(id):
    pass

def export_lincs(id):
    pass

def export_actor(id):
    pass

def export_recon(id):
    pass

def export_molport(id):
    pass

def export_nikkaji(id):
    pass

def export_bindingdb(id):
    pass

def export_comptox(id):
    pass

def export_lipidmaps(id):
    pass

def export_drugcentral(id):
    pass

def export_carotenoiddb(id):
    pass

def export_metabolights(id):
    pass

def export_brenda(id):
    pass

def export_rhea(id):
    pass

def export_chemicalbook(id):
    pass

def export_swisslipids(id):
    pass

def export_dailymed(id):
    pass

def export_clinicaltrials(id):
    pass

def export_rxnorm(id):
    pass

def export_MedChemExpress(id):
    pass

def export_probes_and_drugs(id):
    pass

DATABASE_DICT = {
    'chembl': export_chembl,
    'drugbank': export_drugbank,
    'pdb': export_pdb,
    'gtopdb': export_gtopdb,
    'pubchem_dotf': export_pubchem_dotf,
    'kegg_ligand': export_kegg_ligand,
    'chebi': export_chebi,
    'nih_ncc': export_nih_ncc,
    'zinc': export_zinc,
    'emolecules': export_emolecules,
    'atlas': export_atlas,
    'fdasrs': export_fdasrs,
    'surechembl': export_surechembl,
    'pharmgkb': export_pharmgkb,
    'hmdb': export_hmdb,
    'selleck': export_selleck,
    'pubchem_tpharma': export_pubchem_tpharma,
    'pubchem': export_pubchem,
    'mcule': export_mcule,
    'nmrshiftdb2': export_nmrshiftdb2,
    'lincs': export_lincs,
    'actor': export_actor,
    'recon': export_recon,
    'molport': export_molport,
    'nikkaji': export_nikkaji,
    'bindingdb': export_bindingdb,
    'comptox': export_comptox,
    'lipidmaps': export_lipidmaps,
    'drugcentral': export_drugcentral,
    'carotenoiddb': export_carotenoiddb,
    'metabolights': export_metabolights,
    'brenda': export_brenda,
    'rhea': export_rhea,
    'chemicalbook': export_chemicalbook,
    'swisslipids': export_swisslipids,
    'dailymed': export_dailymed,
    'clinicaltrials': export_clinicaltrials,
    'rxnorm': export_rxnorm,
    'MedChemExpress': export_MedChemExpress,
    'probes_and_drugs': export_probes_and_drugs
}

def export_database(database_name, id):
    database_df = DATABASE_DICT[database_name](id)
    try:
        return database_df.to_dict()
    except Exception as e:
        print(e, database_name, id)
