import pandas as pd 

df = pd.read_csv('icd10cm_codes_2023.txt', 
                 sep='\t', 
                 names=['code'],
                 header=None)

## if two or more white spaces, push rest of string to next column
df = df.code.str.split(' ', expand=True)

## rename column 0 to count, column 1 to code
df.rename(columns={0: 'code'}, inplace=True)

df['code']

## merge all other columns into one column
df['description'] = df[df.columns[2:]].apply(lambda x: ' '.join(x.dropna().astype(str)), axis=1)

## drop all columns except code and description
df = df[['code', 'description']]

## from description, remove all white space that is not a space
df['description'] = df['description'].str.replace('\s+', ' ', regex=True)

df.to_csv('icd10cm_codes_2023.csv', index=False)
