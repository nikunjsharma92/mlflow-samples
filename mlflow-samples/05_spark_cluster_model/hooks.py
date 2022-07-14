import json
from pyspark.sql import SQLContext
from pyspark import SparkContext
from pyspark.sql.types import StructType    
import os

sc = SparkContext.getOrCreate();
spark = SQLContext(sc)

f = open(os.path.join(os.path.dirname(__file__), 'schema.json')) # Generated at the time of training. Always use absolute paths
schema_json = json.load(f)
schema = StructType.fromJson(json.loads(schema_json))

schemaReader = spark.read.schema(schema)

def input_fn(X):
    df = schemaReader.json(X)
    return df

def output_fn(Y):
    return Y
