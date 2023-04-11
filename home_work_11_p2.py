from datetime import date


class Company:
    def __init__(self, name: str, foundation: int):
        self.name = name
        self.foundation = foundation

    @classmethod
    def company_info(cls, name, year):
        return cls(name, date.today().year - year)


company_1 = Company.company_info('Google', 1995)
print(company_1.foundation)

