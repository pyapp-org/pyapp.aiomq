import logging

from typing import Sequence
from pyapp_ext.aiobotocore import create_client

from ..base import TaskQueue, PubSubQueue

logger = logging.getLogger(__name__)


class SQS(TaskQueue):
    """
    SQS based task queue
    """

    def __init__(self, *, url: str, aws_credentials: str = None):
        self.url = url

        self.client = create_client("SQS", aws_credentials)

    async def create(self, name):
        pass

    async def send(self, message: str):
        self.client.sendMessage(
            URL=self.url,
            MessageBody=message
        )

    async def receive(self, count: int = 1) -> Sequence[str]:
        self.client

    async def listen(self):
        pass


class SNS(PubSubQueue):
    """
    SNS based pub/sub queue.
    """
    async def publish(self, message: str, topic: str):
        pass

    async def subscribe(self, topic: str):
        pass

    async def cancel_subscription(self, topic: str):
        pass