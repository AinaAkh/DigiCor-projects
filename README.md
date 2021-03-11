# DigiCor projects
 Web Crawler, Dashboard, Recommender engine

1.Web Crawler - written in Python3 with bs4 and selenium packages:
Run main.py to access the crawler program. This code will create soecification.xlsx file with partner's data (Supermicro, ASUS, Intel).
Run app.py to view crawler data on the dashboard (will need to run front-end for that in dashboard folder -> npm start).

2.Recommender - written in Python3, Flask package:
Run app.py to view the output on the dashboard
Part 1: Recommend list of 6 similar products based on product's bom_id (we used cosine_similarity to generate the similarity matrix);
Part 2: Access Google Analytics data to retrieve list of popular products within last 14 days; Credentials are in client_secret.json;
Program (history_data.py) suppose to run once every day (I put timer for that in the code), list of popular products will be generated and written in history.txt file;
later on app.py will read histroy.txt file to obtain the list.

3.Dashboard - written with JavaScript React:
Consist of - Crawler - Recommender engine - Compasrison (front-end not yet finished) parts
To run the Crawler, go to the Crawler option on a dashboard and press 'Run the Crawler'
