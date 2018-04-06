import pytest
import os

from fortnite_python.base import Fortnite
from fortnite_python.domain import Mode, Platform
from fortnite_python.exceptions import UnauthorizedError, UnknownPlayerError


def test_unauthorized():
    fortnite = Fortnite('')
    pytest.raises(UnauthorizedError, fortnite.player, 'test')


def test_notfound():
    fortnite = Fortnite(os.environ.get("fortnite_api_key"))
    pytest.raises(UnknownPlayerError, fortnite.player, 'test')


def test_platform():
    fortnite = Fortnite(os.environ.get("fortnite_api_key"))

    # Test wrong Platform
    with pytest.raises(AttributeError):
        player = fortnite.player('ninja', Platform.playstation)

    # Check that if it's empty returns PC platform
    player = fortnite.player('ninja')
    assert player.platform == 'pc'

    player = fortnite.player('ninja', Platform.PC)
    assert player.platform == 'pc'

    player = fortnite.player('RawXB', Platform.XBOX)
    assert player.platform == 'xbox'

    player = fortnite.player('AlexRamiGaming', Platform.PSN)
    assert player.platform == 'psn'


def test_stats():
    fortnite = Fortnite(os.environ.get("fortnite_api_key"))
    player = fortnite.player('ninja')

    # Test wrong mode
    with pytest.raises(AttributeError):
        player.getStats(Mode.duo)

    # Check that if empty returns squad
    stats = player.getStats()
    assert stats.wins
    assert stats.total
    assert stats.kd
    assert stats.winratio
    assert stats.kills
    assert stats.score
    assert stats.score_match
    assert stats.kills_match
    assert stats.top3
    assert stats.top5
    assert stats.top6
    assert stats.top10
    assert stats.top12
    assert stats.top25
    assert stats.avg_time
