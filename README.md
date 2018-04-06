[![Build Status](https://travis-ci.org/xcodinas/fortnite-python.svg?branch=master)](https://travis-ci.org/xcodinas/fortnite-python)
[![PyPI version](https://badge.fury.io/py/fortnite-python.svg)](https://badge.fury.io/py/fortnite-python)
[![Requirements Status](https://requires.io/github/xcodinas/fortnite-python/requirements.svg?branch=master)](https://requires.io/github/xcodinas/fortnite-python/requirements/?branch=master)

# fortnite-python
Python wrapper for http://fortnitetracker.com/ api.

## Installation

You can install it via pip

```
pip install fortnite-python
```


## Usage

You need to register for an api key at https://fortnitetracker.com/site-api

Then it's just easy as:

```
from fortnite_python import Fortnite

fortnite = Fortnite('Given api key')
```


Retrieving a player:

```
>>> from fortnite_python import Fortnite

>>> fortnite = Fortnite('Given api key')
>>> player = fortnite.player('playername')
player

<Player 20a8fafaa-6chfj-6455-b715-2424fff pc>

```

The default platform is PC, if you want to use a diferent platform you should
do it this way:

```
>>> from fortnite_python import Fortnite
>>> from fortnite_python.domain import Platform

>>> fortnite = Fortnite('Given api key')
>>> player = fortnite.player('playername', Platform.XBOX)
>>> player
<Player 20a8fafaa-6chfj-6455-b715-2424fff xb1>


```

You can check the available platforms [here](https://github.com/xcodinas/fortnite-python/blob/master/fortnite_python/domain.py#L4)


Retrieving player stats:


```
>>> from fortnite_python import Fortnite
>>> from fortnite_python.domain import Mode

>>> fortnite = Fortnite('Given api key')
>>> player = fortnite.player('playername')
>>> stats = player.getStats(Mode.DUO)
>>> stats.wins
'10'
>>> stats.top3
'20'

```
You can check the available modes [here](https://github.com/xcodinas/fortnite-python/blob/master/fortnite_python/domain.py#L10)
