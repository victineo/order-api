class HttpUnauthorizedError(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)
        self.name = "Unauthorized"
        self.message = message
        self.status_code = 401
