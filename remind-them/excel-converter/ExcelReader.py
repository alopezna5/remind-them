import pandas as pd
from config.Sheet import SheetEnum

class ExcelReader():

    def __init__(self, excel_path):
        self.excel_path = excel_path

    def my_excel_to_dict(self):
        xls = pd.ExcelFile(path_or_buffer=self.excel_path)
        data = xls.parse('Targets').to_dict()
        assert SheetEnum.NAME.value in data.keys(), 'Missing {} column'.format(SheetEnum.NAME.value)
        assert SheetEnum.RELEVANCE.value in data.keys(), 'Missing {} column'.format(SheetEnum.RELEVANCE.value)
        assert SheetEnum.N_MONTHLY_MEETINGS.value in data.keys(), 'Missing {} column'.format(SheetEnum.N_MONTHLY_MEETINGS.value)
        assert SheetEnum.LAST_CONTACT.value in data.keys(), 'Missing {} column'.format(SheetEnum.LAST_CONTACT.value)
        return data

test = Exce('../../data/targets.ods')
print(test.my_excel_to_dict())