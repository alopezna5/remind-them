from .config.TargetPerson import TargetPerson
from datetime import date

N_DAYS_FREQUENCY = int(30)


class FriendsReminder:
    targets: list

    def __init__(self, friends):
        self.targets = friends

    def month_frequency(self, target: TargetPerson):
        return round(N_DAYS_FREQUENCY / (target.relevance * 2 - target.nMonthlyMeetings))

    def talk_or_not(self, target: TargetPerson):
        frequency = self.month_frequency(target)
        return (date.today() - target.lastContact).days > frequency

    def todays_targets(self):
        targets = []
        for target in self.targets:
            if self.talk_or_not(target):
                targets.append(target.name)
        return targets

    def set_last_meeting(self):
        pass


test_targets = [
    TargetPerson(name='1', relevance=1, nMonthlyMeetings=0, lastContact=date(2022, 9, 1)),
    TargetPerson(name='2', relevance=2, nMonthlyMeetings=1, lastContact=date(2022, 9, 1)),
    TargetPerson(name='3', relevance=3, nMonthlyMeetings=1, lastContact=date(2022, 9, 1)),
    TargetPerson(name='4', relevance=4, nMonthlyMeetings=1, lastContact=date(2022, 9, 1)),
    TargetPerson(name='5', relevance=5, nMonthlyMeetings=2, lastContact=date(2022, 9, 1)),
    TargetPerson(name='6', relevance=6, nMonthlyMeetings=2, lastContact=date(2022, 9, 1)),
    TargetPerson(name='7', relevance=7, nMonthlyMeetings=3, lastContact=date(2022, 9, 1)),
    TargetPerson(name='8', relevance=8, nMonthlyMeetings=4, lastContact=date(2022, 9, 1)),
    TargetPerson(name='9', relevance=9, nMonthlyMeetings=4, lastContact=date(2022, 9, 1)),
    TargetPerson(name='10', relevance=10, nMonthlyMeetings=8, lastContact=date(2022, 9, 1)),
    TargetPerson(name='11', relevance=10, nMonthlyMeetings=0, lastContact=date(2022, 11, 1)),
]

test = FriendsReminder(test_targets)

for target in test_targets:
    print('Target {} has to be contacted every {} days'.format(target.name, test.month_frequency(target)))


print(test.todays_targets())