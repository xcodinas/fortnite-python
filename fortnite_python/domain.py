from enum import Enum


class Platform(Enum):
    """Defines the platform the account uses"""
    PC = 'pc'
    XBOX = 'xbl'
    PSN = 'psn'


class Mode(Enum):
    """Defines the gamemode in which a user played"""
    SOLO = 'p2'
    DUO = 'p10'
    SQUAD = 'p9'


class Domain:
    """T"""
    def __init__(self, data, meta=None):
        """Creates data object"""
        self._data = data
        self.from_json()

    def __repr__(self):
        """Returns string containing printable representation of object"""
        return '<{0} {1}>'.format(self.__class__.__name__, self.id)

    def __str__(self):
        """Returns id"""
        return str(self.id)

    def from_json(self):
        """Sets default id to 1"""
        self.id = 1


class Player(Domain):
    """The Player class builds a player object to be queried"""
    def __repr__(self):
        """Returns string containing printable representation of object"""
        return '<{0} {1} {2}>'.format(
            self.__class__.__name__, self.id, self.platform)

    def from_json(self):
        """Sets player attributes from json data"""
        super().from_json()
        self.id = self._data.get('accountId')
        self.platform = self._data.get('platformName')
        self.username = self._data.get('epicUserHandle')
        self.recentMatches = self._data.get('recentMatches')
        self._stats = self._data.get('stats')
        self._lifetime = self._data.get('lifeTimeStats')

    def getStats(self, mode=Mode.SQUAD):
        """Returns player stats"""
        return Stats(self._stats.get(mode.value))


class Stats(Domain):
    """The Stats class builds a stats object of a player"""
    def __init__(self, stats):
        """Creates states object"""
        self._data = stats
        self.from_json()

    def from_json(self):
        """Takes in arguments and sets attributes to default by placement"""
        super().from_json()
        if 'wins' in self._data:
            self.wins = self._data.get('top1').get('value')
        self.total = self._data.get('matches').get('value')
        self.kd = self._data.get('kd').get('value')
        if 'winRatio' in self._data:
            self.winratio = self._data.get('winRatio').get('value')
        self.kills = self._data.get('kills').get('value')
        self.score = self._data.get('score').get('value')
        self.score_match = self._data.get('scorePerMatch').get('value')
        self.kills_match = self._data.get('kpg').get('value')
        self.top3 = self._data.get('top3').get('value')
        self.top5 = self._data.get('top5').get('value')
        self.top6 = self._data.get('top6').get('value')
        self.top10 = self._data.get('top10').get('value')
        self.top12 = self._data.get('top12').get('value')
        self.top25 = self._data.get('top25').get('value')
        self.avg_time = self._data.get('avgTimePlayed').get('value')

    def __str__(self):
        """Returns string of player objects"""
        stats = 'Top 1: ' + self.wins + '\n'
        stats += 'Top 3: ' + self.top3 + '\n'
        stats += 'Top 5: ' + self.top5 + '\n'
        stats += 'Top 10: ' + self.top10 + '\n'
        if hasattr(self, 'winratio'):
            stats += 'Win Ratio: ' + self.winratio + '\n'
        stats += 'Kills: ' + self.kills + '\n'
        stats += 'Kills/Match: ' + self.kills_match + '\n\n'
        return stats
