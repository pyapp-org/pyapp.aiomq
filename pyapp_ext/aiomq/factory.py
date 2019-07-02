from pyapp.conf.helpers import NamedPluginFactory
from typing import Type

from .base import TaskQueue, PubSubQueue

__all__ = ("task_queue_factory", "pubsub_queue_factory")


task_queue_factory = NamedPluginFactory[TaskQueue]("TASK_QUEUES", abc=Type[TaskQueue])
pubsub_queue_factory = NamedPluginFactory[PubSubQueue]("PUBSUB_QUEUES", abc=Type[PubSubQueue])
