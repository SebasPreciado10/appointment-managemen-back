from core.exceptions.base import (
    ElementAlreadyExists,
    ElementNotFound,
)

class ProductSublineAlreadyExists(ElementAlreadyExists):
    pass

class ProductSublineNotFound(ElementNotFound):
    pass
