import pandas as pd 
import os

required_jobs=[
  

  "Senior Distinguished Architect"
  "Senior Distinguished Engineer"
  "Senior Engineering Leader"
  "Distinguished Architect"
  "Distinguished Engineer"
  "Engineering Leader"
  "Senior Principal Architect"
  "Senior Principal Engineer"
  "Senior Engineering Manager II"
  "Principal Architect"
  "Principal Engineer"
  "Senior Engineering Manager I"
  "Senior Architect"
  "Senior Staff Engineer"
  "Engineering Manager"
  "Architect"
  "Staff Engineer"
  "Technical Lead"
  "Senior Engineer"
  "Associate Engineer"
  "Senior Leader"
  "Leader"
  "Senior Manager II"
  "Senior Manager I"
  "Manager"
  "Associate Manager"
  "Lead"
  "Associate Lead"
  "Associate Product Analyst"
  "Product Analyst"
  "Senior Product Analyst"
  "Lead Product Analyst"
  "Associate Analyst"
  "Analyst"
  "Senior Analyst"
  "Lead Consultant"
  "Senior Lead Consultant"
  "Principal Consultant"
  "Senior Principal Consultant"
  "Client Manager"
  "Senior Client Manager I"
  "Senior Client Manager II"
  "Client Partner"
  "Senior Client Partner"
  "Head"
  "Group Head"
  "Specialist"
  "Senior Specialist"
  "Lead Engineer"
  "Product Owner"
  "MDM Architect"

]
file_path = r"C:\Users\ksatish\Documents\2025_6_demands.xlsx"
df= pd.read_excel(file_path)
print(df.head())

def check_job(job_title):
    for job in required_jobs:
        if job.lower() in str(job_title).lower():
            return "in required list"
        return "Not in required list"
    
df['reason'] = df['job_req_title'].apply(check_job)
filter_df =df.copy()
clean_df = df[df['reason']=="in required list"].copy()

output_path ="demands/final_output.xlsx"   
with pd.ExcelWriter(output_path, engine='xlsxwriter') as writer:
    filter_df.to_excle(writer,sheet_name='Fliter', index=False)
    clean_df.to_excel(writer,sheet_name= 'Clean',index= False)

    print("compeleted")

    