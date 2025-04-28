**Scenario:** 
Using local python integrating with BigQuery(Python + Bigquery) as part of Data Visualization using BigQuery

### Introduction about Bigquery:
  1.Fully managed ,server less, data warehouse for large data sets which enables fast SQL Queries
### How to start Bigquery in Google Console? 
1. Navigate to url : 
2. Create a new project in Bigquery with   user defined name
3. Add data by clicking “+” icon and choose public dataset which is  not paid 
4. Go to explorer and run the  below sample sql query 
                SELECT
                  name, gender,
                  SUM(number) AS total
                FROM
                  `bigquery-public-data.tablename`
                GROUP BY
                  name, gender
                ORDER BY
                  total DESC
                LIMIT
                  10;
            
**How to Setup Python in Local machine ?**
Download python and setup in local machine

**To Create a service account:**
1.	Go to the Google Cloud Console.
2.	Select your project.
3.	Go to "IAM & Admin" > "Service Accounts".
4.	Click "+ CREATE SERVICE ACCOUNT".
5.	Enter a service account name and click "Create".
6.	Grant the service account the necessary BigQuery permissions (e.g., "BigQuery Data Viewer", "BigQuery Data Editor").
7.	Click "Create Key" and choose JSON.
8.	Download the JSON key file and store it securely.
•	Set the GOOGLE_APPLICATION_CREDENTIALS environment variable:
In your terminal or command prompt, set the GOOGLE_APPLICATION_CREDENTIALS environment variable to the path of the JSON key file you downloaded:
export GOOGLE_APPLICATION_CREDENTIALS="path/to/your/service-account-file.json"
Replace "path/to/your/service-account-file.json" with the actual path to your JSON key file. In Windows, use set instead of export.

5. Use the BigQuery client in below Python code:
Now that you've imported the library and authenticated, you can use the BigQuery client to interact with BigQuery. Here's a basic example of how to create a BigQuery client and run a query:

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


