import pandas as pd
from xlsxwriter.workbook import Workbook
from .config.Sheet import SheetEnum


class ExcelReader():

    def __init__(self, excel_path):
        self.excel_path = excel_path
        self.name = SheetEnum.NAME.value, 0
        self.relevance = SheetEnum.RELEVANCE.value, 1
        self.monthly_meetings = SheetEnum.N_MONTHLY_MEETINGS.value, 2
        self.last_contact = SheetEnum.LAST_CONTACT.value, 3

    def n_targets(self):
        xls = pd.ExcelFile(path_or_buffer=self.excel_path)
        return len(xls.parse('Targets').index)

    def my_excel_to_dict(self):
        xls = pd.ExcelFile(path_or_buffer=self.excel_path)
        data = xls.parse('Targets').to_dict()
        assert self.name[0] in data.keys(), 'Missing {} column'.format(SheetEnum.NAME.value)
        assert self.relevance[0] in data.keys(), 'Missing {} column'.format(SheetEnum.RELEVANCE.value)
        assert self.monthly_meetings[0] in data.keys(), 'Missing {} column'.format(SheetEnum.N_MONTHLY_MEETINGS.value)
        assert self.last_contact[0] in data.keys(), 'Missing {} column'.format(SheetEnum.LAST_CONTACT.value)
        return data

    def update_excel(self, new_dict):
        workbook = Workbook(self.excel_path)
        worksheet = workbook.add_worksheet()
        # Store the read information
        worksheet.write(0, self.name[1], self.name[0])
        worksheet.write(0, self.relevance[1], self.relevance[0])
        worksheet.write(0, self.monthly_meetings[1], self.monthly_meetings[0])
        worksheet.write(0, self.last_contact[1], self.last_contact[0])
        for i, row in enumerate(new_dict):
            worksheet.write(i+1, self.name[1], row.name)
            worksheet.write(i+1, self.relevance[1], row.relevance)
            worksheet.write(i+1, self.monthly_meetings[1], row.nMonthlyMeetings)
            worksheet.write(i+1, self.last_contact[1], row.lastContact.strftime("%d/%m/%Y"))
        workbook.close()