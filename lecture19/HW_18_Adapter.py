import json
import csv


class JsonConvert:
    def __init__(self, json_file):
        self.json_file = json_file
        self.data = None

    def read_file_json(self, filename):
        with open(filename, 'r') as json_file:
            self.data = json.load(json_file)
        return self.data

    def write_file(self, filename: str):
        if self.data:
            with open(filename, 'w', newline='') as csv_file:
                fieldnames = self.data[0].keys()
                csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                csv_writer.writeheader()
                csv_writer.writerows(self.data)


converter = JsonConvert('example.json')
converter.read_file_json(converter.json_file)
converter.write_file('example.csv')
converter.write_file('example2.csv')


