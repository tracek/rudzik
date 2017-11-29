import os
import pandas as pd

data_dir = '/home/tracek/Data/Rudzik/'
datafile_name = 'Sample_E_410_000261_S1.realigned.freebayes.norm.streamann2.vcf.tab'
data_path = os.path.join(data_dir, datafile_name)
mygenes_name = 'target_Genes.csv'
mygenes_path = os.path.join(data_dir, mygenes_name)

df = pd.read_csv(data_path, sep='\t')
print('Total records: {}'.format(len(df)))

filter_column = 'EFF____GENE'
df = df[pd.notnull(df[filter_column])]
print('After removing nulls in {}: {}'.format(filter_column, len(df)))

with open(mygenes_path) as f:
    genes = f.read().splitlines()

filtered = df[df[filter_column].isin(genes)]
print('After filtering for genes in {}: {}'.format(datafile_name, len(filtered)))

filtered.to_csv(os.path.join(data_dir, 'filtered.tsv'), index=False, sep='\t')

#print(df[filter_column])