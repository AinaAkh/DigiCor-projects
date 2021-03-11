import pandas as pd
import numpy as np
from apiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials
import schedule
import time

SCOPES = ['https://www.googleapis.com/auth/analytics.readonly']
KEY_FILE_LOCATION = './client_secrets.json'
VIEW_ID = '190568677'

def job():
    def initialize_analyticsreporting():
        
        credentials = ServiceAccountCredentials.from_json_keyfile_name(
           KEY_FILE_LOCATION, SCOPES)
        analytics = build('analyticsreporting', 'v4', credentials=credentials)
        return analytics
    
    #Get one report page
    def get_report(analytics, pageTokenVar):
      return analytics.reports().batchGet(
          body={
            'reportRequests': [
            {
              'viewId': VIEW_ID,
              'dateRanges': [{'startDate': '14daysAgo', 'endDate': 'today'}],
              'metrics': [{'expression': 'ga:totalEvents'}],
              'dimensions': [{'name': 'ga:eventLabel'}],
              'pageSize': 10000,
              'pageToken': pageTokenVar,
              'samplingLevel': 'LARGE'
            }]
          }
      ).execute()
    
    def handle_report(analytics,pagetoken,rows):  
        response = get_report(analytics, pagetoken)
    
        #Header, Dimentions Headers, Metric Headers 
        columnHeader = response.get("reports")[0].get('columnHeader', {})
        dimensionHeaders = columnHeader.get('dimensions', [])
        metricHeaders = columnHeader.get('metricHeader', {}).get('metricHeaderEntries', [])
    
        #Pagination
        pagetoken = response.get("reports")[0].get('nextPageToken', None)
        
        #Rows
        rowsNew = response.get("reports")[0].get('data', {}).get('rows', [])
        rows = rows + rowsNew
        #print("len(rows): " + str(len(rows)))
    
        #Recursivly query next page
        if pagetoken != None:
            return handle_report(analytics,pagetoken,rows)
        else:
            #nicer results
            nicerows=[]
            for row in rows:
                dic={}
                dimensions = row.get('dimensions', [])
                dateRangeValues = row.get('metrics', [])
    
                for header, dimension in zip(dimensionHeaders, dimensions):
                    dic[header] = dimension
    
                for i, values in enumerate(dateRangeValues):
                    for metric, value in zip(metricHeaders, values.get('values')):
                        if ',' in value or ',' in value:
                            dic[metric.get('name')] = float(value)
                        else:
                            dic[metric.get('name')] = int(value)
                nicerows.append(dic)
            return nicerows
    
    analytics = initialize_analyticsreporting()
    
    global df
    df = []

    rows = []
    rows = handle_report(analytics,'0',rows)

    df = pd.DataFrame(list(rows)) 
    df.rename(columns={"ga:totalEvents": "total", "ga:eventLabel": "event"}, inplace = True)
  
    array = df['total'].array

    n_25 = np.percentile(array, 25)
    n_75 = np.percentile(array, 75) + 10

    df = df[df['total'] >= n_25]
    df = df[df['total'] <= n_75]

    df = df[df['event'].str.contains("Bom")]
    #df.reset_index(drop=True, inplace = True)
    
    df.event = df.event.str.split('|').str[1]
    df.event = df.event.str.split('"').str[0]
    df = df.groupby('event', as_index=False).max()
    df = df.sort_values(by=['total'], ascending = False)
    
    df.dropna(inplace = True)
    df.reset_index(drop=True, inplace = True)

    popular_recommendations = df.iloc[0:3, 0].to_frame()
    popular_recommendations = popular_recommendations.to_dict()

    with open('hist.txt', 'w') as f:
       print(popular_recommendations, file=f)

    f.close()

schedule.every().day.at("01:00").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)