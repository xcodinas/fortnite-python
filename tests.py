import pytest

from fortnite_python.base import Fortnite
from fortnite_python.exceptions import UnauthorizedError, NotFoundError


def test_unauthorized():
    fortnite = Fortnite('')
    pytest.raises(UnauthorizedError, fortnite.player, 'test')
