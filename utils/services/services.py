from utils.error_handlers.error_handlers import RoleNotFoundError
from applications.users.models import Employee, Admin
from applications.users.roles import Role
import logging

logger=logging.getLogger(__name__)

def assign_user_role(admin_user:Admin, target_user:Employee, role_name=str):
    """
    Assigns a role to a user. Only callable by an Admin model instance.
    :param admin_user: instance of Admin.
    :param target_user: instance of Employee, or of its subclasses.
    :param role_name: name of the role to be assigned to target_user.
    :raise: PermissionError if the user is not an Admin model
    :raise: RoleNotFoundError if assigned role does not exist in roles.py
    """

    if not admin_user.is_staff:
        raise PermissionError('You do not have administrative privileges to perform this action:'
                              'Please contact your local administrator.')

    try:
        role= Role.roles.get_role_by_name(role_name)
    except RoleNotFoundError as error:
        logger.error(f'Failed to assign role "{role_name}": {error}')
        raise error

    target_user.role= role
    target_user.save()

    logger.info(f'Role "{role}" assigned to user {target_user} successfully!')

    return f'"{target_user}" successfully assigned a new role:{role}'