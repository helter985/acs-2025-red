# This file makes the models directory a Python package 

from app.models.product_model import Product
from app.models.user_model import User
from app.models.task_model import Task

__all__ = ['Product', 'User', 'Task'] 