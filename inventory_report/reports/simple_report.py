class ReportFilter:
    @classmethod
    def oldest_date(cls, report):
        return min([date['data_de_fabricacao'] for date in report])

    @classmethod
    def min_fabrication_date(cls, report):
        expiration_date = [date['data_de_validade'] for date in report]

        return min(expiration_date)

    @classmethod
    def company_with_more_products(cls, report):
        all_companies = [company['nome_da_empresa'] for company in report]
        return max(all_companies, key=all_companies.count)


class SimpleReport:
    @classmethod
    def generate(cls, report):
        oldest_fabrication = ReportFilter.oldest_date(report)
        closest_expiration = ReportFilter.min_fabrication_date(report)
        company = ReportFilter.company_with_more_products(report)

        return (
            f'Data de fabricação mais antiga: {oldest_fabrication}\n'
            f'Data de validade mais próxima: {closest_expiration}\n'
            f'Empresa com mais produtos: {company}'
        )
