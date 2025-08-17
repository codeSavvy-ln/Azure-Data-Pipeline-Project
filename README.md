# Azure-Data-Pipeline-Project

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
    ├── adls_parquet_hosa_archive_ds.json
    ├── adls_parquet_hosb_archive_ds.json
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
    ├── Azuredatabricks.json
    ├── emr_pl_src_to_landing.json
    ├── emr_pl_src_to_landing_copy1.json
    ├── silver_to_gold.json
    └── sqldb_to_bronze.json
└── publish_config.json
