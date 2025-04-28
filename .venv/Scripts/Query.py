from google.cloud import bigquery

#db-dtypes

# add the Json file name ,which is stored in local
key_path = "C://selenium_python//mybigquery-456319-.json"

client = bigquery.Client.from_service_account
_json(key_path)

# Example query
query = """
    SELECT *
    FROM `mybigquery-456319.transactions.txns`
"""

# Execute the query
query_job = client.query(query)
df = query_job.to_dataframe()
print(df)

# Print results
for row in query_job:
    print(row)