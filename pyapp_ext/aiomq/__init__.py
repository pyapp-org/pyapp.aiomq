"""
pyApp Asyncio Message Queuing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""
from pyapp.app import CommandGroup, argument
from pyapp import injection

from .base import *
from .factory import *


class Extension:
    """
    Asyncio Message Queuing Extension
    """
    default_settings = ".default_settings"
    checks = ".checks"

    @staticmethod
    def register_commands(root: CommandGroup):
        pass

    @staticmethod
    def ready():
        injection.register_factory(TaskQueue, task_queue_factory.create)
        injection.register_factory(PubSubQueue, pubsub_queue_factory.create)
