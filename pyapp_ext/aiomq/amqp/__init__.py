import logging

from typing import Sequence
from pyapp_ext.aio_pika import Connection, connection_factory

from ..import base

logger = logging.getLogger(__name__)


class TaskQueue(base.TaskQueue):
    """
    Pika based task queue
    """
    def __init__(self, *, name: str, amqp_config: str = None):
        self.name = name
        self.config = amqp_config

        self._connection: Connection = None

    async def open(self):
        self._connection = connection_factory(self.config)

    async def close(self):
        if self._connection:
            await self._connection.close()
            self._connection = None

    async def send(self, message: str):
        pass

    async def receive(self, count: int = 1) -> Sequence[str]:
        pass

    async def listen(self):
        pass
