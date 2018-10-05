import re

from enum import Enum


class Platform(Enum):
    PC = 'pc'
    XBOX = 'xbl'
    PSN = 'psn'


class Mode(Enum):
    SOLO = 'p2'
    DUO = 'p10'
    SQUAD = 'p9'


class Domain:
    def __init__(self, data, meta=None):
        self._data = data
        self.from_json()

    def __repr__(self):
        return '<{0} {1}>'.format(self.__class__.__name__, self.id)

    def __str__(self):
        return str(self.id)

    def from_json(self):
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
    def __repr__(self):
        return '<{0} {1} {2}>'.format(
            self.__class__.__name__, self.id, self.platform)

    def from_json(self):
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
    def from_json(self):
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
