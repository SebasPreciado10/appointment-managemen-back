from rest_framework.exceptions import APIException
from rest_framework import status


class ElementNotFound(APIException):
    status_code = status.HTTP_404_NOT_FOUND
    default_detail = "El elemento no fue encontrado."
    default_code = "not_found"


class ElementAlreadyExists(APIException):
    status_code = status.HTTP_409_CONFLICT
    default_detail = "El elemento ya existe."
    default_code = "conflict"


class ElementHasRelationship(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = "El elemento tiene relaciones asociadas y no puede ser eliminado."
    default_code = "related_object"