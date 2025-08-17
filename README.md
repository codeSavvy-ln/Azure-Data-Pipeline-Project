# Azure-Data-Engineering-Project
**End-to-End Data Pipeline Implementation Using Azure**

---

## **Project Overview**  
This project demonstrates an end-to-end data engineering solution built using Microsoft Azure. The pipeline automates data ingestion, transformation, and storage, providing an efficient and scalable system for managing enterprise data.  

## **Pipeline Architecture**  
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
