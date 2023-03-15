import unittest

import os

from jannes_utility_package.CsvUtils.csvutils import CsvUtils

def write_file(file, contents):
	with open(file, "w", encoding="utf-8") as file:
		file.write(contents)

def read_file(file):
	with open(file, "r", encoding="utf-8") as file:
		return file.read()

def delete_file(file):
	os.remove(file)

class TestCsvMethods(unittest.TestCase):

	def setUp(self):
		self.test_file = "test.csv"
		self.test_csv_string = "a;b\n1;2\n"
		self.test_csv_list_of_lists = [["a", "b"], ["1", "2"]]
		self.test_csv_list_of_dicts = [{"a": "1", "b": "2"}]

		write_file(self.test_file, self.test_csv_string)

	def tearDown(self):
		delete_file(self.test_file)

	def test_read_to_list_of_lists(self):
		self.assertEqual(CsvUtils.read(self.test_file), self.test_csv_list_of_lists)

	def test_read_to_list_of_dicts(self):
		self.assertEqual(CsvUtils.read(self.test_file, output_dict=True), self.test_csv_list_of_dicts)

	def test_write_list_of_lists(self):
		CsvUtils.write(self.test_file, self.test_csv_list_of_lists)
		self.assertEqual(read_file(self.test_file), self.test_csv_string)

	def test_write_list_of_dicts(self):
		CsvUtils.write(self.test_file, self.test_csv_list_of_dicts)
		self.assertEqual(read_file(self.test_file), self.test_csv_string)


if __name__ == "__main__":
	unittest.main()

