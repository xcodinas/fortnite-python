import unittest

from fortnite_python.base import Fortnite
from fortnite_python.exceptions import UnauthorizedError, NotFoundError


class TestStringMethods(unittest.TestCase):

    def test_unauthorized(self):
        fortnite = Fortnite('')
        self.assertRaises(UnauthorizedError, fortnite.player, 'test')

if __name__ == '__main__':
    unittest.main()
