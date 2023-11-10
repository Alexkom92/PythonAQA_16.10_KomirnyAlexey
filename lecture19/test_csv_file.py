from lecture19.HW_18_Adapter import JsonConvert
from lecture19.HW_18_Adapter import CsvFileOperations
import csv


class Test_operations_csv:
    def test_append_line(self):
        csv_operations = CsvFileOperations("example.csv")
        data = ["Test", "User", "25", "Male", "50000"]
        csv_operations.append_str_to_csv(data)

        with open("example.csv", mode="r") as file:
            reader = csv.reader(file)
            rows = list(reader)

        assert data == rows[-1]

    def test_delete_line(self):
        csv_operations = CsvFileOperations("example.csv")
        row_index = 1

        with open("example.csv", "r") as f:
            reader_before = csv.reader(f)
            rows_before = list(reader_before)

        # Проверка, что индекс строки для удаления корректен
        assert 0 <= row_index < len(rows_before)

        csv_operations.del_str_csv(row_index)

        with open("example.csv", "r") as f:
            reader_after = csv.reader(f)
            rows_after = list(reader_after)

        assert len(rows_before) == len(rows_after) + 1
