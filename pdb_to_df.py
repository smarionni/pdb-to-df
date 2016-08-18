import pandas as pd
import numpy as np

def pdb_to_df(fname):
    with open(fname, 'r') as PDBfile:
        PDBlines = PDBfile.read().splitlines()
        PDBlines = filter(lambda x: x[0:4] == 'ATOM', PDBlines)

    ATOMdata = [[x[0:6], x[6:11], x[12:16], x[16:17], x[17:20], x[21:22],
            x[22:26], x[26:27], x[30:38], x[38:46], x[46:54], x[54:60],
            x[60:66], x[76:78], x[78:80]] for x in PDBlines]

    headers = ['Record', 'serial', 'name', 'altLoc', 'Resn',
            'chainID', 'resSeq', 'iCode', 'x', 'y', 'z', 'occupancy',
            'tempFactor', 'element', 'charge']

    ATOMdata = [[s.strip() for s in inner] for inner in ATOMdata]
    df = pd.DataFrame(ATOMdata, columns=headers)

    # Convert numeric columns to numeric dtype
    num_cols = ['serial', 'resSeq', 'x', 'y', 'z', 'occupancy', 'tempFactor']
    df[num_cols] = df[num_cols].apply(pd.to_numeric)

    df = df.set_index(df['serial'].values)
    return df
