"import csv
import json"

input_file_path = 'D:/OLD DATA/RC_2015-01'
output_file_path = 'D:/OLD DATA/Politics COMMENT 2015-01.csv'

with open(input_file_path, 'r', encoding='utf-8') as input_file, open(output_file_path, 'w', newline='', encoding='utf-8') as output_file:
    csv_writer = csv.writer(output_file)
    csv_writer.writerow(['ID', 'Body', 'Subreddit', 'Ups'])

    for line in input_file:
        try:
            json_data = json.loads(line)
            if json_data.get('subreddit') in ['democrats', 'Republican']:
                csv_writer.writerow([json_data.get('id'), json_data.get('body'), json_data.get('subreddit'),
                                     json_data.get('ups')])
        except json.JSONDecodeError:
            print("Error decoding JSON from line: " + line)