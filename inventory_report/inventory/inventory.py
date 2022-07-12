from csv import reader
from json import load
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    def csv_reader(path):
        with open(path, 'r', encoding='utf-8') as file:
            csv_reader = reader(file, delimiter=',', quotechar='"')

            head, *data = csv_reader

        return [dict(zip(head, row)) for row in data]

    def json_reader(path):
        with open(path, 'r', encoding='utf-8') as file:
            json_file_data = load(file)

        return json_file_data

    def report_generator(data, type):
        if type == 'simples':
            return SimpleReport.generate(data)
        elif type == 'completo':
            return CompleteReport.generate(data)
        else:
            raise ValueError('Unknown type')

    @classmethod
    def import_data(cls, path, type):
        if path.endswith("csv"):
            data_file = cls.csv_reader(path)
        elif path.endswith("json"):
            data_file = cls.json_reader(path)
        else:
            raise ValueError('Unable to read selected file')

        return cls.report_generator(data_file, type)
