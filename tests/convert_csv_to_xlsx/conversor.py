import pandas as pd
from os import makedirs, chdir

file_name_path = 'tests/convert_csv_to_xlsx/email'

makedirs(file_name_path)
chdir(file_name_path)
csv_created = open("email.csv", "x")
file_csv = pd.read_csv (csv_created)
file_csv.to_excel (file_name_path, index = None, header=True)

