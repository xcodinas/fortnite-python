import pytest
import os

from fortnite_python.base import Fortnite
from fortnite_python.exceptions import UnauthorizedError, UnknownPlayerError


def test_unauthorized():
    fortnite = Fortnite('')
    pytest.raises(UnauthorizedError, fortnite.player, 'test')


def test_notfound():
    fortnite = Fortnite(os.environ.get("fortnite_api_key"))
    pytest.raises(UnknownPlayerError, fortnite.player, 'test')
