import csv

def write_csv_with_headers(path=None, contents=[], fieldnames=[], delimiter=";", newline="\n", encoding="utf-8"):
	"""Write the 'contents' into the file specified by 'path' formatted as csv with a hader row.
		
	Arguments:
	path -- path to the csv-file to be written. Will throw an error if not specified. (default: None)
	contents -- list of rows to write. (default: [])
	fieldnames -- keys of the row-dicts in 'contents'. Only used if 'contents' is a dict (default: [])
	delimiter -- character used to separate values from each other in the file (default: ";")
	newline -- character used to separate rows from each other in the file (default: "\\n")
	encoding -- encoding in which the file is written (default: "utf-8")
	"""

	with open(path, mode="w", encoding=encoding, newline=newline) as file:
		
		# If fieldnames are not provided, get them from the first row of 'contents'
		if len(fieldnames) == 0:
			fieldnames = list(contents[0].keys())

		writer = csv.DictWriter(file, fieldnames=fieldnames, delimiter=delimiter)

		writer.writeheader()
		for row in contents:
			writer.writerow(row)

def write_csv_without_headers(path=None, contents=[], delimiter=";", newline="\n", encoding="utf-8"):
	"""Write the 'contents' into the file specified by 'path' formatted as csv without a header row.
		
	Arguments:
	path -- path to the csv-file to be written. Will throw an error if not specified. (default: None)
	contents -- list of rows to write. (default: [])
	delimiter -- character used to separate values from each other in the file (default: ";")
	newline -- character used to separate rows from each other in the file (default: "\\n")
	encoding -- encoding in which the file is written (default: "utf-8")
	"""

	with open(path, mode="w", encoding=encoding, newline=newline) as file:
		writer = csv.writer(file, delimiter=delimiter)
		for row in contents:
			writer.writerow(row)

def read_csv_without_headers(path=None, delimiter=";", newline="\n", encoding="utf-8"):
	"""Read given csv-file and return a list of lists of the rows in the file.
	
	Arguments:
	path -- path to the csv-file to be read. Will throw an error if not specified. (default: None)
	delimiter -- character used to separate values from each other in the file (default: ";")
	newline -- character used to separate rows from each other in the file (default: "\\n")
	encoding -- encoding in which the file is read (default: "utf-8")
	"""

	with open(path, encoding=encoding, newline=newline) as file:
		reader = csv.reader(file, delimiter=delimiter)
		return list(reader)

def read_csv_with_headers(path=None, delimiter=";", newline="\n", encoding="utf-8", fieldnames=None):
	"""Read given csv-file and return a list of dicts of the rows in the file.
	
	Arguments:
	path -- path to the csv-file to be read. Will throw an error if not specified. (default: None)
	delimiter -- character used to separate values from each other in the file (default: ";")
	newline -- character used to separate rows from each other in the file (default: "\\n")
	encoding -- encoding in which the file is read (default: "utf-8")
	fieldnames -- list of fieldnames for the dictionaries. Only used if 'output_dict' is True. If not specified, will be read from the first row. (default: None)
	"""

	with open(path, encoding=encoding, newline=newline) as file:
		reader = csv.DictReader(file, delimiter=delimiter, fieldnames=fieldnames)
		return list(reader)


class CsvUtils():
	"""CsvUtils provides helper functions for reading and writing csv files

	Methods:
	write(path, contents, fieldnames, delimiter, newline, encoding) -- format 'contents' as csv and write it into 'path'
	read(path, delimiter, newline, encofing, output_dict, fieldnames) -- read file in 'path' into a list of rows
	"""

	def write(path=None, contents=[], fieldnames=[], delimiter=";", newline="\n", encoding="utf-8"):
		"""Write the 'contents' into the file specified by 'path' formatted as csv.
		
		Arguments:
		path -- path to the csv-file to be written. Will throw an error if not specified. (default: None)
		contents -- list of rows to write. (default: [])
		fieldnames -- keys of the row-dicts in 'contents'. Only used if 'contents' is a dict (default: [])
		delimiter -- character used to separate values from each other in the file (default: ";")
		newline -- character used to separate rows from each other in the file (default: "\\n")
		encoding -- encoding in which the file is written (default: "utf-8")
		"""

		# If 'contents' is a list of dicts, call write_csv_with_headers, otherwise call write_csv_without_headers
		if type(contents[0]) is dict:
			write_csv_with_headers(path=path, fieldnames=fieldnames, contents=contents, delimiter=delimiter, newline=newline, encoding=encoding)
		else:
			write_csv_without_headers(path=path, contents=contents, delimiter=delimiter, newline=newline, encoding=encoding)

	def read(path=None, delimiter=";", newline="\n", encoding="utf-8", output_dict=False, fieldnames=None):
		"""Read given csv-file and return a list of rows in the file.
		
		Arguments:
		path -- path to the csv-file to be read. Will throw an error if not specified. (default: None)
		delimiter -- character used to separate values from each other in the file (default: ";")
		newline -- character used to separate rows from each other in the file (default: "\\n")
		encoding -- encoding in which the file is read (default: "utf-8")
		output_dict -- if the output should be a list of dicts or a list of lists (default: False)
		fieldnames -- list of fieldnames for the dictionaries. Only used if 'output_dict' is True. If not specified, will be read from the first row. (default: None)
		"""

		# If 'output_dict' is set to True, call read_csv_with_headers, otherwise call read_csv_without_headers
		if output_dict:
			return read_csv_with_headers(path=path, delimiter=delimiter, newline=newline, encoding=encoding)
		
		return read_csv_without_headers(path=path, delimiter=delimiter, newline=newline, encoding=encoding)