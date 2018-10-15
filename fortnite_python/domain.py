import re

from enum import Enum


class Platform(Enum):
    """This is to refer to the platform always the same way and to prevent 
    the changes if the api updates."""
    PC = 'pc'
    XBOX = 'xbl'
    PSN = 'psn'


class Mode(Enum):
    """Same as platform but for mode"""
    SOLO = 'p2'
    DUO = 'p10'
    SQUAD = 'p9'


class Domain:
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
        for key in self._data:
            if 'id' in key or 'Id' in key or 'ID' in key:
                value = self._data.get(key)
                self.id = value if type(value) != dict else value.get('value')
                continue
            value = self._data.get(key)
            setattr(self, self.to_snake(key),
                value if type(value) != dict else value.get('value'))

    def to_snake(self, name):
        s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
        return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()


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

    def get_stats(self, mode=Mode.SQUAD):
        return Stats(self._stats.get(mode.value))


class Stats(Domain):
    """Object containing stats items attributes"""
    def __str__(self):
        general_stats = {
            'wins': 'Top 1',
            'top3': 'Top 3',
            'top5': 'Top 5',
            'top10': 'Top 10',
            'winratio': 'Win Ratio',
            'kills': 'Kills',
            'kills_match': 'Kills/Match',
        }
        stats = ''
        for stat in general_stats:
            if hasattr(self, stat):
                stats += ("%s: %s\n") % (general_stats[stat],
                    getattr(self, stat))
        return stats


class Challenge(Domain):
    """Object containing challenge items attributes"""
    def from_json(self):
        """Takes in arguments and sets attributes to default by placement"""
        super().from_json()
        self.name = self.metadata[1].get('value')
        self.quest_completed = self.metadata[2].get('value')
        self.quest_total = self.metadata[3].get('value')
        self.reward_picture_url = self.metadata[4].get('value')
        self.reward_name = self.metadata[5].get('value')


class StoreItem(Domain):
    """Object containing store items attributes"""


class Match(Domain):
    """Object containing match attributes"""
