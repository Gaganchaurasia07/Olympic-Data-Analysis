
# preprocess.py
import pandas as pd
import pickle

def preprocess(df, region_df):
    df = df[df['Season'] == 'Summer']
    df = df.merge(region_df, on='NOC', how='left')
    df.drop_duplicates(inplace=True)
    df = pd.concat([df, pd.get_dummies(df['Medal'])], axis=1)
    return df

# Load the data
df = pd.read_csv('athlete_events.csv')
region_df = pd.read_csv('noc_regions.csv')

# Preprocess the data
df = preprocess(df, region_df)

# Save the preprocessed data as a pickle file
with open('data.pkl', 'wb') as f:
    pickle.dump(df, f)


