class ResponseTypes:
    PARAMETERS_ERROR = "ParametersError"
    RESOURCE_ERROR = "ResourceError"
    SYSTEM_ERROR = "SystemError"
    NOT_FOUND_ERROR = "NotFoundError"
    SUCCESS = "Success"
    CREATE = "Create"
    DELETE = "Delete"


class ResponseFailure:
    def __init__(self, type_, message):
        self.type = type_
        self.message = self._format_message(message)

    def _format_message(self, msg):
        if isinstance(msg, Exception):
            return "{}: {}".format(msg.__class__.__name__, "{}".format(msg))
        return msg

    @property
    def value(self):
        return {"type": self.type, "message": self.message}

    def __bool__(self):
        return False


class ResponseSuccess:
    def __init__(self, value=None):
        self.type = ResponseTypes.SUCCESS
        self.value = value

    def __bool__(self):
        return True


class ResponseCreate:
    def __init__(self, value=None):
        self.type = ResponseTypes.CREATE
        self.value = value

    def __bool__(self):
        return True


class ResponseDelete:
    def __init__(self, value=None):
        self.type = ResponseTypes.DELETE
        self.value = value

    def __bool__(self):
        return True
