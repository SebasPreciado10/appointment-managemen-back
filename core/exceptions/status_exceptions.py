from core.exceptions.base import (
    ElementAlreadyExists,
    ElementNotFound,
)

class StatusAlreadyExists(ElementAlreadyExists):
    pass

class StatusNotFound(ElementNotFound):
    pass