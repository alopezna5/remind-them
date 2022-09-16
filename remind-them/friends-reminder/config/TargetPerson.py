import datetime


class TargetPerson:
    name: str
    relevance: int
    nMonthlyMeetings: int
    lastContact: datetime

    def __init__(self, name, relevance, nMonthlyMeetings, lastContact):
        self.name = name
        self.relevance = relevance
        self.nMonthlyMeetings = nMonthlyMeetings
        self.lastContact = lastContact
