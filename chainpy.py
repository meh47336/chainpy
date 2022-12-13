'''
12-12-2022
Much thanks to pippo1980 at StackOverflow for assisting in
the renaming of the second chain.
'''

import os
from Bio.PDB import PDBIO, PDBParser
from Bio.PDB.Chain import Chain
from Bio.PDB.Model import Model
from Bio.PDB.Structure import Structure
from glob import glob


dirPath = os.getcwd()
pdbFiles = glob("*.pdb")
pdbString = str(pdbFiles).replace('[','').replace(']','').replace("'", "")
dirName = os.path.basename(dirPath)
fileName = os.path.basename(pdbString).replace('[','').replace(']','').replace("'", "")
fileLength = len(fileName)
fileString = fileName[:fileLength - 2]
fileNameNoPDB = fileName[:fileLength - 4]


io = PDBIO()

structure = PDBParser(QUIET=True).get_structure(dirPath, pdbString)
model = structure[0]
chainOriginal = model["A"]


##Change Chain A length accordingly
chainA = 275
residues_chainB = []

for model in structure:
    for chains in model:
        for residues in chains:
            if residues.get_id()[1] > chainA:
                residues_chainB.append(residues)

gap = residues_chainB[0].get_full_id()[3][1] - 1

##Remove chainB residues from original PDB
for model in structure:
    for chain in model:
        [chain.detach_child(res.get_id()) for res in residues_chainB]


##Create chainB
chainB = Chain("B")


##Add residues to new chain with id "B"
for res in residues_chainB:
    chainB.add(res)

for residues in chainB:
    residues.id = (residues.id[0], residues.id[1] - gap, residues.id[2])


##Make empty structure
new_structure = Structure("1")
new_model = Model("1")

new_structure.add(new_model)
new_model.add(model["A"])
new_model.add(chainB)


##Save new structure that contains original chain A and renumbered chain B
io.set_structure(new_model)
savename = "{}_edit.pdb".format(fileNameNoPDB)
io.save(savename, write_end = False, preserve_atom_numbering = True)


##Exit and rerun with bash launcher
exit()
