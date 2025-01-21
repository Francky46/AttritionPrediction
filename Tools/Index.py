import os
import pandas as pd
import zipfile

# Path to the dataset
src_path = "src"
general_data_file_path = os.path.join(src_path, "general_data.csv")
employee_survey_data_file_path = os.path.join(src_path, "employee_survey_data.csv")
manager_survey_data_file_path = os.path.join(src_path, "manager_survey_data.csv")
in_out_time_file_path = os.path.join(src_path, "in_out_time.zip")

# Unzip the dataset from in_out_time.zip
with zipfile.ZipFile(in_out_time_file_path, 'r') as zip_ref:
    zip_ref.extractall(src_path)

# Load the dataset
general_data = pd.read_csv(general_data_file_path)
employee_survey_data = pd.read_csv(employee_survey_data_file_path)
manager_survey_data = pd.read_csv(manager_survey_data_file_path)
in_time_data = pd.read_csv(os.path.join(src_path, "in_time.csv"))
out_time_data = pd.read_csv(os.path.join(src_path, "out_time.csv"))

# set into a dictionary
data = {
    'general_data': general_data,
    'employee_survey_data': employee_survey_data,
    'manager_survey_data': manager_survey_data,
    'in_time_data': in_time_data,
    'out_time_data': out_time_data
}
