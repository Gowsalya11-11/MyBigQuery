**Scenario:** 
Using local python setup to integrating with Google cloud BigQuery(Python + Bigquery) as part of Data Visualization

### Introduction about Bigquery:
  1.Fully managed ,server less, data warehouse for large data sets which enables fast SQL Queries
### How to start Bigquery in Google Console? 
1. Navigate to Google console url : https://console.cloud.google.com/bigquery?hl=en
2. Create a new project in Bigquery with user defined name
3. Add data by clicking “+ Add Data” and choose public dataset it free available for practise
4. In the Explorer panel DataSet is loaded successfully  
5. In Query panel add the below sample Query ,click on run 
                SELECT  
                  name, gender,  
                  SUM(number) AS total  
                FROM  
                  `bigquery-public-data.tablename`  
                GROUP BY  
                  name, gender  
                ORDER BY  
                  total DESC  
                LIMIT10;  
6. Results will be displayed successfully

Note: Json file is required to execute the Bigquery using python in local machine 
            
**To Create a service account:**  
1.	Go to the Google Cloud Console.
2.	Select your project.
3.	Go to "IAM & Admin" -> "Service Accounts".
4.	Click "+ CREATE SERVICE ACCOUNT".
5.	Enter a service account name and click "Create".
6.	Grant the service account the necessary BigQuery permissions (e.g., "BigQuery Data Viewer", "BigQuery Data Editor").
7.	Click "Create Key" and choose JSON.
8.	Download the JSON key file and store it securely.
9.	Use the BigQuery client in below Python code:
      Now that you've imported the library and authenticated, you can use the BigQuery client to interact with BigQuery. Here's a basic example of how to create a BigQuery client and run a query

from google.cloud import bigquery  
import pandas as pd

### Construct a BigQuery client object.
client = bigquery.Client()

### Define your SQL query.
query = """
    SELECT
        word,
        word_count
    FROM
        `bigquery-public-data.samples.shakespeare`
    WHERE
        corpus = 'hamlet'
    ORDER BY
        word_count DESC
    LIMIT 10
"""

### Run the query.
query_job = client.query(query)  # Make an API request.

### Print the results.
for row in query_job:
    print(f"word: {row.word}, word_count: {row.word_count}")

### Convert the results to a Pandas DataFrame
df = query_job.to_dataframe()
print(df.head())


