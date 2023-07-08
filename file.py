import csv

class File:
    def __init__(self, file_name, file_extension):
        self.file_name = file_name
        self.file_extension = file_extension

    def read_file(self):
        if self.file_extension == "txt":
            return self.read_txt_file()
        else:
            return self.read_csv_file()

    def read_txt_file(self):
        file = open(self.file_name)
        lines = file.readlines()
        for index in range(len(lines)):
            lines[index] = lines[index].replace("\n", "")
        return lines
    
    def read_csv_file(self):
        file = open(self.file_name)
        csvreader = csv.reader(file)
        rows = []
        for row in csvreader:
            rows.append(row)            
        return rows
