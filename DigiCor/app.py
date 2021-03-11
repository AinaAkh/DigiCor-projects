from flask import Flask, request, jsonify, redirect
from main import crawler, database
from flask import send_file
from flask_cors import CORS
import flask_excel as excel
import pandas as pd
import openpyxl
import json
import os
import glob

# Init app
app = Flask(__name__)
CORS(app)

def run_crawler():
    crawler_status = crawler()
    return jsonify(crawler_status)

# Crawler API
@app.route('/api')
@app.route('/api/crawler', methods=['GET'])
def get_crawler():
    try:
        data = run_crawler()
        return data
    except ValueError:
        return 'error'

# Database API
@app.route('/api/database', methods=['GET'])
def get_database():
    database_status = database()
    print('Database Working', database_status)
    return jsonify(database_status)

@app.route('/api/download', methods=['GET'])
def download_file():
    PATH = 'DigiCor/final files/specifications.xlsx'
    print(PATH)
    # return ({'Path': PATH })
    return send_file(PATH, attachment_filename = 'specifications.xlsx', as_attachment=True, cache_timeout = 0)

@app.route("/api/upload", methods=['GET', 'POST'])
def upload_file():
    try: 
        if request.method == 'POST':
            print(request.files['file'])
            file = request.files['file']
            data = pd.read_excel(file, engine = 'openpyxl')
            data.drop([col for col in data.columns if "Unnamed" in col], axis=1, inplace=True)
            data.to_excel('final files/specifications.xlsx')
            status = 200
            data = json.loads(data.to_json(orient='records'))
            error = ''
            # return ({'status': status, 'data': data, 'error': error})
            return redirect('http://192.168.15.113:3000')
    
    except ValueError:
        return ({"status": 500, 'data': '', 'error': ValueError})

# Run Server
if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5001', debug=True)