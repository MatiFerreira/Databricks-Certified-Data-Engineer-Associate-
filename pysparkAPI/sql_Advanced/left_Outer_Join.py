# Left Outer Join

from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()

empleados = spark.read.parquet('./data/empleados/')

departamentos = spark.read.parquet('./data/departamentos/')

from pyspark.sql.functions import col

empleados.join(departamentos, col('num_dpto') == col('id'), 'leftouter').show()

empleados.join(departamentos, col('num_dpto') == col('id'), 'left_outer').show()

empleados.join(departamentos, col('num_dpto') == col('id'), 'left').show()

