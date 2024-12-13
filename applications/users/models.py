"""
This file contains business-specific models for database user models: Employee, Administrator, Manager, Staff
"""

from django.db import models
from django.core.exceptions import ValidationError
import logging