import datetime
import time
import typing

import pandas as pd


filename = 'files/smeta.xlsx'

class Smeta:
    work_flags = ['ФЕР', 'ТЕР']
    mat_flags = ['ФССЦ', 'прайс']
    razdel_flags = ['Раздел']


    def __init__(self):
        self.n_colonka_type: int = 11
        self.estimate_col_indexes: dict = {
            'code': 2,
            'name': 3,
            'unit': 6,
            'amount': 9,
        }
        self.work_filters = self.work_flags
        self.material_filters = self.mat_flags
        self.razdel_filters = self.razdel_flags
        self.last_operation_row: int = 0

    def filter_lines(self, line: pd.Series, filters: [str]):
        for cell in line:
            if any(f in str(cell) for f in filters):
                print('TRUE!!!>>>>', line.tolist().index(cell))
                return True
        return False

    def exel_parser(self, io) -> pd.DataFrame:
        df = pd.read_excel(io=io, engine='openpyxl', usecols=list(range(self.n_colonka_type+1)), header=None)
        filtered = df[df.apply(lambda row: self.filter_lines(row, self.work_filters), axis=1)]
        return filtered

    def get_entities(self, filtered_df: pd.DataFrame):
        entities = []
        for row in filtered_df.itertuples():
            entity = {
                key: row[self.estimate_col_indexes[key]]
                if pd.notnull(row[self.estimate_col_indexes[key]])
                else None
                for key in self.estimate_col_indexes.keys()
            }
            if all(pd.notnull(value) for value in entity.values()):
                entities.append(entity)
        return entities

def my_timer(func: typing.Callable):

    def wrapper(*args, **kwargs):
        start_time = datetime.datetime.now()
        result = func(*args, **kwargs)
        delta_t = datetime.datetime.now() - start_time
        print(f'MY_TIMER>>FUNC:{func.__name__}>>>time>>>{delta_t}>>>{func.__qualname__}')
        return result
    return wrapper
