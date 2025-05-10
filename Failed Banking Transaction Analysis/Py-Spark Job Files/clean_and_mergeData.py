from pyspark.sql import SparkSession
from pyspark.sql.functions import col, trim

spark = SparkSession.builder.appName("CleanAndMergeTransactions").getOrCreate()

# Load all CSVs
df = spark.read.option("header", True).csv("gs://hemachandra-bucket/data/*.csv")

# Drop rows with nulls or blank columns
df_clean = df.dropna(how='any')
df_clean = df_clean.filter(~(col('txn_id') == "") & ~(col('status') == ""))

# Save to a single CSV file
df_clean.coalesce(1).write.option("header", True).csv("gs://hemachandra-bucket/cleaned/merged_transactions.csv", mode='overwrite')

spark.stop()
