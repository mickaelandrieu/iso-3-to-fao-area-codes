import pandas as pd


tables = pd.read_html('https://unstats.un.org/unsd/methodology/m49/')

tables[0].to_csv('country_codes.csv', index=False)
