import json
from pyspark.sql import SQLContext
from pyspark import SparkContext
from pyspark.sql.types import StructType    

sc = SparkContext.getOrCreate();
spark = SQLContext(sc)

f = open('schema.json') # Generated at the time of training
schema_json = json.load(f)
schema = StructType.fromJson(json.loads(schema_json))

def input_fn(X):
    df = spark.read.schema(schema).json(sc.parallelize([X]))
    return df

def output_fn(Y):
    return Y
