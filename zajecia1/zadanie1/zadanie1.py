#! /bin/python3

import pandas as pd

flats = pd.read_scv('train/train.tsv', sep = '\t', 
        names = ['price', 'isNew', 'rooms', 'floor', 'location', 'sqrMeters']

flts_mean = flats['price'].pd.mean()

print(flats_mean)

