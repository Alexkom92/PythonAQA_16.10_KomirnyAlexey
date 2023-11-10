import json
import csv


class JsonConvert:
    def __init__(self, json_file):
        self.json_file = json_file
        self.data = None

    def read_file_json(self, filename):
        with open(filename, "r") as json_file:
            self.data = json.load(json_file)
        return self.data

    def write_file(self, filename: str):
        if self.data:
            with open(filename, "w", newline="") as csv_file:
                fieldnames = self.data[0].keys()
                csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                csv_writer.writeheader()
                csv_writer.writerows(self.data)


class CsvFileOperations:
    def __init__(self, filename):
        self._filename = filename

    def append_str_to_csv(self, data):
        with open(self._filename, "a", newline="") as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(data)

    def del_str_csv(self, row_index):
        with open(self._filename, "r") as f:
            reader = csv.reader(f)
            rows = list(reader)

        if 0 <= row_index < len(rows):
            del rows[row_index]

            with open(self._filename, "w", newline="") as f:
                writer = csv.writer(f)
                writer.writerows(rows)


# Пример использования
converter = JsonConvert("example.json")
converter.read_file_json(converter.json_file)
converter.write_file("example.csv")

filename = "example.csv"  # Передаем имя файла, а не объект CsvFileOperations
csv_operations = CsvFileOperations(filename)

data = ["Alex", "Korewqmirny", "30", "Male", "250000"]
csv_operations.append_str_to_csv(data)
# csv_operations.del_str_csv(4)  # Расскомментируйте, если нужно удалить строку
