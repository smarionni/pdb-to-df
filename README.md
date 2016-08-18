# `pdb_to_df()`

`pdb_to_df` is a convenience function for loading `ATOM` data from Protein Data Bank (PDB) format files as a pandas `DataFrame`. After constantly rewriting different versions of the same code to load PDB files and filter for the relevant lines, I wrote a function that would put everything into a data frame for easy querying. Now, if you just wanted the coordinates for all the alpha-carbons from chain A of a protein complex, one line of code would yield it.

```python
atoms = pdb_to_df('4i6j.pdb')
coords = atoms[(atoms['chain'] == 'A') & (atoms['name'] == 'CA')][['x', 'y', 'z']]
```

## Installation

Just copy and paste it into a script. I don't think it's worth packaging up, but if you're working with PDB files it's convenient to have around.
