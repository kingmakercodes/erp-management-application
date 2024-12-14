"""
This file contains business-specific models for database user models: Employee, Administrator, Manager, Staff
"""

from django.db import models
from argon2 import PasswordHasher
from django.core.exceptions import ValidationError
from argon2.exceptions import VerifyMismatchError
from utils.error_handlers.error_handlers import RoleNotFoundError
import logging

logger= logging.getLogger(__name__)

class Employee(models.Model):

    email= models.EmailField(unique=True)
    password_hash= models.CharField(max_length=255)
    username= models.CharField(max_length=40, blank=True)
    first_name= models.CharField(max_length=40, blank=True)
    last_name= models.CharField(max_length=40, blank=True)
    phone_number= models.CharField(max_length=15, blank=True, null=True)

    is_active= models.BooleanField(default=True)
    is_staff= models.BooleanField(default=True)
    role= models.ForeignKey('roles.Role', null=True, blank=True, on_delete=models.SET_NULL)

    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now_add=True)

    _hasher= PasswordHasher()

    class Meta:
        abstract= True

    def __init__(self, *args, **kwargs):
        super().__init__(*args, *kwargs)
        print(f'Initialized AbstractUser: {self}')

    def set_password(self, password):
        self.password_hash= self._hasher.hash(password)

    def check_password(self, password):
        try:
            return self._hasher.verify(self.password_hash, password)
        except VerifyMismatchError:
            return False

    def clean(self):
        """Validates the model fields before saving"""
        if not self.username:
            logger.error('Validation Error: Username field is required yet empty.')
            raise ValidationError('Username cannot be empty!')
        if not self.email:
            logger.error('Validation Error: Email field is required yet empty.')
            raise ValidationError('Email cannot be empty!')

    def save(self, *args, **kwargs):
        """Overrides the save method to add login"""
        try:
            self.clean() # call clean to validate the fields
            super().save(*args, **kwargs)
        except ValidationError as error:
            logger.error(f'Error saving "Employee": {error}')
            raise
        except Exception as error:
            logger.error(f'Unexpected error in "Employee.save": {error}')
            raise

    def __repr__(self):
        return f'<AbstractUser(email={self.email}, username:{self.username})>'


class Admin(Employee):
    """Model for Administrator roles"""
    additional_admin_field= models.CharField(max_length=50, blank=True, null=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print(f'Initialized Admin: {self}')

    def __repr__(self):
        return f'<Admin(email:{self.email}, username={self.username})>'

    def assign_role(self, target_user:Employee, role_name:str):
        """
        Delegates role assignment logic to the service layer
        """
        from utils.services.services import assign_user_role
        try:
            result= assign_user_role(self, target_user, role_name)
            logger.info(result)
        except RoleNotFoundError as e:
            logger.error(e)
            return e


class Manager(Employee):
    """Model for Manager roles"""
    department= models.CharField(max_length=100, blank=True, null=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print(f'Initialized Manager: {self}')

    def __repr__(self):
        return f'<Manager(email={self.email}, username={self.username})>'


class Staff(Employee):
    """Model for Staff roles"""
    supervisor= models.ForeignKey(
        'self', on_delete=models.SET_NULL, null=True, blank=True, related_name='subordinates'
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print(f'Initialized Staff: {self}')

    def __repr__(self):
        return f'<Staff(email={self.email}, username={self.username})>'