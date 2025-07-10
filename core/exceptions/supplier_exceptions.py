from core.exceptions.base import (
    ElementAlreadyExists,
    ElementNotFound,
)

class SupplierAlreadyExists(ElementAlreadyExists):
    pass

class SupplierNotFound(ElementNotFound):
    pass