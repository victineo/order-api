class HttpNotFoundError(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)
        self.name = "NotFound"
        self.message = message
        self.status_code = 404
