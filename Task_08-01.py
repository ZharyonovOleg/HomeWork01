class Data:
    def __init__(self, date: str):
        self.__date = date

    @classmethod
    def data_to_int(cls, obj):
        split_data_to_int = list(map(int, obj.date.split('-')))
        return split_data_to_int

    @staticmethod
    def check_data(obj):
        from time import strptime
        try:
            valid_date = strptime(obj.date.replace('-', '/'), '%d/%m/%Y')
        except ValueError as ve:
            return f'Дата введена некорректно!!! {ve}'
        else:
            return f'Дата введена корректно!'

    @property
    def date(self):
        return self.__date