python
import pandas as pd

# Load the dataset
file_path = 'Agricultural_Business_Licenses_Dataset.xlsx'
data = pd.read_excel(file_path)

# Display the first few rows
print('Dataset Overview:')
print(data.head())

# Analyze license types and their counts
license_type_counts = data['License Type'].value_counts()
print('\nLicense Type Distribution:')
print(license_type_counts)

# Filter dataset for licenses expiring in the next year
import datetime
today = datetime.datetime.today()
next_year = today + datetime.timedelta(days=365)
expiring_licenses = data[data['Expiry Date'] <= next_year]
print('\nLicenses Expiring in the Next Year:')
print(expiring_licenses)

# Save filtered data for further analysis
expiring_licenses.to_excel('Expiring_Licenses_Next_Year.xlsx', index=False)
print('\nFiltered data saved to Expiring_Licenses_Next_Year.xlsx')
