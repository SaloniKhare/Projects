import pandas as pd
import numpy as np

pd.set_option('display.max_columns', 10)

data = pd.read_csv('Bengaluru_House_Data.csv')
#print(data.head())
#print(data.shape)
#print(data.info())
'''for column in data.columns:
  print(data[column].value_counts())
  print("*"*20)'''
#print(data.isna().sum())
data.drop(columns=['area_type','availability','society','balcony'],inplace=True)
#print(data.describe())

#*Null removal for location*
#print(data['location'].value_counts())
data['location'] = data['location'].fillna('Whitefield')

#*Null removal for size*
#print(data['size'].value_counts())
data['size'] = data['size'].fillna('2 BHK')

#*Null removal for bathroom*
#print(data['bath'].value_counts())
data['bath'] = data['bath'].fillna(data['bath'].median())

data['bhk'] = data['size'].str.split().str.get(0).astype(int)
 
def convertRange(x):
  temp = x.split('-')
  if len(temp) == 2:
    return (float(temp[0]) + float(temp[1]))/2
  try:
    return float(x)
  except:
    return None
  
data['total_sqft'] = data['total_sqft'].apply(convertRange)
data['price_per_sqft'] = data['price']*100000 / data['total_sqft']

#handling locations
data['location'] = data['location'].apply(lambda x : x.strip())
location_counts=data['location'].value_counts()
location_counts_less_10=location_counts[location_counts<=10]
data['location']=data['location'].apply(lambda x : 'other' if x in location_counts_less_10 else x)

#handling sqft
data = data[((data['total_sqft']/data['bhk']) >=300)]

def bhk_outlier_removal(df):
  exclude_indices = np.array([])
  for location, location_df in df.groupby('location'):
    bhk_stats={}
    for bhk, bhk_df in location_df.groupby('bhk'):
      bhk_stats[bhk] ={
        'mean':np.mean(bhk_df.price_per_sqft),
        'std':np.std(bhk_df.price_per_sqft),
        'count': bhk_df.shape[0]
        
      }
    for bhk ,bhk_df in location_df.groupby('bhk'):
      stats = bhk_stats.get(bhk-1)
      if stats and stats['count']>5:
        exclude_indices = np.append(exclude_indices,bhk_df[bhk_df.price_per_sqft<(stats['mean'])].index.values)
  return df.drop(exclude_indices,axis='index')

data = bhk_outlier_removal(data)

data.drop(columns=['price_per_sqft','size'],inplace=True)
data.reset_index(drop=True, inplace=True)

data.to_csv('Cleaned_data.csv')
print(data.info())
X=data.drop(columns=['price'])
Y=data['price']
