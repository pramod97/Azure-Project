# Databricks notebook source
configs = {"fs.azure.account.auth.type": "OAuth",
"fs.azure.account.oauth.provider.type": "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider",
"fs.azure.account.oauth2.client.id": "************",
"fs.azure.account.oauth2.client.secret": '**************',
"fs.azure.account.oauth2.client.endpoint": "***************"}

dbutils.fs.mount(
source = "abfss://tokyo-olympic-data@tokyoolympicstr.dfs.core.windows.net", # contrainer@storageacc
mount_point = "/mnt/tokyoolymic",
extra_configs = configs)


# COMMAND ----------

# MAGIC %fs
# MAGIC ls "/mnt/tokyoolymic"

# COMMAND ----------

spark

# COMMAND ----------

athletes = spark.read.format("csv").option("header","true").load("/mnt/tokyoolymic/raw-data/athletes.csv")

# COMMAND ----------

coaches = spark.read.format("csv").option("header","true").load("/mnt/tokyoolymic/raw-data/coaches.csv")
EntriesGender = spark.read.format("csv").option("header","true").option("inferSchema","true").load("/mnt/tokyoolymic/raw-data/EntriesGender.csv")
Medals = spark.read.format("csv").option("header","true").option("inferSchema","true").load("/mnt/tokyoolymic/raw-data/Medals.csv")
Teams = spark.read.format("csv").option("header","true").option("inferSchema","true").load("/mnt/tokyoolymic/raw-data/Teams.csv")

# COMMAND ----------

athletes.show()

# COMMAND ----------

athletes.printSchema()

# COMMAND ----------

coaches.show()

# COMMAND ----------

coaches.printSchema()

# COMMAND ----------

EntriesGender.show()

# COMMAND ----------

EntriesGender.printSchema()

# COMMAND ----------

from pyspark.sql.functions import col
from pyspark.sql.types import IntegerType

EntriesGender = EntriesGender.withColumn("Female",col("Female").cast(IntegerType()))\
    .withColumn("Male",col("Male").cast(IntegerType()))\
        .withColumn("Total",col("Total").cast(IntegerType()))
        

# COMMAND ----------

EntriesGender.printSchema()

# COMMAND ----------

Medals.show()

# COMMAND ----------

Medals.printSchema()

# COMMAND ----------

Teams.show()

# COMMAND ----------

Teams.printSchema()

# COMMAND ----------

athletes.write.mode("overwrite").option("header", "true").csv("/mnt/tokyoolymic/transformed-data/athletes")


# COMMAND ----------

coaches.write.mode("overwrite").option("header","true").csv("/mnt/tokyoolymic/transformed-data/coaches")
EntriesGender.write.mode("overwrite").option("header","true").csv("/mnt/tokyoolymic/transformed-data/EntriesGender")
Medals.write.mode("overwrite").option("header","true").csv("/mnt/tokyoolymic/transformed-data/Medals")
Teams.write.mode("overwrite").option("header","true").csv("/mnt/tokyoolymic/transformed-data/Teams")

# COMMAND ----------

athletes.printSchema()
athletes.show()

