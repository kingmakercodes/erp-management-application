from utils.error_handlers.error_handlers import RoleNotFoundError
from django.db import models

class RoleManager(models.Manager):
    """
    Custom manager to encapsulate dynamic role lookup logic
    """
    def get_role_by_name(self, name):
        """
        Dynamically fetches argued role by name
        :param name: defined name of the role
        :raise: RoleNotFoundError if name does not exist
        """
        try:
            return self.get(name=name)
        except self.model.ObjectDoesNotExist:
            raise RoleNotFoundError(
                role_name=name,
                details=f'Attempted to retrieve role "{name}", but it does not exist or is not defined yet in database.'
            )


class Role(models.Model):
    """
    Role model to dynamically store roles
    """
    name= models.CharField(max_length=60, unique=True, null=False)
    roles= RoleManager()

    def __str__(self):
        return self.name