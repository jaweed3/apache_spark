import os
import sys

# Set the correct Python executable for Spark
os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable

# Set the correct Spark home path
os.environ['SPARK_HOME'] = r'C:\spark-3.5.5-bin-hadoop3\spark-3.5.5-bin-hadoop3'
os.environ['JAVA_HOME'] = r'C:\Program Files\Eclipse Adoptium\jdk-11.0.20.101-hotspot'
os.environ['HADOOP_HOME'] = r'C:\hadoop'

# Now import and use PySpark
from pyspark.sql import SparkSession

# Create Spark session with explicit configurations
print("Creating Spark session...")
spark = SparkSession.builder \
    .appName("SparkTest") \
    .master("local[*]") \
    .config("spark.python.worker.reuse", "true") \
    .config("spark.driver.host", "localhost") \
    .config("spark.pyspark.python", sys.executable) \
    .config("spark.pyspark.driver.python", sys.executable) \
    .getOrCreate()

print(f"Successfully created Spark session version: {spark.version}")

# Create a simple DataFrame
data = [("Java", 1000), ("Python", 2000), ("Scala", 3000)]
df = spark.createDataFrame(data, ["Language", "Users"])
print("Sample DataFrame:")
df.show()

# Stop the Spark session
spark.stop()
