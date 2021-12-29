class Date:
    def __init__(self, date):
        self.date = date

    @classmethod
    def make_int(cls, date):
        return list(map(int, date.split('-')))


    @staticmethod
    def is_it_date(date):
        dd, mm, yyyy = date.split('-')
        if 0 < int(dd) < 32 and 0 < int(mm) < 13 and 1000 < int(yyyy) < 3000:
            return f"Дата {date} корректная"
        else:
            return f"Дата {date} некорректная"


print(Date.make_int("29-12-2020"))
print(Date.is_it_date("29-12-2021"))
print(Date.is_it_date("31-12-2023"))



