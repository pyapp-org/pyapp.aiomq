from pyapp.checks.registry import register

from .factory import task_queue_factory, pubsub_queue_factory

register(task_queue_factory)
register(pubsub_queue_factory)
