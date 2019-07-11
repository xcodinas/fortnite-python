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


#### Retrieving a player:

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


#### Retrieving player stats:


```
>>> from fortnite_python import Fortnite
>>> from fortnite_python.domain import Mode

>>> fortnite = Fortnite('Given api key')
>>> player = fortnite.player('playername')
>>> stats = player.get_stats(Mode.DUO)
>>> stats.wins
'10'
>>> stats.top3
'20'
```

You can check the available modes [here](https://github.com/xcodinas/fortnite-python/blob/master/fortnite_python/domain.py#L10)


#### Getting matches data:

When calling matches you have to pass the player id and the number of matches
you want (from 1 to 50)

```
>>> player = fortnite.player('playername')
<Player 20a8fafaa-6chfj-6455-b715-2424fff pc>

>>> fortnite.matches(player.id, 5)
[<Match 806686859>, <Match 806611889>, <Match 806602331>, <Match 806532871>,
    <Match 806522998>]
```


#### Retrieving the current Challenges:

```
>>> from fortnite_python import Fortnite

>>> fortnite = Fortnite('Given api key')
>>> challenges = fortnite.challenges()
>>> print (challenges)
[<Challenge 1>, <Challenge 1>, <Challenge 1>, <Challenge 1>, <Challenge 1>, <Challenge 1>, <Challenge 1>]
>>> challenges[0].name
Visit all of the Corrupted Areas
>>> challenges[0].reward_picture_url
https://cdn.thetrackernetwork.com/cdn/trackernetwork/63D2upload.png
```

#### Retrieving the current Fortnite store:

```
>>> from fortnite_python import Fortnite

>>> fortnite = Fortnite('Given api key')
>>> store = fortnite.store()
>>> fortnite.store()
[<StoreItem 1974>, <StoreItem 6010>, <StoreItem 1246>, <StoreItem 6012>,
<StoreItem 918>, <StoreItem 4835>, <StoreItem 6050>, <StoreItem 5981>]
```
