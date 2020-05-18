import csv

with open('script_results.csv', 'w', newline='') as f:
  csv_writer = csv.writer(f, delimiter='\t')

  csv_writer.writerow(['col1', 'col2', 'col3'])

