import pandas as pd
from .config.TargetPerson import TargetPerson
from remind_them.utilities.excel_converter.config.Sheet import SheetEnum

from datetime import date

N_DAYS_FREQUENCY = int(30)


class FriendsReminder:
    targets: list


    def __init__(self, friends, n_friends):
        targets = []
        ts = pd.Timestamp('2014-01-23 00:00:00', tz=None)
        for i in range(n_friends):
            targets.append(TargetPerson(
                name=friends[SheetEnum.NAME.value][i],
                relevance=friends[SheetEnum.RELEVANCE.value][i],
                nMonthlyMeetings=friends[SheetEnum.N_MONTHLY_MEETINGS.value][i],
                lastContact=friends[SheetEnum.LAST_CONTACT.value][i].to_pydatetime()))

        self.targets = targets


    def month_frequency(self, target: TargetPerson):
        divider = abs(target.relevance * 2 - target.nMonthlyMeetings)
        divider = 1 if divider == 0 else divider
        return round(N_DAYS_FREQUENCY / divider)


    def talk_or_not(self, target: TargetPerson):
        frequency = self.month_frequency(target)
        return (date.today() - target.lastContact.date()).days > frequency


    def set_last_meeting(self, target: TargetPerson):
        target.lastContact = date.today()


    def todays_targets(self):
        targets = []
        for target in self.targets:
            if self.talk_or_not(target):
                targets.append((target.name, target.lastContact))
                self.set_last_meeting(target)
        return targets