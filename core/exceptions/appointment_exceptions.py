from core.exceptions.base import ElementNotFound, ElementAlreadyExists

class AppointmentAlreadyExists(ElementAlreadyExists):
   pass

class AppointmentNotFound(ElementNotFound):
   pass