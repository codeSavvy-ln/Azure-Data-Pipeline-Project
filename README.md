# Azure-Data-Engineering-Project
**End-to-End Data Pipeline Implementation Using Azure**

---

## **Project Overview**  
This project demonstrates an end-to-end data engineering solution built using Microsoft Azure for healthcare revenue cycle management domain. The pipeline automates data ingestion, transformation, and storage, providing an efficient and scalable system for managing enterprise data.  

## **Project Architecture**  
![logo](https://github.com/codeSavvy-ln/Azure-Data-Pipeline-Project/blob/main/Images/project%20architecture%20snapshot.png)

---

## **Project Structure**
```
├── Azure SQL database
    ├── hospital-a
    │   ├── departments.csv
    │   ├── encounters.csv
    │   ├── hospital_a
    │   ├── patients.csv
    │   ├── providers.csv
    │   ├── readme
    │   └── transactions.csv
    ├── hospital-b
    │   ├── departments.csv
    │   ├── encounters.csv
    │   ├── hospital_b
    │   ├── patients.csv
    │   ├── providers.csv
    │   ├── readme
    │   └── transactions.csv
    └── readme
├── README.md
├── dataset
    ├── AzureDatabricksDeltaLakeDataset1.json
    ├── generic_adls_flat_file_ds.json
    ├── generic_adls_parquet_ds.json
    └── generic_sql_ds.json
├── factory
    └── ADF-HC-RCM-DEV-Project.json
├── landing
    ├── CPT codes
    │   ├── cptcodes.csv
    │   └── readme
    ├── claims
    │   ├── hospital1_claim_data.csv
    │   ├── hospital2_claim_data.csv
    │   └── readme
    └── readme
├── linkedService
    ├── AzureDataLakeStorage1.json
    ├── AzureDatabricks1.json
    ├── AzureDatabricksDeltaLake1_ls.json
    ├── AzureKeyVault_ls.json
    └── hosa_sql_ls.json
├── load_config.csv
├── notebook
    ├── API
    │   ├── ICD Code API extract.ipynb
    │   ├── NPI API extract.ipynb
    │   └── readme
    ├── gold
    │   ├── dim_cpt_code.py
    │   ├── dim_department.py
    │   ├── dim_icd_code.ipynb
    │   ├── dim_npi.ipynb
    │   ├── dim_patient.py
    │   ├── dim_provider.py
    │   ├── fact_transaction.sql
    │   └── readme
    ├── readme
    ├── set up
    │   ├── ADLS_mount.py
    │   ├── Audit_table.py
    │   └── readme
    └── silver
    │   ├── CPT codes.py
    │   ├── Claims.py
    │   ├── Departments_F.py
    │   ├── Encounters.py
    │   ├── ICD Code.ipynb
    │   ├── NPI.ipynb
    │   ├── Patient.py
    │   ├── Providers_F.py
    │   ├── Transactions.py
    │   └── readme
├── pipeline
    ├── emr_pl_src_to_landing.json
    ├── silver_to_gold.json
└── publish_config.json
```

## **Technologies Used**
- **Programming Language:** Python, SQL, Pyspark
- **Azure Data Factory**
- **Azure Databricks**
- **Azure Key Vault**
- **Data Sources:**
    - **Azure SQL Database**
    - **Azure storage:** ADLS Gen2, Flat files(csv), Parquet.
    - **API:** ICD code, NPI.

---


## **Pipeline Architecture (ETL Pipeline Breakdown)**  


1. **Data Ingestion**:  
   - Ingest raw tables from SQL Server using Azure Data Factory (ADF).  
	Set up Integration runtime

---



## **How the Pipeline Works** 
[load_config](https://github.com/codeSavvy-ln/Azure-Data-Pipeline-Project/blob/main/load_config.csv) Main file that holds config related details which will be referenced to implement the Data pipeline.

**Pipeline 1 - emr_pl_src_to_landing**

  - **Lookup Activity** is used to retrieve the data from load_config file. 
  - **for each activity** will iterate over each row in load_config file and perform the opertions(activity) on it.
  
![logo](https://github.com/codeSavvy-ln/Azure-Data-Pipeline-Project/blob/main/Images/emr_pl_src_to_landing.png)

  - **Get Metadata Activity** checks if the targetpath and tablename from load_config exists in bronze container.
  - **If Condition** If the output of get metadata activity is true then copy activity is ran to copy the data into archive folder under current date format yyyy/MM/DD.
  - **If Condition (Fetch_Logs)** checks if the loadtype is full
    - **If loadtype = Full** takes the data from SQL DB and store it into bronze container in parquet format and also stores the pipeline running details in the audit table
    - **If loadtype <> Full** fetches the latest loaddate and compare it in the next increamental load activity which copies the data from SQL db into bronze layer in the form of parquet format and then further update the audit table with the latest data.

**Pipeline 2 - silver_to_gold**
![logo](https://github.com/codeSavvy-ln/Azure-Data-Pipeline-Project/blob/main/Images/silver_to_gold.png)

 All the code for silver and gold layer stored in databricks notebook can be triggered from ADF itself.
- **silver** Data is in Delta format here, Data loaded here will be cleaned and SCD type 2 will also be implemented and then this will be sent to the gold layer.
- **gold** - Data is in Delta format here , Fact and Dimension table are implemented here.

---

## **How to Use**  

### **1. Prerequisites**  
- Active Azure Subscription.  
- Azure Databricks cluster with below specs:
  - Databricks runtime: 15.4 LTS(includes Apache Spark 3.5.0, Scala 2.12)
  - Worker Type: Standard_D2ds_v6 - min:1 - Max:1 - Current:0  

### **2. Steps to Set Up**  
1. Clone this repository:  
   ```bash
   git clone https://github.com/codeSavvy-ln/Azure-Data-Pipeline-Project.git
