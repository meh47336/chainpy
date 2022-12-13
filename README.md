# chainpy
Reformat AlphaFold on Summit heterodimer PDBs


When running AlphaFold multimer (specifically heterodimeric) predictions on Summit, the PDB files are not in a useful format. Particularly, both proteins in the complex will be listed as the same chain (ID "A") and the numbering of the second protein (what should be chain ID "B") begins after a chain break of 200 (for example, if Chain A is 100 residues in length, Chain B will begin being numbered as residue 300).

Running chainpy.py using the bash launch script will edit the AlphaFold multimer on Summit PDBs so that the heterodimer PDBs contain two chains: "A" and "B" where the first residue of Chain "B" is numbered as residue 1.

Chainpy runs using python3.

ChainA variable in Chainpy must be changed so that it is the length of the first protein in the dimer (or what you want to be considered Chain "A").

The parallelized bash launch script may need to be modified depending on how your directories are organized.
