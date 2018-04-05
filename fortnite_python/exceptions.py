class UnauthorizedError(Exception):
    def __init__(self, message='API key invalid or missing'):
        super().__init__(message)


class NotFoundError(BaseException):
    def __init__(self, message='The specified resource was not found'):
        super().__init__()
