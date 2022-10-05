# ChEBI fields

1. ID: ChEBI id
2. Name: The name for an entity recommended for use by the biological community
3. Names: Returns all alternative names for an entity that either have been used in EBI or external sources or have been devised by the curators based on recommendations of IUPAC, NC-IUBMB or their associated bodies
4. Charge: Sum of all the positive and negative charges shown in the structure. For ions the magnitude of the charge is given in arabic numerals preceded by the sign of the charge. For neutral molecules the charge is indicated as a numerical zero.
5. Comments:
6. CompoundOrigins: Provides a list of origins for a given ChEBI entity
7. Author: If an entry is present by virtue of its having been submitted via the ChEBI Submissions Tool, the name of the submitter is displayed here (unless the submitter has elected to remain anonymous).
8. Database Accessions: Direct links to the entries for an entity in the databases cited
9. Definition: A short verbal definition is included in some entries
10. Formula: formula and formula source
11. InChI: non-proprietary identifier for chemical substances that can be used in printed andelectronic data sources thus enabling easier linking of diverse data compilations. It expresses chemical structures in terms of atomic connectivity, tautomeric state, isotopes, stereochemistry and electronic charge in order to produce a sequence of machine-readable characters unique to the respective molecule
12. InchiKey: The InChIKey is a 25-character hashed version of the full InChI, designed to allow for easy web searches of chemical compounds.
13. Outgoings: ChEBI is an ontology, and as such maintains relations between chemical entities.
14. Incomings: Similar to getOutgoings(), getIncomings() returns a List of Relation objects stating relations in which the ChEBI entity is the object of the relationship
15. Mass: Returns the average mass. The relative masses are calculated from tables of relative atomic masses
    (atomic weights) published by IUPAC.
16. Last Modification Date: Indicating the date that the entity was last modified by an annotator.
17. Mol: ChEBI stores the two-dimensional or three-dimensional structural diagrams as connection tables in MDL molfile format
18. References: Returns a list of textual references to external resources, covering references to the given ChEBI entity in resources such as BRENDA, UniProt and in patents.
19. Parent_ID: Some ChEBI entities have subsequently been found to be duplicates. If a given entity is a duplicate, it will
    have a parent id that maps to a parent entity that is considered the primary id for a given set of duplicates.
20. SMILES (Simplified Molecular Input Line Entry System) is a simple but comprehensive chemical line
    notation, that specifically represents a valence model of a molecule and is widely used as a data
    exchange format.
21. Source: Returns the source of the ChEBI entity
22. Star: Entries that have been manually annotated by the ChEBI team are indicated by the presence of a '3-star' symbol. This is shown on the main display screen for an entity and on the search results page. An absence of a '3-star' symbol indicates that a third party has manually annotated the entity, or  (occasionally) that it has been marked as deleted or obsolete.
