class UnauthorizedError(Exception):
    """"Raises an error that the current API key is invalid or missing"""
    def __init__(self, message='API key invalid or missing'):
        super().__init__(message)


class NotFoundError(BaseException):
    """Raises an error that a remote resource was not found"""
    def __init__(self, message='The specified resource was not found'):
        super().__init__()


class UnknownPlayerError(BaseException):
    """Raises an error when a player does not exist via the API"""
    def __init__(self, message='The specified player was not found'):
        super().__init__()
