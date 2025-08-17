# Databricks notebook source
# MAGIC %sql
# MAGIC create schema if not exists audit;

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE TABLE IF NOT EXISTS audit.load_logs (
# MAGIC     
# MAGIC     data_source STRING,
# MAGIC     tablename STRING,
# MAGIC     numberofrowscopied INT,
# MAGIC     watermarkcolumnname STRING,
# MAGIC     loaddate TIMESTAMP
# MAGIC );

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from audit.load_logs

# COMMAND ----------

# MAGIC %sql
# MAGIC truncate table audit.load_logs