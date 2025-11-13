from pyspark.sql import SparkSession
from pyspark.sql.functions import col, count

def transform(input_path: str, output_path: str):
    spark = SparkSession.builder.appName("PostsTransform").getOrCreate()
    
    df = spark.read.json(input_path)
    transformed = df.groupBy("userId").agg(count("*").alias("post_count"))
    
    transformed.write.mode("overwrite").parquet(output_path)
    spark.stop()

if __name__ == "__main__":
    transform("/data/raw/posts.json", "/data/processed/user_post_counts")
