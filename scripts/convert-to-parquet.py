# this script will convert the original data to parquet

import polars as pl

train = pl.read_csv('data/train.csv')
train_xtra = pl.read_csv('data/training_extra.csv')
test = pl.read_csv('data/test.csv')

# write out to parquet
train.write_parquet('data/train.parquet')
train_xtra.write_parquet('data/training_extra.parquet')
test.write_parquet('data/test.parquet')