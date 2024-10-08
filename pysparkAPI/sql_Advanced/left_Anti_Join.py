# Left Anti Join

from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()

empleados = spark.read.parquet('./data/empleados/')

departamentos = spark.read.parquet('./data/departamentos/')

from pyspark.sql.functions import col

empleados.join(departamentos, col('num_dpto') == col('id'), 'left_anti').show()

departamentos.join(empleados, col('num_dpto') == col('id'), 'left_anti').show()

