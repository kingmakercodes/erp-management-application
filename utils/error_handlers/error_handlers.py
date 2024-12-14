"""
This file defines custom error handlers for application
"""

import logging


logger= logging.getLogger(__name__)


class ApplicationError(Exception):
    """Base application exception model for all application-specific errors"""

    def __init__(self, message:str=None, details:str=None, log=logging.ERROR):
        """
        :param message: Descriptive error message.
        :param details: Optional additional details about the error.
        :param log: Log level for the exception.
        """

        super().__init__(message)
        self.message= message
        self.details= details
        self.log= log

    def log(self, log):
        log_message= f'{self.__class__.__name__}: {self.message}'
        if self.details:
            log_message+= f' | Details: {self.message}'
        logger.log(log, log_message)

    def __str__(self):
        return f'{self.__class__.__name__}: {self.message}' + (f'Details: {self.details}' if self.details else'')


class RoleNotFoundError(ApplicationError):
    """Exception raised when a role does not exist or is not defined"""

    def __init__(self, role_name=None, details=None):
        if role_name:
            message=f'Role "{role_name}" does not exist.'
            super().__init__(message=message, details=details)

        f'Role not found!'


class InvalidRoleAssignmentError(ApplicationError):
    """Exception raised for invalid role assignment"""

    def __init__(self, role_name=None, details=None):
        if role_name:
            message=f'Invalid assignment for role"{role_name}"'
            super().__init__(message=message, details=details)