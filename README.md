# Azure-Project

Introduction
This project demonstrates a comprehensive data pipeline for the Tokyo Olympic data, showcasing the ingestion, transformation, storage, and visualization processes using Azure Data Factory (ADF), Azure Databricks, Azure Synapse, and Power BI.

Data Source
Dataset: Tokyo Olympic Data
Source: Kaggle
Initial Storage: GitHub Repository
Pipeline Overview
1. Full Pipeline Overview Diagram

This screenshot shows the complete view of all ADF pipelines used in the project, illustrating the flow of data through various components.

Screenshot 1: Full Pipeline Overview
![image](https://github.com/user-attachments/assets/651f8923-3988-4173-9eea-fcca22dcaeff)


2. Detailed Pipeline Screenshots

Pipeline 1: Data Ingestion Pipeline
![image](https://github.com/user-attachments/assets/63ac2cae-7232-4ccd-995c-30862a2ad8d1)
![image](https://github.com/user-attachments/assets/cde64bd3-8ef6-420e-8767-cebb7c2bb4f1)
![image](https://github.com/user-attachments/assets/7d3d177a-abb9-4e0d-8d6e-c8686926aef3)
![image](https://github.com/user-attachments/assets/cdf0daa6-7a3f-41a4-8131-dad7134811ff)
![image](https://github.com/user-attachments/assets/981137b7-a0b7-4b41-aa5a-b890762e5f25)






Description: Responsible for ingesting the Tokyo Olympic data from GitHub to Azure Data Factory.
Screenshot: Shows the pipeline’s activities, including the Copy Data activity.
Screenshot 2: Data Ingestion Pipeline Configuration
Pipeline 2: Data Transformation Pipeline

Description: Handles the transformation of data using Azure Databricks.
Screenshot: Displays the activities involved in data transformation.
Screenshot 3: Data Transformation Pipeline Configuration
Pipeline 3: Data Storage Pipeline

Description: Manages the process of storing transformed data in Azure Synapse.
Screenshot: Illustrates how data is loaded into Synapse.
Screenshot 4: Data Storage Pipeline Configuration
Data Transformation Using Azure Databricks
1. Databricks Cluster Configuration

Screenshot 5: Databricks Cluster Configuration

2. Data Transformation Notebooks

Screenshot 6: Transformation Notebook

3. Transformation Results

Screenshot 7: Transformation Results

Data Storage in Azure Synapse
1. Linked Service Configuration for Synapse

Screenshot 8: Synapse Linked Service Configuration

2. Data Load Process

Screenshot 9: Data Load Process

Data Visualization Using Power BI
1. Power BI Connection to Azure Synapse

Screenshot 10: Power BI Connection to Synapse

2. Power BI Dashboard

Screenshot 11: Power BI Dashboard
