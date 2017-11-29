import os
import pandas as pd

data_dir = '/home/tracek/Data/Rudzik/'
datafile_name = 'Sample_E_410_000261_S1.realigned.freebayes.norm.streamann2.vcf.tab'
mygenes_name = 'target_Genes.csv'
filter_column = 'EFF____GENE'

data_path = os.path.join(data_dir, datafile_name)
mygenes_path = os.path.join(data_dir, mygenes_name)

df = pd.read_csv(data_path, sep='\t')
print('Total records: {}'.format(len(df)))

# Remove all entries that have no value in 'filter_column'
df = df[pd.notnull(df[filter_column])]
print('After removing nulls (entries without value in {}): {}'.format(filter_column, len(df)))

# Read file with genes to filter
with open(mygenes_path) as f:
    # Make a list of the genes to filter e.g. [MAC, EYS, LCA5, ...]
    genes = f.read().splitlines()

# Select the entries in which value in filter_column matches the created 'genes' list
filtered = df[df[filter_column].isin(genes)]
print('After filtering for genes in {}: {}'.format(datafile_name, len(filtered)))

# Save to file
filtered.to_csv(os.path.join(data_dir, 'filtered.tsv'), index=False, sep='\t')
