# Databricks notebook source
dbutils.fs.mount(
source = "wasbs://bronze@adlsdevrcm.blob.core.windows.net",
mount_point = "/mnt/bronze",
extra_configs = {"fs.azure.account.key.adlsdevrcm.blob.core.windows.net":'Account Key of storage contianer'}
)

# COMMAND ----------

dbutils.fs.help()

# COMMAND ----------

dbutils.fs.ls("/mnt/landing")

# COMMAND ----------


dbutils.fs.mount(
source = "wasbs://silver@adlsdevrcm.blob.core.windows.net",
mount_point = "/mnt/silver",
extra_configs = {"fs.azure.account.key.adlsdevrcm.blob.core.windows.net":'Account Key of storage contianer'})

# COMMAND ----------


dbutils.fs.mount(
source = "wasbs://gold@adlsdevrcm.blob.core.windows.net",
mount_point = "/mnt/gold",
extra_configs = {"fs.azure.account.key.adlsdevrcm.blob.core.windows.net":'Account Key of storage contianer'})

# COMMAND ----------


dbutils.fs.mount(
source = "wasbs://landing@adlsdevrcm.blob.core.windows.net",
mount_point = "/mnt/landing",
extra_configs = {"fs.azure.account.key.adlsdevrcm.blob.core.windows.net":'Account Key of storage contianer'})
