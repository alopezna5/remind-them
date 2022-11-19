#!/usr/bin/python
from remind_them.utilities.excel_converter.ExcelReader import ExcelReader
from remind_them.utilities.friends_reminder.FriendsReminder import FriendsReminder
from remind_them.utilities.telegram_connector.TelegramConnector import TelegramConnector



def main():
    excel = ExcelReader('/home/telugu/PycharmProjects/remind-them/data/targets.xls')
    n_targets = excel.n_targets()
    raw_targets = excel.my_excel_to_dict()
    targets = FriendsReminder(raw_targets, n_targets)
    todays_targets = targets.todays_targets()
    telegram_connector = TelegramConnector()
    msg = """  
    *REMIND THEM - TODAYS TARGETS:*
    ---------------
    """

    for today_target in todays_targets:
        target_msg = "\n {}  Last contact: {}".format(today_target[0], today_target[1])
        msg += target_msg
    telegram_connector.message_sender(msg)
    print(msg)
    excel.update_excel(targets.targets)



if __name__ == "__main__":
    main()