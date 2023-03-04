import pandas as pd
from chembl_webresource_client.new_client import new_client
from libchebipy import ChebiEntity
import pubchempy as pcp
from Bio.KEGG import REST
import logging

s = pd.read_csv("SCOGS_filtered.csv")
f = pd.read_csv("food_substances_filtered.csv")
i = pd.read_csv("indirect_additives_filtered.csv")


logging.basicConfig(filename='logs/utils.log',
                    filemode='a',
                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                    datefmt='%H:%M:%S', level=logging.DEBUG)


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
    df_output = df_output.rename(columns={col: col.lower()
                                          for col in df_output.columns}
                                 )
    return df_output


def export_chebi(id):
    columns = ['id', 'name', 'names', 'charge', 'comments', 'compound_origins', 'created_by', 'db_accessions',
               'definition', 'formula', 'formulae', 'inchi', 'inchi_key', 'incomings', 'mass',
               'modified_on', 'mol', 'outgoings', 'references', 'parent_id',
               'smiles', 'source', 'stars']

    df = pd.DataFrame([], columns=columns)
    if isinstance(id, float):
        id = str(int(id))
    chebi_entity = ChebiEntity(chebi_id=id)
    name = chebi_entity.get_name()
    names = chebi_entity.get_names()
    names = [{"name": n.get_name(), "type": n.get_type(
    ), "source": n.get_source(), "language": n.get_language()} for n in names]
    charge = chebi_entity.get_charge()
    comments = chebi_entity.get_comments()
    comments = [{"datatype_id": c.get_datatype_id(), "datatype": c.get_datatype(),
                 "text": c.get_text(), "created_on": c.get_created_on()} for c in comments]
    compound_origins = chebi_entity.get_compound_origins()
    compound_origins = [{"species_text": c.get_species_text(), "source_accession": c.get_source_accession(
    ), "source_type": c.get_source_type(), "component_text": c.get_component_text(), "source_type": c.get_source_type(),
        "source_accession": c.__dict__['_CompoundOrigin__source_accession'], "comments": c.get_comments()} for c in compound_origins]
    created_by = chebi_entity.get_created_by()
    db_accessions = chebi_entity.get_database_accessions()
    db_accessions = [{"type": d.get_type(), "accession_number": d.get_accession_number(
    ), "source": d.get_source()} for d in db_accessions]
    definition = chebi_entity.get_definition()
    formula = chebi_entity.get_formula()
    formulae = chebi_entity.get_formulae()
    formulae = [{"formula": f.get_formula(), "source": f.get_source()}
                for f in formulae]
    inchi = chebi_entity.get_inchi()
    inchi_key = chebi_entity.get_inchi_key()
    incomings = chebi_entity.get_incomings()
    incomings = [{"type": i.get_type(), "target_chebi_id": i.get_target_chebi_id(
    ), "status": i.__dict__['_Relation__status']} for i in incomings]
    mass = chebi_entity.get_mass()
    modified_on = chebi_entity.get_modified_on().strftime("%m/%d/%Y")
    mol = chebi_entity.get_mol()
    outgoings = chebi_entity.get_outgoings()
    outgoings = [{"type": o.get_type(), "target_chebi_id": o.get_target_chebi_id(
    ), "status": o.__dict__['_Relation__status']} for o in outgoings]
    references = chebi_entity.get_references()
    references = [{"reference_id": r.get_reference_id(), "reference_db_name": r.get__reference_db_name(
    ), "location_in_ref": r.get_location_in_ref(), "reference_name": r.get_reference_name()} for r in references]
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


def export_fda(id):
    df = pd.DataFrame()
    found_s = s[s['cas_rn'] == id]
    found_s = found_s[found_s['syns'].apply(lambda x: isinstance(x, str))]
    found_f = f[f['cas_rn'] == id]
    found_i = i[i['cas_rn'] == id]
    df = pd.concat([found_s, found_f, found_i])
    try:
        df = df.groupby('cas_rn', as_index=False).agg({
            'cas_rn': 'first',
            'substance': ', '.join,
            'report_num': 'first',
            'syns': ', '.join,
            'conclusion': 'first',
            'regs': 'first',
            'used_for': 'first',
            'FEMA No': 'first',
            'GRAS Pub No': 'first',
            'Most Recent GRAS Pub Update': 'first',
            'FEMA status': 'first',
            'JECFA Flavor Number': 'first',
        })
    except KeyError:
        if 'conclusion' in df.columns:
            df = df.groupby('cas_rn', as_index=False).agg({
                'cas_rn': 'first',
                'substance': ', '.join,
                'report_num': 'first',
                'syns': ', '.join,
                'conclusion': 'first',
                'regs': 'first',
                'used_for': 'first',
                'FEMA No': 'first',
                'GRAS Pub No': 'first',
                'Most Recent GRAS Pub Update': 'first',
                'FEMA status': 'first',
                'JECFA Flavor Number': 'first',
            })
        else:
            return df
    return df


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
    'probes_and_drugs': export_probes_and_drugs,
    'fda': export_fda,
}


def export_database(database_name, id):
    if database_name == 'cas_rn' or database_name == 'CAS-RN':
        database_name = 'fda'
    try:
        database_df = DATABASE_DICT[database_name](id)
        logging.info(f"Processing {database_name} -  {id}")
        d = database_df.to_dict()
        logging.info(f"{database_name} -  {id} processed correctly")
        return d
    except AttributeError:
        logging.warning(f"{database_name} not implemented yet")
    except Exception as e:
        logging.error(f"{e} - {database_name} -  {id}")
