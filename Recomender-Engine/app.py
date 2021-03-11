# Packages
from flask import Flask, jsonify, request
from flask_cors import CORS
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
import openpyxl
import ast
from more_itertools import flatten
import json


# Load Dataset
global data
data = pd.read_excel('specifications.xlsx', engine='openpyxl')
data.drop([col for col in data.columns if "Unnamed" in col], axis=1, inplace=True)
data['partner'] = data['partner'].fillna('intel')
global data_new
data_new = pd.read_excel('data_new.xlsx', engine = 'openpyxl')

# Axulliary functions
def drop_nan_col(df, threshold): 
    for i in df.columns:
        if (float(df[i].isnull().sum())/df[i].shape[0]) > threshold:
            df = df.drop(i, axis=1) 
    return df

def similarity_algorithm(): 
    results = {}
    for idx, row in data2.iterrows():
        similar_indices = cosine_similarities[idx].argsort()[:-100:-1]
        similar_items = [(cosine_similarities[idx][i], data2['boms_id'][i]) for i in similar_indices]
        results[row['boms_id']] = similar_items[1:]
    return results

def item(id):
    return data2.loc[data2['boms_id'] == id]['name'].tolist()[0].split(' - ')[0]

def recommend(boms_id, num):
    # print("Recommending " + str(num) + " products similar to " + item(boms_id))
    # print("-"*60)
    results = similarity_algorithm()
    recs = results[boms_id][:num]
    recomendations = []
    recomendations_dict = {}
    recomendations_dict['status'] = 200
    for rec in recs:
        recomendations.append((str(rec[1]), item(rec[1])))
        # print("Recommended: " + item(rec[1]) + " (simillarity score: " + str(rec[0]) + ")" )
    recomendations_dict['data'] = [dict(recomendations)]
    return recomendations_dict

def get_boms_id(name, data):
    bom_id = data[data['name'] == name].boms_id.values[0]
    return bom_id 

# Data pre-processing
data2 = drop_nan_col(data, 0.9)
data2['bag of words'] = data2[data2.columns[:]].apply(lambda x: ' '.join(x.dropna().astype(str)),axis=1)
data2['bag of words'] = data2['bag of words'].apply(lambda x: x.lower())

# Machine learning
tf = TfidfVectorizer(analyzer='word', 
                     ngram_range=(1, 1), 
                     min_df=0, 
                     stop_words='english')

tfidf_matrix = tf.fit_transform(data2['bag of words'])

cosine_similarities = linear_kernel(tfidf_matrix, tfidf_matrix)

# API app
app = Flask(__name__)
CORS(app)

## API
## Simillar product
@app.route('/api')
@app.route('/api/recomender/name/<name>', methods = ['GET', 'POST'])
def send_recommenxwdatios_name(name):
    print(name, type(name))
    if name:
        boms_id = get_boms_id(name, data2)
        recomendations = recommend(int(boms_id), 5)
        recomendations['error'] = ''
        return jsonify(recomendations)
    print(recomendations)
    return 'API Not Working'

@app.route('/api/recomender/boms/<boms_id>', methods = ['GET', 'POST'])
def send_recommenxwdatios_boms(boms_id):
    print(boms_id, type(boms_id))
    if boms_id:
        recomendations = recommend(int(boms_id), 5)
        recomendations['error'] = ''
        return jsonify(recomendations)
    print(recomendations)
    return 'API Not Working'

## Popular product
@app.route('/api/recomender/simillar', methods = ['GET', 'POST'])
def send_popular_products():
    f = open("hist.txt", "r")
    data_g = f.read()
    data_g = ast.literal_eval(data_g)
    f.close()
    
    boms = []
    for key, value in data_g.items():
        for k, v in value.items():
            boms.append(v.split()[0])

    current_popular_products = {}
    recommende_popular_items = []
    b = 0
    for items in boms:
        if data2['name'].str.contains(items).any():
            boms_id = get_boms_id(items, data2)
            current_popular_products[str(boms_id)] = items
            recommende_popular_items.append(recommend(int(boms_id), 2))
            b = b + 1
        else:
            boms_id = data_new[data_new['name'] == items].boms_id.values[0]
            current_popular_products[str(boms_id)] = items
    recommended_list = {"Data":[]}

    for i in range (b):
        recommended_list["Data"].append(recommende_popular_items[i]['data'])

    recommender = {}
    recommender['status'] = 200
    b = list(flatten(recommended_list["Data"]))
    
    recommender_list_most_popular = [current_popular_products] + b
    
    final_resut = {}
    for i in recommender_list_most_popular:
        final_resut.update(i)
    recommender['data'] = [final_resut]
    recommender['error'] = ''
    return jsonify(recommender)
    
# Run Server
if __name__ == '__main__':
    app.run(host='0.0.0.0' ,port='9101')
# send_popular_products()
