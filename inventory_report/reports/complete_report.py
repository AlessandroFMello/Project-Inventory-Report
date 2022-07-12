from collections import Counter
from inventory_report.reports.simple_report import SimpleReport


class CompaniesFilter:
    @classmethod
    def companies_counter(cls, report):
        all_companies = Counter(
          [company['nome_da_empresa'] for company in report]
          )

        return all_companies

    @classmethod
    def companies_data(cls, report):
        all_companies_counter = cls.companies_counter(report)
        all_companies_data = str()

        for company in all_companies_counter.most_common():
            all_companies_data += f"- {company[0]}: {company[1]}\n"

        report = (
            "Produtos estocados por empresa:\n"
            f"{all_companies_data}"
        )

        return report


class CompleteReport(SimpleReport):
    @classmethod
    def generate(cls, report):
        complete_report = (
            f"{super().generate(report)}\n"
            f"{CompaniesFilter.companies_data(report)}"
        )

        return complete_report
