from src.response import ResponseTypes


class CustomError(Exception):
    """Exception that catches all other exceptions that inherit from it"""

    type = ResponseTypes.SYSTEM_ERROR

    def __init__(self, message, extra=None):
        self.message = message
        self.extra = extra


class ParametersError(CustomError, ValueError):
    """Parameters Error"""

    type = ResponseTypes.PARAMETERS_ERROR


class NotFoundError(CustomError):
    type = ResponseTypes.NOT_FOUND_ERROR


class NoContentError(CustomError):
    type = ResponseTypes.RESOURCE_ERROR


class InvalidRequest(CustomError):
    type = ResponseTypes.RESOURCE_ERROR
